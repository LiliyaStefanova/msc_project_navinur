from django.shortcuts import render

# Views for the tile map server

from django.http import HttpResponse

def root(request):
    return HttpResponse("Dummy tile map server implementation for testing")

def service(request, version):
    return HttpResponse("Dummy tile map service implementation for testing ")

def tileMap(request, version, area):
    return HttpResponse("Dummy service to display the whole tile map ")

def tile(request, version, area, zoom, x, y):
    return HttpResponse("Dummy impelementation of a tile displayed based on coords")



