__author__ = 'lstefa'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django

django.setup()
from django.contrib.gis.db.models import Extent
from django.contrib.gis.geos import Point
from navinur.shared.models import PathGrid

qs = PathGrid.objects.all()


def start_and_end_points():
    start_pt = Point(-89.028, 29.087, srid=4326)
    end_pt = Point(-89.005, 29.077, srid=4326)
    start_cell = PathGrid.objects.get(geom__contains=start_pt)
    end_cell = PathGrid.objects.get(geom__contains=end_pt)
    return start_cell.gid, end_cell.gid


def grid_contains_cell(cell):
    qs.aggregate(Extent('geom'))
    if PathGrid.objects.filter(geom__contains=cell.geom):
        return True
    else:
        return False


def number_cells_in_grid():
    return list(qs).__len__()
