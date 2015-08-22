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


def service(request, version):
    # creation of a service xml file which will be accessed by Openlayers
    try:
        if version != "1.0":
            raise Http404
        base_url = request.build_absolute_uri()
        area_id = "1"
        xml = []
        xml.append('<?xml version = "1.0" encoding = "utf-8" ?>')
        xml.append('<TileMapService version="1.0" services="' + base_url + '">')
        xml.append('<Title> Navinur Tile Map Service</Title>')
        xml.append('<Abstract></Abstract>')
        xml.append('    <TileMaps>')
        xml.append('        <TileMap title= "Bay of Mexico" srs="EPSG:4326" href= "' + base_url + '/'
                   + area_id + '"/>')
        xml.append('    </TileMaps>')
        xml.append('</TileMapService>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def tile_map(request, version, area_id):
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


def tile(request, version, area_id, zoom, x, y):
    try:
        # check parameters are specified correctly
        if version != "1.0" or area_id != "1":
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

