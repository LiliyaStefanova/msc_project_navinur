# Views for the tile map server

from django.http import HttpResponse
from django.http import Http404
import traceback
from navinur.shared.models import PathGrid
from navinur import settings
from navinur.planner.grid_utils import GridUtilities
import math
import mapnik
import shapely
import os

from pkg_resources import resource_filename

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")

TILE_WIDTH = 256
TILE_HEIGHT = 256
# overview, general, coastal
MAX_ZOOM_LEVEL = 11
cache_dir = settings.NAVINUR_GRAPH_CACHE_DIR
mapfile_location = os.path.join(cache_dir, 'map_file.xml')


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


# creation of a service xml file which will be accessed by Openlayers
def service(request, version, route_id):
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

        mapfile = resource_filename(__name__, 'style/map_file.xml')
        initialize_static_layers(map)
        route_layer = mapnik.Layer("Route", "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        start_icon_layer = mapnik.Layer("RouteIcons", "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        end_icon_layer = mapnik.Layer("RouteIcons", "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

        if route_id != "0":

            layers = _initialize_dynamic_layers(route_layer, start_icon_layer, end_icon_layer, route_id)
            route_layer = layers[0]
            start_icon_layer = layers[1]
            end_icon_layer = layers[2]

            route_layer.styles.append("Route")
            route_layer.styles.append("RouteDirection")
            start_icon_layer.styles.append("RouteIcons")
            end_icon_layer.styles.append("RouteIcons")

        map.layers.append(route_layer)
        map.layers.append(start_icon_layer)
        map.layers.append(end_icon_layer)

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


def _initialize_dynamic_layers(route_layer, start_icon_layer, end_icon_layer, route_id):
    """
    Initializes dynamic map layers associated with a route display
    :param route_layer:
    :param start_icon_layer:
    :param end_icon_layer:
    :param route_id:
    :return: a tuple containing the route and start and end icon layers initialized with data sources
    """

    route_query = "(select * from test_routes where gid=" + route_id + ") as route"
    route_params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost',
                        table=route_query, geometry_field='geom')
    route_data_source = mapnik.PostGIS(**route_params)
    route_layer.datasource = route_data_source

    icon_query = "(select start_geom, end_geom from test_routes where gid=" + route_id + ") as points"
    start_icon_params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost',
                             table=icon_query,geometry_field='start_geom')
    end_icon_params = dict(dbname='navinur_db', user='postgres', password='password1', host='localhost',
                           table=icon_query, geometry_field='end_geom')
    start_icon_data_source = mapnik.PostGIS(**start_icon_params)
    end_icon_data_source = mapnik.PostGIS(**end_icon_params)
    start_icon_layer.datasource = start_icon_data_source
    end_icon_layer.datasource = end_icon_data_source
    return route_layer, start_icon_layer, end_icon_layer


def initialize_static_layers(map):
    """
    Initializes the static map layers which do not change
    :param map:
    :return: nothing; just loads layers and appends them to the maps already
    """
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

    overview_depth_area = mapnik.Layer("OverviewDepthArea")
    params = common_params
    params['table'] = 'overview_depth_area'
    data_source = mapnik.PostGIS(**params)
    overview_depth_area.datasource = data_source
    overview_depth_area.styles.append("OverviewdDepthArea")
    overview_depth_area.styles.append("DryingHeight")
    map.layers.append(overview_depth_area)

    overview_coastline_layer = mapnik.Layer("OverviewCoastline")
    params = common_params
    params['table'] = 'overview_coastline_line'
    data_source = mapnik.PostGIS(**params)
    overview_coastline_layer.datasource = data_source
    overview_coastline_layer.styles.append("OverviewCoastline")
    map.layers.append(overview_coastline_layer)

    overview_depthcontour_layer = mapnik.Layer("OverviewDepthContour")
    params = common_params
    params['table'] = 'overview_depth_contour_line'
    data_source = mapnik.PostGIS(**params)
    overview_depthcontour_layer.datasource = data_source
    overview_depthcontour_layer.styles.append("OverviewDepthContour")
    map.layers.append(overview_depthcontour_layer)

    general_land_area_layer = mapnik.Layer("GeneralLandArea")
    params = common_params
    params['table'] = 'general_land_area'
    data_source = mapnik.PostGIS(**params)
    general_land_area_layer.datasource = data_source
    general_land_area_layer.styles.append("GeneralLandArea")
    map.layers.append(general_land_area_layer)

    general_depth_area_layer = mapnik.Layer("GeneralDepthArea")
    params = common_params
    params['table'] = 'general_depth_area'
    data_source = mapnik.PostGIS(**params)
    general_depth_area_layer.datasource = data_source
    general_depth_area_layer.styles.append("GeneralDepthArea")
    general_depth_area_layer.styles.append("DryingHeight")
    general_depth_area_layer.styles.append("DepthAreaText")
    map.layers.append(general_depth_area_layer)

    general_coast_line_layer = mapnik.Layer("GeneralCoastLine")
    params = common_params
    params['table'] = 'general_coastline_line'
    data_source = mapnik.PostGIS(**params)
    general_coast_line_layer.datasource = data_source
    general_coast_line_layer.styles.append("GeneralCoastline")
    map.layers.append(general_coast_line_layer)

    general_depthcontour_layer = mapnik.Layer("GeneralDepthContour")
    params = common_params
    params['table'] = 'general_depth_contour_line'
    data_source = mapnik.PostGIS(**params)
    general_depthcontour_layer.datasource = data_source
    general_depthcontour_layer.styles.append("GeneralDepthContour")
    map.layers.append(general_depthcontour_layer)

    coastal_land_line_layer = mapnik.Layer("CoastalLandLine")
    params = common_params
    params['table'] = 'coastal_land_area_line'
    data_source = mapnik.PostGIS(**params)
    coastal_land_line_layer.datasource = data_source
    coastal_land_line_layer.styles.append("CoastalLandLine")
    map.layers.append(coastal_land_line_layer)

    coastal_depth_area_layer = mapnik.Layer("CoastalDepthArea")
    params = common_params
    query = "(select * from coastal_depth_area where drval1 > 0.0) as depth_area"
    params['table'] = query
    data_source = mapnik.PostGIS(**params)
    coastal_depth_area_layer.datasource = data_source
    coastal_depth_area_layer.styles.append("CoastalDepthArea")
    coastal_depth_area_layer.styles.append("DepthAreaText")
    map.layers.append(coastal_depth_area_layer)

    coastal_depth_area_drying_layer = mapnik.Layer("CoastalDepthArea")
    params = common_params
    dry_query = "(select * from coastal_depth_area where drval1 < 0.0 and dsnm!='US3GC03M.000') as depth_area_drying"
    params['table'] = dry_query
    data_source = mapnik.PostGIS(**params)
    coastal_depth_area_drying_layer.datasource = data_source
    coastal_depth_area_drying_layer.styles.append("DepthAreaText")
    coastal_depth_area_drying_layer.styles.append("DryingHeight")
    map.layers.append(coastal_depth_area_drying_layer)

    coastal_depth_contour_layer = mapnik.Layer("CoastalDepthContour")
    params = common_params
    params['table'] = 'coastal_depth_contour_line'
    data_source = mapnik.PostGIS(**params)
    coastal_depth_contour_layer.datasource = data_source
    coastal_depth_contour_layer.styles.append("CoastalDepthContour")
    map.layers.append(coastal_depth_contour_layer)

    overview_river_line_layer = mapnik.Layer("OverviewRiverLine")
    params = common_params
    params['table'] = 'overview_river_line'
    data_source = mapnik.PostGIS(**params)
    overview_river_line_layer.datasource = data_source
    overview_river_line_layer.styles.append("OverviewRiverLine")
    map.layers.append(overview_river_line_layer)

    general_river_line_layer = mapnik.Layer("GeneralRiverLine")
    params = common_params
    params['table'] = 'general_river_line'
    data_source = mapnik.PostGIS(**params)
    general_river_line_layer.datasource = data_source
    general_river_line_layer.styles.append("GeneralRiverLine")
    map.layers.append(general_river_line_layer)

    coastal_river_line_layer = mapnik.Layer("CoastalRiverLine")
    params = common_params
    params['table'] = 'coastal_river_line'
    data_source = mapnik.PostGIS(**params)
    coastal_river_line_layer.datasource = data_source
    coastal_river_line_layer.styles.append("CoastalRiverLine")
    map.layers.append(coastal_river_line_layer)

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

    coastal_anchorage_layer = mapnik.Layer("CoastalAnchorageArea")
    params = common_params
    params['table'] = 'coastal_anchorage_area'
    data_source = mapnik.PostGIS(**params)
    coastal_anchorage_layer.datasource = data_source
    coastal_anchorage_layer.styles.append("CoastalAnchorageArea")
    map.layers.append(coastal_anchorage_layer)

    general_land_region_layer = mapnik.Layer("GeneralLandRegion")
    params = common_params
    params['table'] = 'general_land_region_point'
    data_source = mapnik.PostGIS(**params)
    general_land_region_layer.datasource = data_source
    general_land_region_layer.styles.append("GeneralLandRegionText")
    map.layers.append(general_land_region_layer)

    general_coverage_area_layer = mapnik.Layer("GeneralCoverageArea")
    params = common_params
    params['table'] = 'general_coverage_area'
    data_source = mapnik.PostGIS(**params)
    general_coverage_area_layer.datasource = data_source
    general_coverage_area_layer.styles.append("GeneralCoverageArea")
    # general_coverage_area_layer.styles.append("CoastalCoverageAreaTitle")
    map.layers.append(general_coverage_area_layer)

    coastal_land_region_layer = mapnik.Layer("CoastalLandRegionText")
    params = common_params
    params['table'] = 'coastal_land_region_point'
    data_source = mapnik.PostGIS(**params)
    coastal_land_region_layer.datasource = data_source
    coastal_land_region_layer.styles.append("CoastalLandRegionText")
    map.layers.append(coastal_land_region_layer)

    coastal_coverage_area_layer = mapnik.Layer("CoastalCoverageArea")
    params = common_params
    params['table'] = 'coastal_coverage_area'
    data_source = mapnik.PostGIS(**params)
    coastal_coverage_area_layer.datasource = data_source
    coastal_coverage_area_layer.styles.append("CoastalCoverageArea")
    coastal_coverage_area_layer.styles.append("CoastalCoverageAreaTitle")
    map.layers.append(coastal_coverage_area_layer)

    # path_grid_layer = mapnik.Layer("PathGrid", "+proj=utm +zone=16 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
    # params = common_params
    # params['table'] = 'path_grid'
    # data_source = mapnik.PostGIS(**params)
    # path_grid_layer.datasource = data_source
    # path_grid_layer.styles.append("grid")
    # map.layers.append(path_grid_layer)
