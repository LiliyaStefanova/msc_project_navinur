import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from django.shortcuts import render
from navinur.shared.models import PathGrid, TestRoutes
from django.contrib.gis.geos import LineString, Point
from django.http import HttpResponse
from navinur.planner import grid_utils, graph, a_star_path_finder
from bfs_path_finder import BFSPathFinder
from grid_utils import GridUtilities
from graph_initializer import GraphSerializer
import pickle
import random
import traceback


# Views used to interact with web pages live here

def display_map(request, route_id):
    """
    Displays the main map or the map with a route on depending on the route id passed from the request
    Route id = 0 is equivalent to a map with no route
    """
    tms_url = "http://" + request.get_host() + "/tms/"
    calc_route_url = "http://" + request.get_host() + "/planner/calc_route"
    return render(request, "main.html",
                  {'route_id': route_id,
                   'calc_route_url': calc_route_url,
                   'tms_url': tms_url})


def display_route(request, route_id):
    """
    Handles the requests to display the route once it has been calculated
    this method is called by calc_route once finished
    """
    tms_url = "http://" + request.get_host() + "/tms/"
    return render(request, "main.html",
                  {'route_id': route_id,
                   'tms_url': tms_url}
                  )

_ROUTE_FACTORY = None


def calc_route(request):
    """
    Calculates the route and passes it to the display_route view for display in the GUI
    """
    global _ROUTE_FACTORY

    try:
        start_lat = float(request.GET['start_lat'])
        start_lon = float(request.GET['start_lon'])
        end_lat = float(request.GET['end_lat'])
        end_lon = float(request.GET['end_lon'])
        start_pt = Point(start_lon, start_lat, srid=4326)
        end_pt = Point(end_lon, end_lat, srid=4326)
        _ROUTE_FACTORY = _ROUTE_FACTORY or AStarFactory()
        route_id = _ROUTE_FACTORY.create_route(start_pt, end_pt)

        return HttpResponse("/planner/display_route/" + str(route_id))

    except:
        traceback.print_exc()
        return HttpResponse("")


def existing_routes(request):
    """
    Returns a page with existing routes
    """
    routes = TestRoutes.objects.all().order_by("gid")
    return render(request, "existing_routes.html",
                  {'routes': routes})


class AStarFactory(object):
    """
    Factory object used to create AStarFinder objects which give access to the graph and weights structures
    Used to prevent creation of a new object instance each time through the use of global variable
    however this is not best practice and should be refactored in future
    """

    def __init__(self):
        self.serializer = GraphSerializer()
        self.g = pickle.load(open(self.serializer.outfile_location))
        self.gra = graph.Graph(self.g)
        self.path_finder = a_star_path_finder.AStarPathFinder(self.serializer)
        self.qs = PathGrid.objects.all()

    def create_route(self, start_pt, target_pt):
        """
        Based on points passed through a HTTP request a route is calculated, geometry generated on the basis of it
        and persisted to the database.
        :param start_pt: the start point specified
        :param target_pt: the end point specified
        :return: the id of the generated and persisted route geometry back to the page which requested it
        """
        start_end = grid_utils.GridUtilities.start_end_points_to_cells(start_pt, target_pt)
        start_node = start_end[0]
        end_node = start_end[1]
        reverse_path = self.path_finder.find_path(start_node, end_node, self.gra.graph_dict)
        path = self.path_finder.rebuild_path(reverse_path[0], start_node, end_node)
        route_geoms = _generate_route_geom(path)
        start_pt_record = GridUtilities.find_cell_centre_projected(start_node, self.qs)
        end_pt_record = GridUtilities.find_cell_centre_projected(end_node, self.qs)
        route = TestRoutes(name='Route No {}'.format(random.randint(1, 100000)),
                           distance=round(route_geoms[0].length/1852, 2),
                           geom=route_geoms[0],
                           geom_4326=route_geoms[1],
                           start_geom=start_pt_record,
                           end_geom=end_pt_record)
        route.save()
        return route.gid


def _generate_route_geom(path):
    """
    Helper method which looks after the conversion of a list of geometry ids to a line
    which can be persisted in the database and displayed on screen
    :param path:
    :return: a linestring geometry representing the route calculated
    """
    waypoints_proj = []
    waypoints_geo = []
    for item in path:
        cell = PathGrid.objects.get(pk=item)
        centre_point_geo = GridUtilities.convert_to_latlon(cell.geom.centroid)
        centre_point_proj = cell.geom.centroid
        waypoints_proj.append(centre_point_proj)
        waypoints_geo.append(centre_point_geo)
    route_line_proj = LineString(waypoints_proj, srid=32616)
    route_line_geom = LineString(waypoints_geo, srid=4326)
    return route_line_proj, route_line_geom


def bfs_route(start, target):
    """
    Included for completeness but not available through the GUI
    :param start:
    :param target:
    :return:
    """
    bfs_finder = BFSPathFinder()
    g = pickle.load(open('outfile.txt', 'rb'))
    gra = graph.Graph(g)
    print("Graph generated...")
    BFSPathFinder.find_path_bfs(gra.graph_dict, start)
    route_cell_gids = BFSPathFinder.find_path_bfs(start, target, bfs_finder.parents[::-1])
    print(route_cell_gids)
    waypoints = []
    for item in route_cell_gids:
        cell = PathGrid.objects.get(pk=item)
        centre_point = cell.geom.centroid
        waypoints.append(centre_point)
    route_line = LineString(waypoints)
    route = TestRoutes(name='Test route No' + str(random.random), start=start, end=target,
                       distance=route_line.length, geom=route_line)
    route.save()
    return route.gid


