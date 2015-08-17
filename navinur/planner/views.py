from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid
from navinur.shared.models import TestRoutes
from django.contrib.gis.geos import LineString
import pickle
import random
from navinur.planner import grid_utils, graph, bfs_path_finder, a_star_path_finder


# Create your views here.


def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"

    return render(request, "main.html",
                  {'tms_url': tms_url})


def get_route(request):

    tms_url = "http://"+request.get_host()+ "/tms/"
    get_route_url = "http://" + request.get_host() + "/planner/get_route"
    return render(request, "main.html",
                  {'get_route_url': get_route_url,
                   'tms_url': tms_url})


start_point = grid_utils.start_and_end_points()[0]
end_point = grid_utils.start_and_end_points()[1]
print ("Start point: {}", start_point)
print ("End point: {}", end_point)
g = pickle.load(open('outfile.txt', 'rb'))
gra = graph.Graph(g)
print("Graph generated...")
bfs_path_finder.bfs(gra.graph_dict, grid_utils.start_and_end_points()[0])
route_cell_gids = bfs_path_finder.find_path_bfs(start_point, end_point, bfs_path_finder.parents)[::-1]
print(route_cell_gids)
waypoints = []
for item in route_cell_gids:
    cell = PathGrid.objects.get(pk=item)
    centre_point = cell.geom.centroid
    waypoints.append(centre_point)
route_line = LineString(waypoints)
route = TestRoutes(name='Test route No' + str(random.random), start=start_point, end=end_point, distance=0,
                   geom=route_line)
route.save()
print(route_line)
print waypoints

