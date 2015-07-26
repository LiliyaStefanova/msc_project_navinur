from django.shortcuts import render
from django.contrib.gis.geos import Point
from navinur.shared.models import PathGrid

# Create your views here.
def find_neighbours():
    start_pt = Point(-89.417724609375, 28.919036881998)
    start_cell = PathGrid.objects.filter(poly__contains=start_pt)
    print(start_cell)


find_neighbours()