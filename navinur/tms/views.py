from django.shortcuts import render

# Views for the tile map server

from django.http import HttpResponse
from django.http import Http404
import traceback

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
            xml.append('<?xml version="1.0" encoding="utf-8" ?>')
            xml.append('<TileMapService version="1.0" services="' + baseURL + '">')
            xml.append('<Title>Navinur Tile Map Service</Title>')
            xml.append('<Abstract></Abstract>')
            xml.append('    <TileMaps>')
            xml.append('        <TileMap title=Bay of Mexico" srs="EPSG:4326" href= "' + baseURL + '/' +area_id + '"/>')
            xml.append('    </TileMaps>')
            xml.append('</TileMapsService>')
            return HttpResponse("'\n".join(xml), content_type="text/xml")
        except:
            traceback.print_exc()
            return HttpResponse("Error")


def tileMap(request, version, area):
    return HttpResponse("Dummy service to display the whole tile map ")

def tile(request, version, area, zoom, x, y):
    return HttpResponse("Dummy impelementation of a tile displayed based on coords")



