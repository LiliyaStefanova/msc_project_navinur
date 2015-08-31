from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid, TestRoutes
from django.contrib.gis.geos import LineString, Point
from django.http import HttpResponse
from navinur.planner import grid_utils, graph, bfs_path_finder, a_star_path_finder
import pyproj
import pickle
import random
import traceback


# Create your views here.


def display_map(request, route_id):
    tms_url = "http://" + request.get_host() + "/tms/"
    calc_route_url = "http://" + request.get_host() + "/planner/calc_route"
    return render(request, "main.html",
                  {'route_id': route_id,
                   'calc_route_url': calc_route_url,
                   'tms_url': tms_url})


def display_route(request, route_id):
    tms_url = "http://" + request.get_host() + "/tms/"
    return render(request, "main.html",
                  {'route_id': route_id,
                   'tms_url': tms_url}
                  )


def calc_route(request):
    try:
        start_lat = float(request.GET['start_lat'])
        start_lon = float(request.GET['start_lon'])
        end_lat = float(request.GET['end_lat'])
        end_lon = float(request.GET['end_lon'])
        start_pt = Point(start_lon, start_lat, srid=4326)
        end_pt = Point(end_lon, end_lat, srid=4326)
        start_end = grid_utils.GridUtilities.start_end_points_to_cells(start_pt, end_pt)
        start_node = start_end[0]
        end_node = start_end[1]
        route_id = a_star_route(start_node, end_node)
        return HttpResponse("/planner/display_route/" + str(route_id))
    except:
        traceback.print_exc()
        return HttpResponse("")


def existing_routes(request):
    routes = TestRoutes.objects.all().order_by("gid")
    return render(request, "existing_routes.html",
                  {'routes': routes})


def a_star_route(start, target):
    print ("Route start point: {}".format(start))
    print ("Route end point: {}".format(target))
    # TODO fix this path
    g = pickle.load(open('/home/lstefa/repos/project_navinur/navinur/planner/outfile.txt', 'rb'))
    # g = pickle.load(open('./outfile.txt', 'rb'))
    gra = graph.Graph(g)
    print("Graph dictionary generated...")
    astar_finder = a_star_path_finder.AStarPathFinder()
    path = astar_finder.reconstruct_path(astar_finder.a_star_path_finder(start, target, gra.graph_dict)[0],
                                         start, target)
    waypoints = []
    for item in path:
        cell = PathGrid.objects.get(pk=item)
        centre_point = cell.geom.centroid
        waypoints.append(centre_point)
    route_line = LineString(waypoints, srid=32616)
    geod = pyproj.Geod(ellps="WGS84")
    # qs = PathGrid.objects.all()
    # tlon, tlat = grid_utils.find_cell_centre_coords(target, qs)
    # clon, clat = grid_utils.find_cell_centre_coords(current, qs)
    # distance = geod.inv(clon, clat, tlon, tlat)[2]
    route = TestRoutes(name='Route No {}'.format(random.randint(1, 100000)), start=start, end=target,
                       distance=0, geom=route_line)
    route.save()
    return route.gid


def bfs_route(start, target):
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


