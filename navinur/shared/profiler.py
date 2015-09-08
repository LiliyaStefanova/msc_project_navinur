__author__ = 'lstefa'
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import pyproj
from navinur.planner import views
from django.contrib.gis.geos import Point
from navinur.planner.graph_initializer import GraphInitializer, GraphSerializer
from navinur.planner.grid_utils import GridUtilities
from navinur.shared.models import PathGrid
from navinur.planner import graph
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


start_pt = Point(-89.51, 28.95, srid=4326)
end_pt = Point(-88.99, 29.43, srid=4326)
serializer = GraphSerializer()
querystring = PathGrid.objects
utils = GridUtilities()
start_cell_id = 563371035
start_next_cell_id = 563371036
land_cell_id = 563371414
land_neighbour_cell_id = 563371415
end_cell_id = 563384794
start_route_point_id = 563378568
end_route_point_id = 563379106
graph = graph.Graph()
geod = pyproj.Geod(ellps="WGS84")
initializer = GraphInitializer(serializer)

with PyCallGraph(output=GraphvizOutput()):
    views.a_star_route(start_cell_id, end_cell_id)
    GraphInitializer.generate_graph(initializer)
