from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid, TestRoutes
from django.contrib.gis.geos import LineString, Point
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from navinur.planner import grid_utils, graph, bfs_path_finder, a_star_path_finder
import  navinur.tms
import pickle
import random
import traceback


# Create your views here.


def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"
    calc_route_url = "http://" + request.get_host() + "/planner/calc_route"
    return render(request, "main.html",
                  {'calc_route_url': calc_route_url,
                   'tms_url': tms_url})


def display_route(request, route_id):
    tms_url = "http://" + request.get_host() + "/tms/"
    display_route_url = "http://"+request.get_host()+"/planner/display_route/"+route_id
    return render(request, "main.html",
                  {'tms_url': tms_url}
                  )


def calc_route(request):
    try:
        start_lat = float(request.GET['start_lat'])
        start_lon = float(request.GET['start_lon'])
        end_lat = float(request.GET['end_lat'])
        end_lon = float(request.GET['end_lon'])
        start_pt = Point(start_lon, start_lat, srid=4326)
        end_pt = Point(end_lon, end_lat, srid=4326)
        start_node = grid_utils.start_end_points_to_cells(start_pt, end_pt)[0]
        end_node = grid_utils.start_end_points_to_cells(start_pt, end_pt)[1]
        # route_id = 1
        route_id = a_star_route(start_node, end_node)
        return HttpResponse("/planner/display_route/" + str(route_id))
    except:
        traceback.print_exc()
        return HttpResponse("")


def a_star_route(start, target):
    print ("Route start point: {}".format(start))
    print ("Route end point: {}".format(target))
    # TODO fix this path
    g = pickle.load(open('/home/lstefa/repos/project_navinur/navinur/planner/outfile.txt', 'rb'))
    gra = graph.Graph(g)
    print("Graph dictionary generated...")
    astar_finder = a_star_path_finder.AStarPathFinder()
    path = astar_finder.astar_path_find(start, target, gra.graph_dict)
    waypoints = []
    for item in path:
        cell = PathGrid.objects.get(pk=item)
        centre_point = cell.geom.centroid
        waypoints.append(centre_point)
    route_line = LineString(waypoints)
    route = TestRoutes(name='Test route No {}'.format(random.randint(1, 100000)), start=start, end=target,
                       distance=0, geom=route_line)
    route.save()
    return route.gid


def bfs_route(start, target):
    print ("Start point: {}".format(start))
    print ("End point: {}".format(target))
    g = pickle.load(open('outfile.txt', 'rb'))
    gra = graph.Graph(g)
    print("Graph generated...")
    bfs_path_finder.bfs(gra.graph_dict, start)
    route_cell_gids = bfs_path_finder.find_path_bfs(start, target, bfs_path_finder.parents)[::-1]
    print(route_cell_gids)
    waypoints = []
    for item in route_cell_gids:
        cell = PathGrid.objects.get(pk=item)
        centre_point = cell.geom.centroid
        waypoints.append(centre_point)
    route_line = LineString(waypoints)
    route = TestRoutes(name='Test route No' + str(random.random), start=start, end=target,
                       distance=0, geom=route_line)
    route.save()
