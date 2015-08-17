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
    start_pt = Point(-89.51, 28.95, srid=4326)
    end_pt = Point(-88.99, 29.43, srid=4326)
    # GeoDjango will c onvert the geometry of the point to the correct SRID of table being looked up
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


def cell_containing_point(pt):
    cell = PathGrid.objects.get(geom__contains=pt)
    return cell.geom

# point = Point(-89.398498535157, 29.285705583171, srid=4326)
# c = cell_containing_point(point)
print(number_cells_in_grid())
