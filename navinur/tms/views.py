# Views for the tile map server

from django.http import HttpResponse
from django.http import Http404
import traceback
import math
import mapnik
import logging

TILE_WIDTH = 256
TILE_HEIGHT = 256
# overview, general, coastal, approach
MAX_ZOOM_LEVEL = 11

def root(request):
    try:
        base_url = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding="utf-8" ?>')
        xml.append('<Services>')
        xml.append('    <TileMapService ' +
                   'title = "Navinur tile map service" ' +
                   'version = "1.0" href=" ' + base_url + '1.0" />')
        xml.append('</Services>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def service(request, version, route_id):
    # creation of a service xml file which will be accessed by Openlayers
    try:
        if version != "1.0":
            raise Http404
        base_url = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding = "utf-8" ?>')
        xml.append('<TileMapService version="1.0" services="' + base_url + '">')
        xml.append('<Title> Navinur Tile Map Service</Title>')
        xml.append('<Abstract></Abstract>')
        xml.append('    <TileMaps>')
        xml.append('       <TileMap title= "Bay of Mexico" srs="EPSG:4326" href= "' + base_url + '/' + route_id + '"/>')
        xml.append('    </TileMaps>')
        xml.append('</TileMapService>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def tile_map(request, version, route_id):
    print("Request looks like:{}".format(request))
    if version != "1.0":
        raise Http404
    try:
        base_url = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding = "utf-8" ?>')
        xml.append('<TileMap version ="1.0" tilemapservice = "' + base_url + '">')
        xml.append('    <Title>Bay of Mexico</Title>')
        xml.append('    <Abstract></Abstract>')
        xml.append('    <SRS>EPSG:4326</SRS>')
        xml.append('    <BoundingBox minx="-180" miny="-90" maxx="180" maxy="90" />')
        xml.append('    <Origin x = "" y = "" />')
        xml.append('    <TileFormat width="' + str(TILE_WIDTH) + '" height="' + str(TILE_HEIGHT) + '"'
                   + ' mime-type="image/png" extension="png"/>')
        xml.append('    <TileSets profile="global-geodetic">')
        for zoomLevel in range(0, MAX_ZOOM_LEVEL + 1):
            units_per_pixel = _units_per_pixel(zoomLevel)
            xml.append('    <TileSet href = "' + base_url + '/' + str(zoomLevel) + '" units-per-pixel ="' + str(
                units_per_pixel) + '" order = "' + str(zoomLevel) + '"/>')
        xml.append('    </TileSets>')
        xml.append('</TileMap>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def tile(request, version, route_id, zoom, x, y):
    try:
        # check parameters are specified correctly
        if version != "1.0":
            raise Http404

        zoom = int(zoom)
        x = int(x)
        y = int(y)

        # check level of zoom specified correctly
        if zoom < 0 or zoom > MAX_ZOOM_LEVEL:
            raise Http404

        # determining the extent of a tile a the given zoom level
        x_extent = _units_per_pixel(zoom) * TILE_WIDTH
        y_extent = _units_per_pixel(zoom) * TILE_HEIGHT

        # convert x and y into min and max lat and lon values covered by tile
        min_long = x * x_extent - 180
        min_lat = y * y_extent - 90
        max_long = min_long + x_extent
        max_lat = min_lat + y_extent

        # ensure the values specified for each tile are correct
        if min_long < -180 or max_long > 180 or min_lat < -90 or max_lat > 90:
            raise Http404

        # set up mapnik map
        map = mapnik.Map(TILE_WIDTH, TILE_HEIGHT, "+proj=longlat +datum=WGS84")
        map.background = mapnik.Color("#7391ad")

        # TODO fix these links
        mapfile = "/home/lstefa/repos/project_navinur/navinur/tms/style/map_file.xml"


        common_params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost')

        ocean_layer = mapnik.Layer("OceanBase")
        params = common_params
        params['table'] = 'ne_50m_ocean'
        data_source = mapnik.PostGIS(**params)
        ocean_layer.datasource = data_source
        ocean_layer.styles.append("OceanBase")
        map.layers.append(ocean_layer)

        base_land_layer = mapnik.Layer("LandBase")
        params = common_params
        params['table'] = 'tms_basemap'
        data_source = mapnik.PostGIS(**params)
        base_land_layer.datasource = data_source
        base_land_layer.styles.append("BaseLayer")
        base_land_layer.styles.append("BaseLayerText")
        map.layers.append(base_land_layer)

        overview_land_area_layer = mapnik.Layer("OverviewLandArea")
        params = common_params
        params['table'] = 'overview_land_area'
        data_source = mapnik.PostGIS(**params)
        overview_land_area_layer.datasource = data_source
        overview_land_area_layer.styles.append("OverviewLandArea")
        map.layers.append(overview_land_area_layer)

        overview_land_line_layer = mapnik.Layer("OverviewLandLine")
        params = common_params
        params['table'] = 'overview_land_area_line'
        data_source = mapnik.PostGIS(**params)
        overview_land_line_layer.datasource = data_source
        overview_land_line_layer.styles.append("OverviewLandLine")
        map.layers.append(overview_land_line_layer)

        overview_coastline_layer = mapnik.Layer("OverviewCoastline")
        params = common_params
        params['table'] = 'overview_coastline_line'
        data_source = mapnik.PostGIS(**params)
        overview_coastline_layer.datasource = data_source
        overview_coastline_layer.styles.append("OverviewCoastline")
        map.layers.append(overview_coastline_layer)

        overview_depth_area = mapnik.Layer("OverviewDepthArea")
        params = common_params
        params['table'] = 'overview_depth_area'
        data_source = mapnik.PostGIS(**params)
        overview_depth_area.datasource = data_source
        overview_depth_area.styles.append("OverviewdDepthArea")
        overview_depth_area.styles.append("DryingHeight")
        map.layers.append(overview_depth_area)

        overview_depthcontour_layer = mapnik.Layer("OverviewDepthContour")
        params = common_params
        params['table'] = 'overview_depth_contour_line'
        data_source = mapnik.PostGIS(**params)
        overview_depthcontour_layer.datasource = data_source
        overview_depthcontour_layer.styles.append("OverviewDepthContour")
        map.layers.append(overview_depthcontour_layer)

        overview_river_line_layer = mapnik.Layer("OverviewRiverLine")
        params = common_params
        params['table'] = 'overview_river_line'
        data_source = mapnik.PostGIS(**params)
        overview_river_line_layer.datasource = data_source
        overview_river_line_layer.styles.append("OverviewRiverLine")
        map.layers.append(overview_river_line_layer)

        general_land_area_layer = mapnik.Layer("GeneralLandArea")
        params = common_params
        params['table'] = 'general_land_area'
        data_source = mapnik.PostGIS(**params)
        general_land_area_layer.datasource = data_source
        general_land_area_layer.styles.append("GeneralLandArea")
        map.layers.append(general_land_area_layer)

        general_land_line_layer = mapnik.Layer("GeneralLandLine")
        params = common_params
        params['table'] = 'general_land_area_line'
        data_source = mapnik.PostGIS(**params)
        general_land_line_layer.datasource = data_source
        general_land_line_layer.styles.append("GeneralLandLine")
        map.layers.append(general_land_line_layer)

        general_coast_line_layer = mapnik.Layer("GeneralCoastLine")
        params = common_params
        params['table'] = 'general_coastline_line'
        data_source = mapnik.PostGIS(**params)
        general_coast_line_layer.datasource = data_source
        general_coast_line_layer.styles.append("GeneralCoastline")
        map.layers.append(general_coast_line_layer)

        general_depth_area_layer = mapnik.Layer("GeneralDepthArea")
        params = common_params
        params['table'] = 'general_depth_area'
        data_source = mapnik.PostGIS(**params)
        general_depth_area_layer.datasource = data_source
        general_depth_area_layer.styles.append("GeneralDepthArea")
        general_depth_area_layer.styles.append("DryingHeight")
        map.layers.append(general_depth_area_layer)

        general_depthContour_layer = mapnik.Layer("GeneralDepthContour")
        params = common_params
        params['table'] = 'general_depth_contour_line'
        data_source = mapnik.PostGIS(**params)
        general_depthContour_layer.datasource = data_source
        general_depthContour_layer.styles.append("GeneralDepthContour")
        map.layers.append(general_depthContour_layer)

        general_river_line_layer = mapnik.Layer("GeneralRiverLine")
        params = common_params
        params['table'] = 'general_river_line'
        data_source = mapnik.PostGIS(**params)
        general_river_line_layer.datasource = data_source
        general_river_line_layer.styles.append("GeneralRiverLine")
        map.layers.append(general_river_line_layer)

        general_wreck_point_layer = mapnik.Layer("GeneralWreckPoint")
        params = common_params
        params['table'] = 'general_wreck_point'
        data_source = mapnik.PostGIS(**params)
        general_wreck_point_layer.datasource = data_source
        general_wreck_point_layer.styles.append("GeneralWreckPoint")
        map.layers.append(general_wreck_point_layer)

        general_buoy_layer = mapnik.Layer("GeneralBuoyPoint")
        params = common_params
        params['table'] = 'general_buoy_special_purpose_general_point'
        data_source = mapnik.PostGIS(**params)
        general_buoy_layer.datasource = data_source
        general_buoy_layer.styles.append("GeneralBuoyPoint")
        map.layers.append(general_buoy_layer)

        general_anchorage_layer = mapnik.Layer("GeneralAnchorage")
        params = common_params
        params['table'] = 'general_anchorage_area'
        data_source = mapnik.PostGIS(**params)
        general_anchorage_layer.datasource = data_source
        general_anchorage_layer.styles.append("GeneralAnchorage")
        map.layers.append(general_anchorage_layer)

        general_land_region_layer = mapnik.Layer("GeneralLandRegion")
        params = common_params
        params['table'] = 'general_land_region_point'
        data_source = mapnik.PostGIS(**params)
        general_land_region_layer.datasource = data_source
        general_land_region_layer.styles.append("GeneralLandRegionText")
        map.layers.append(general_land_region_layer)

        coastal_land_line_layer = mapnik.Layer("CoastalLandLine")
        params = common_params
        params['table'] = 'coastal_land_area_line'
        data_source = mapnik.PostGIS(**params)
        coastal_land_line_layer.datasource = data_source
        coastal_land_line_layer.styles.append("CoastalLandLine")
        map.layers.append(coastal_land_line_layer)

        coastal_depth_area_layer = mapnik.Layer("CoastalDepthArea")
        params = common_params
        params['table'] = 'coastal_depth_area'
        data_source = mapnik.PostGIS(**params)
        coastal_depth_area_layer.datasource = data_source
        coastal_depth_area_layer.styles.append("CoastalDepthArea")
        coastal_depth_area_layer.styles.append("DryingHeight")
        coastal_depth_area_layer.styles.append("DepthAreaText")
        map.layers.append(coastal_land_line_layer)

        coastal_depth_contour_layer = mapnik.Layer("CoastalDepthContour")
        params = common_params
        params['table'] = 'coastal_depth_contour_line'
        data_source = mapnik.PostGIS(**params)
        coastal_depth_contour_layer.datasource = data_source
        coastal_depth_contour_layer.styles.append("CoastalDepthContour")
        map.layers.append(coastal_depth_contour_layer)

        coastal_river_line_layer = mapnik.Layer("CoastalRiverLine")
        params = common_params
        params['table'] = 'coastal_river_line'
        data_source = mapnik.PostGIS(**params)
        coastal_river_line_layer.datasource = data_source
        coastal_river_line_layer.styles.append("CoastalRiverLine")
        map.layers.append(coastal_river_line_layer)

        coastal_wreck_point_layer = mapnik.Layer("CoastalWreckPoint")
        params = common_params
        params['table'] = 'coastal_wreck_point'
        data_source = mapnik.PostGIS(**params)
        coastal_wreck_point_layer.datasource = data_source
        coastal_wreck_point_layer.styles.append("CoastalWreckPoint")
        map.layers.append(coastal_wreck_point_layer)

        coastal_buoy_layer = mapnik.Layer("CoastalBuoyPoint")
        params = common_params
        params['table'] = 'coastal_buoy_special_purpose_general_point'
        data_source = mapnik.PostGIS(**params)
        coastal_buoy_layer.datasource = data_source
        coastal_buoy_layer.styles.append("CoastalBuoy")
        map.layers.append(coastal_buoy_layer)

        coastal_land_region_layer = mapnik.Layer("CoastalLandRegionText")
        params = common_params
        params['table'] = 'coastal_land_region_point'
        data_source = mapnik.PostGIS(**params)
        coastal_land_region_layer.datasource = data_source
        coastal_land_region_layer.styles.append("CoastalLandRegionText")
        map.layers.append(coastal_land_region_layer)

        coastal_anchorage_layer = mapnik.Layer("CoastalAnchorageArea")
        params = common_params
        params['table'] = 'coastal_anchorage_area'
        data_source = mapnik.PostGIS(**params)
        coastal_anchorage_layer.datasource = data_source
        coastal_anchorage_layer.styles.append("CoastalAnchorageArea")
        map.layers.append(coastal_anchorage_layer)

        route_layer = mapnik.Layer("Route", "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

        if route_id != "0":
            query = "(select * from test_routes where gid=" + route_id + ") as route"
            params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost',
                          table=query, geometry_field='geom')
            data_source = mapnik.PostGIS(**params)
            route_layer.datasource = data_source

            route_layer.styles.append("Route")

    # TODO fix these links
        map.layers.append(route_layer)

        if False:
            map = mapnik.Map(TILE_WIDTH, TILE_HEIGHT, "+proj=longlat +datum=WGS84")
            map.background = mapnik.Color("#7391ad")
            mapfile = "/home/lstefa/repos/project_navinur/navinur/tms/style/map_combined_old.xml"

        mapnik.load_map(map, mapfile)
        box = mapnik.Box2d(min_long, min_lat, max_long, max_lat)
        map.zoom_to_box(box)

        image = mapnik.Image(TILE_WIDTH, TILE_HEIGHT)
        mapnik.render(map, image)
        image_data = image.tostring("png")

        return HttpResponse(image_data, content_type="image/png")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def _units_per_pixel(zoom_level):
    return 0.703125 / math.pow(2, zoom_level)




