import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from django.contrib.gis.db.models import Extent, Union
from django.contrib.gis.geos import Point, GEOSGeometry
from navinur.shared.models import PathGrid
from navinur.shared.models import GeneralLandArea
from navinur.shared.models import CoastalDepthArea
from navinur.shared.models import GeneralDepthArea
from navinur.shared.models import CoastalCoverageArea

# Create your views here.


def start_and_end_points():
    start_pt = Point(-89.028, 29.087, srid=4326)
    end_pt = Point(-89.005, 29.077, srid=4326)
    start_cell = PathGrid.objects.get(geom__contains=start_pt)
    end_cell = PathGrid.objects.get(geom__contains=end_pt)
    return start_cell, end_cell


def grid_contains_cell(cell):
    qs = PathGrid.objects.all().aggregate(Extent('geom'))
    if PathGrid.objects.filter(geom__contains=cell.geom):
        return True
    else:
        return False


def find_path(start_vertex, end_vertex, path=[]):
    """
     Finding a path from start vertex to end vertex in the graph
    :param start_vertex:
    :param end_vertex:
    :param path:
    :return: extended path
    """
    print(start_vertex.geom)
    path = path + [start_vertex]
    if start_vertex.gid == end_vertex.gid:
        return path
    if not grid_contains_cell(start_vertex):
        return None
    neighbours = PathGrid.objects.filter(geom__touches=start_vertex.geom)
    for vertex in neighbours:
        if vertex not in path:
            extended_path = find_path(vertex,
                                      end_vertex,
                                      path)
            if extended_path:
                return extended_path

    return None

start = start_and_end_points()[0]
end = start_and_end_points()[1]
path = []
print(grid_contains_cell(start))
ext_path = find_path(start, end, path)
for entry in ext_path:
    print(entry.geom)
#
# def find_neighbours():
#     start_pt = Point(-89.563, 28.796, srid=4326)
#     end_pt = Point(-89.464, 28.788, srid=4326)
#     end = GEOSGeometry('POINT(-89.464 28.788)', srid=4326)
#     start_cell = PathGrid.objects.get(geom__contains=start_pt).geom
#     end_cell = PathGrid.objects.get(geom__contains=end_pt).geom
#     print("Neighbours: ")
#     neighbours = PathGrid.objects.filter(geom__touches=start_cell)
#     for n in neighbours:
#         print(n.geom)
#
#     print("Start cell is:")
#     print(start_cell)
#     print("End cell is: ")
#     print(end_cell)

