import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
import pyproj
from pyproj import Proj
django.setup()
from django.contrib.gis.db.models import Extent
from navinur.shared.models import PathGrid


class GridUtilities:

    def __init__(self):
        self.qs = PathGrid.objects.all()

    @staticmethod
    def start_end_points_to_cells(start_pt, end_pt):
        """
        Accepts lat/lon coordinates and returns the gid of the cells in the  grid which contain them
        :param start_pt: start coordinates
        :param end_pt: end coordinates
        :return: start and end cell gid
        """
        print("Start point is: {}".format(start_pt))
        print("End point is: {}".format(end_pt))
        # GeoDjango will convert the geometry of the point to the correct SRID of the table in the query expression
        start_cell = PathGrid.objects.get(geom__contains=start_pt)
        end_cell = PathGrid.objects.get(geom__contains=end_pt)
        return start_cell.gid, end_cell.gid

    def grid_contains_cell(self, cell):
        self.qs.aggregate(Extent('geom'))
        return PathGrid.objects.filter(geom__contains=cell.geom)

    def number_cells_in_grid(self):
        return list(self.qs).__len__()

    @staticmethod
    def find_cell_centre_projected(cell, query_string):
        polygon = query_string.get(pk=cell)
        centre_point = polygon.geom.centroid
        return centre_point

    @staticmethod
    def convert_to_latlon(p):
        utm16 = Proj(init='epsg:32616')
        geo = Proj(init='epsg:4326')
        lon, lat = pyproj.transform(utm16, geo, p[0], p[1])
        return lon, lat

    @staticmethod
    def convert_to_proj(p):
        utm16 = Proj(init='epsg:32616')
        geo = Proj(init='epsg:4326')
        lon, lat = pyproj.transform(geo, utm16, p[0], p[1])
        return lon, lat

    @staticmethod
    def find_cell_centre_coord(cell, query_string):
        polygon = query_string.get(pk=cell)
        centre_point = polygon.geom.centroid
        return GridUtilities.convert_to_latlon(centre_point)

    @staticmethod
    def cell_containing_point(pt):
        cell = PathGrid.objects.get(geom__contains=pt)
        return cell.geom


