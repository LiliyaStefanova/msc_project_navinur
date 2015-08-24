# Views for the tile map server

from django.http import HttpResponse
from django.http import Http404
import traceback
import math
import mapnik


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

        # Ocean base
        common_params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost')

        ocean_layer = mapnik.Layer("OceanBase")
        params = common_params
        params['table'] = 'ne_50m_ocean'
        data_source = mapnik.PostGIS(**params)
        ocean_layer.datasource = data_source
        ocean_layer.styles.append("oceanBase")
        map.layers.append(ocean_layer)

        # Land base
        base_layer = mapnik.Layer("LandBase")
        params = common_params
        params['table'] = 'tms_basemap'
        data_source = mapnik.PostGIS(**params)
        base_layer.datasource = data_source
        base_layer.styles.append("baseLayer")
        base_layer.styles.append("baseLayerText")
        map.layers.append(base_layer)

        # Overview land
        overview_land_layer = mapnik.Layer("LandBase")
        params = common_params
        params['table'] = 'overview_land_area'
        data_source = mapnik.PostGIS(**params)
        overview_land_layer.datasource = data_source
        overview_land_layer.styles.append("OverviewLandArea")
        map.layers.append(overview_land_layer)

        path_grid_layer = mapnik.Layer("PathGrid")
        params = common_params
        query = "(select ST_Transform(geom, 32616) from path_grid) as grid"
        params['table'] = query
        params['srid'] = '32616'
        params['geometry_field'] = 'geom'
        data_source = mapnik.PostGIS(**params)
        path_grid_layer.datasource = data_source
        path_grid_layer.styles.append("grid")
        map.layers.append(path_grid_layer)

        route_layer = mapnik.Layer("Routes")

        if route_id != "0":
            query = "(select ST_Transform(geom, 4326) from test_routes) as routes"
            params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost',
                          table=query, srid='32616', geometry_field='geom')

        data_source = mapnik.PostGIS(**params)
        route_layer.datasource = data_source

        route_layer.styles.append("route")

    # TODO fix these links
        map.layers.append(route_layer)
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

#
#
#
#
# < Layer
# name = "OverviewLandLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > OverviewLandLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > overview_land_area_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "OverviewCoastLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > OverviewCoastLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > overview_coastline_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "OverviewDepthArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > OverviewDepthArea < / StyleName >
# < StyleName > DryingHeight < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > overview_depth_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "OverviewDepthContour"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > OverviewDepthContour < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > overview_depth_contour_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "OverviewRiverLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > OverviewRiverLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > overview_river_line < / Parameter >
# < / Datasource >
# < / Layer >
#
# < Layer
# name = "GeneralCoverageArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > coverageArea < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_coverage_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralLandArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralLandArea < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_land_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralLandLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralLandLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_land_area_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralCoastline"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralCoastline < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_coastline_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralDepthArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralDepthArea < / StyleName >
# < StyleName > DryingHeight < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_depth_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralDepthContour"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralDepthContour < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_depth_contour_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralRiverLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralRiverLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_river_line < / Parameter >
# < / Datasource >
# < / Layer >
#
# < Layer
# name = "GeneralWreckPoint"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralWreckPoint < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_wreck_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralBuoy"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralBuoy < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_buoy_special_purpose_general_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralAnchorage"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralAnchorage < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_buoy_special_purpose_general_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "GeneralLandRegionText"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > GeneralLandRegionText < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > general_land_region_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalLandLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalLandLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_land_area_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalDepthArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalDepthArea < / StyleName >
# < StyleName > DryingHeight < / StyleName >
# < StyleName > DepthAreaText < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_depth_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalDepthContour"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalDepthContour < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_depth_contour_line < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalRiverLine"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalRiverLine < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_river_line < / Parameter >
# < / Datasource >
# < / Layer >
#
# < Layer
# name = "CoastalWreckPoint"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalWreckPoint < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_wreck_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalBuoy"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalBuoy < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_buoy_special_purpose_general_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalLandRegionText"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalLandRegionText < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_land_region_point < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "CoastalAnchorageArea"
# srs = "+proj=latlong +datum=WGS84"
# status = "on" >
# < StyleName > CoastalAnchorageArea < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > coastal_anchorage_area < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "temp"
# srs = "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs" >
# < StyleName > tempLandPoly < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > temp_within < / Parameter >
# < / Datasource >
# < / Layer >
# < Layer
# name = "grid"
# srs = "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs" >
# < StyleName > tempLandPoly < / StyleName >
# < Datasource >
# < Parameter
# name = "type" > postgis < / Parameter >
# < Parameter
# name = "dbname" > navinur_db < / Parameter >
# < Parameter
# name = "user" > postgres < / Parameter >
# < Parameter
# name = "password" > password1 < / Parameter >
# < Parameter
# name = "host" > localhost < / Parameter >
# < Parameter
# name = "table" > temp_partial < / Parameter >
# < / Datasource >
# < / Layer >
