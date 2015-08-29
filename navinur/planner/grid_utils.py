__author__ = 'lstefa'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
import pyproj
from pyproj import Proj
from django.contrib.gis.geos import Point
import traceback

django.setup()
from django.contrib.gis.db.models import Extent
from navinur.shared.models import PathGrid

qs = PathGrid.objects.all()


def start_end_points_to_cells(start_pt, end_pt):
    # start_pt = Point(-89.51, 28.95, srid=4326)
    # end_pt = Point(-88.99, 29.43, srid=4326)
    # GeoDjango will convert the geometry of the point to the correct SRID of table being looked up
    print("Start point is: {}".format(start_pt))
    print("End point is: {}".format(end_pt))
    start_cell = PathGrid.objects.get(geom__contains=start_pt)
    print(start_cell.gid)
    end_cell = PathGrid.objects.get(geom__contains=end_pt)
    print(end_cell.gid)
    return start_cell.gid, end_cell.gid


def grid_contains_cell(cell):
    qs.aggregate(Extent('geom'))
    if PathGrid.objects.filter(geom__contains=cell.geom):
        return True
    else:
        return False


def number_cells_in_grid():
    return list(qs).__len__()


def find_cell_centre_projected(cell, query_string):
    polygon = query_string.get(pk=cell)
    centre_point = polygon.geom.centroid
    return centre_point


def find_cell_centre_coords(cell, query_string):
    polygon = query_string.get(pk=cell)
    centre_point = polygon.geom.centroid
    return convert_to_latlon(centre_point)


def convert_to_latlon(p):
    utm16 = Proj(init='epsg:32616')
    unproj = Proj(init='epsg:4326')
    lon, lat = pyproj.transform(utm16, unproj, p.x, p.y)
    return lon, lat


def cell_containing_point(pt):
    cell = PathGrid.objects.get(geom__contains=pt)
    return cell.geom
