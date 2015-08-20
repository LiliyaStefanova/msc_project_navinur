from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid
from navinur.shared.models import TestRoutes
from django.contrib.gis.geos import LineString, Point
import pickle
import random
from navinur.planner import grid_utils, graph, bfs_path_finder
import a_star_path_finder


# Create your views here.


def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"
    calc_route_url = "http://" + request.get_host() + "/planner/calc_route"
    return render(request, "main.html",
                  {'calc_route_url': calc_route_url,
                   'tms_url': tms_url})


def calc_route(request):
    start_lat = float(request.GET['start_lat'])
    start_lon = float(request.GET['start_lon'])
    end_lat = float(request.GET['end_lat'])
    end_lon = float(request.GET['end_lon'])
    start_pt = Point(start_lon, start_lat, srid=4326)
    end_pt = Point(end_lat, end_lon, srid=4326)
    print(start_pt)
    print(end_pt)
    start_point = grid_utils.start_and_end_points()[0]
    end_point = grid_utils.start_and_end_points()[1]
    print ("Start point: {}".format(start_point))
    print ("End point: {}".format(end_point))
    g = pickle.load(open('outfile.txt', 'rb'))
    gra = graph.Graph(g)
    print("Graph generated...")
    # bfs_path_finder.bfs(gra.graph_dict, grid_utils.start_and_end_points()[0])
    # route_cell_gids = bfs_path_finder.find_path_bfs(start_point, end_point, bfs_path_finder.parents)[::-1]
    # print(route_cell_gids)
    # waypoints = []
    # for item in route_cell_gids:
    #     cell = PathGrid.objects.get(pk=item)
    #     centre_point = cell.geom.centroid
    #     waypoints.append(centre_point)
    # route_line = LineString(waypoints)
    # route = TestRoutes(name='Test route No' + str(random.random), start=start_point, end=end_point,
    #  distance=0,geom=route_line)
    # route.save()
    astar_finder = a_star_path_finder.AStarPathFinder()
    path = astar_finder.astar_path_find(grid_utils.start_and_end_points()[0], grid_utils.start_and_end_points()[1], gra.graph_dict)
    waypoints = []
    for item in path:
        cell = PathGrid.objects.get(pk=item)
        centre_point = cell.geom.centroid
        waypoints.append(centre_point)
    route_line = LineString(waypoints)
    route = TestRoutes(name='Test route No {}'.format(random.randint(1, 100000)), start=start_point, end=end_point,
    distance=0, geom=route_line)
    route.save()
