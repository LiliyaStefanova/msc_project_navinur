from django.shortcuts import render

# Views for the tile map server

from django.http import HttpResponse
from django.http import Http404
import traceback
import math

TILE_WIDTH = 256
TILE_HEIGHT = 256
MAX_ZOOM_LEVEL = 4

def root(request):
    try:
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding="utf-8" ?>')
        xml.append('<Services>')
        xml.append('    <TileMapService ' +
                   'title = "Navinur tile map service" ' +
                   'version = "1.0" href=" ' + baseURL + '1.0" />')
        xml.append('</Services>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def service(request, version):
        #creation of a service xml file which will be accessed by Openlayers
        try:
            if version != "1.0":
                raise Http404
            baseURL = request.build_absolute_uri()
            area_id = "1"
            xml = []
            xml.append('<?xml version = "1.0" encoding = "utf-8" ?>')
            xml.append('<TileMapService version="1.0" services="' + baseURL + '">')
            xml.append('<Title> Navinur Tile Map Service</Title>')
            xml.append('<Abstract></Abstract>')
            xml.append('    <TileMaps>')
            xml.append('        <TileMap title= "Bay of Mexico" srs="EPSG:4326" href= "' + baseURL + '/'
                       + area_id + '"/>')
            xml.append('    </TileMaps>')
            xml.append('</TileMapService>')
            return HttpResponse("\n".join(xml), content_type="text/xml")
        except:
            traceback.print_exc()
            return HttpResponse("Error")


def tileMap(request, version, area_id):
    if version !="1.0":
        raise Http404
    try:
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding = "utf-8" ?>')
        xml.append('<TileMap version ="1.0" tilemapservice = "' + baseURL + '">')
        xml.append('    <Title>Bay of Mexico</Title>')
        xml.append('    <Abstract></Abstract>')
        xml.append('    <SRS>EPSG:4326</SRS>')
        xml.append('    <BoundingBox minx="" miny="" maxx="" maxy="" />')
        xml.append('    <Origin x = " " y = " " />')
        xml.append('    TileFormat width="'+str(TILE_WIDTH) + '" height="' + str(TILE_HEIGHT) + '"'
                   + ' mime-type="image/png" extension="png"/>')
        xml.append('    <TileSets profile="global-geodetic">')
        for zoomLevel in range(0, MAX_ZOOM_LEVEL +1):
            units_per_pixel = _unitsPerPixel(zoomLevel)
            xml.append('    <TileSet href = "' + baseURL + '/' + str(zoomLevel) + '" units-per-pixel ="' + str(units_per_pixel) +
                       '" order = "' + str(zoomLevel) + '"/>')
        xml.append('    </TileSets>')
        xml.append('</TileMap>')
        return HttpResponse("\n".join(xml), content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")


def tile(request, version, area, zoom, x, y):
    return HttpResponse("Dummy impelementation of a tile displayed based on coords")


# underscore denotes private functions in python
def _unitsPerPixel(zoomLevel):
    return 0.702125 / math.pow(2, zoomLevel)