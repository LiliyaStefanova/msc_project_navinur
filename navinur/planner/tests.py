import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import unittest
from navinur.shared.models import PathGrid
from navinur.planner import graph, graph_initializer, grid_utils, queue, priority_queue, a_star_path_finder, views
from a_star_path_finder import AStarPathFinder
from graph_initializer import GraphInitializer, GraphSerializer
from grid_utils import GridUtilities
from django.contrib.gis.geos import Point, LineString
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
import pyproj


class GridUtilitiesTestCases(unittest.TestCase):
    def setUp(self):
        self.start_pt = Point(-89.51, 28.95, srid=4326)
        self.end_pt = Point(-88.99, 29.43, srid=4326)
        self.querystring = PathGrid.objects
        self.utils = GridUtilities()
        self.start_cell_id = 563371035
        self.end_cell_id = 563384794

    def test_start_end_points_to_cells(self):
        start_end_cells = GridUtilities.start_end_points_to_cells(self.start_pt, self.end_pt)
        self.assertEqual(start_end_cells[0], self.start_cell_id)
        self.assertEqual(start_end_cells[1], self.end_cell_id)
        self.assertTrue(type(start_end_cells[0]) is int)
        self.assertTrue(type(start_end_cells[1]) is int)

    def test_grid_contains_cell(self):
        geom = PathGrid.objects.get(pk=self.start_cell_id)
        self.assertTrue(GridUtilities.grid_contains_cell(self.utils, geom))

    def test_num_tests_in_grid(self):
        """
        validated against database query:
        select count(*)
        from path_grid
        :return: number of cells in grid
        """
        expected_number = 44453
        self.assertEqual(expected_number, GridUtilities.number_cells_in_grid(self.utils))

    def test_find_cell_centre_projected(self):
        """
        validated against the following query:
        SELECT ST_AsText(ST_Transform(ST_Centroid(geom), 32616))
        from path_grid p
        where p.gid = 563371035
        :return: test result
        the test point projected coordinates are POINT(255609 3205174)
        """
        expected_proj_lon = 255609
        point = GridUtilities.find_cell_centre_projected(self.start_cell_id, self.querystring)
        self.assertEqual(expected_proj_lon, point.coords[0])

    def test_convert_to_lat_lon(self):
        input_proj_coord = (255609, 3205174)
        expected_coords = (-89.50754515153298, 28.95124700010566)
        self.assertEqual(expected_coords, GridUtilities.convert_to_latlon(input_proj_coord))
        self.assertTrue(type(expected_coords[0]) is float)
        self.assertTrue(type(expected_coords[1]) is float)

    def test_find_cell_centre_coord(self):
        """
        Query used to generate database result:
        SELECT ST_AsText(ST_Transform(ST_Centroid(geom), 4326))
        from path_grid p
        where p.gid = 563371035
        tested against output from the database:
        "POINT(-89.507545151533 28.9512470001057)"
        :return:
        """
        expected_point = (-89.50754515153298, 28.95124700010566)
        self.assertEqual(expected_point, GridUtilities.find_cell_centre_coord(self.start_cell_id, self.querystring))
        self.assertTrue(type(expected_point[0]) is float)
        self.assertTrue(type(expected_point[1]) is float)


class GraphAlgorithmTestCases(TestCase):
    def setUp(self):
        self.start_pt = Point(-89.51, 28.95, srid=4326)
        self.end_pt = Point(-88.99, 29.43, srid=4326)
        self.serializer = GraphSerializer()
        self.querystring = PathGrid.objects
        self.utils = GridUtilities()
        self.start_cell_id = 563371035
        self.start_next_cell_id = 563371036
        self.land_cell_id = 563371414
        self.land_neighbour_cell_id = 563371415
        self.end_cell_id = 563384794
        self.start_route_point_id = 563378568
        self.end_route_point_id = 563379106
        self.graph = graph.Graph()
        self.geod = pyproj.Geod(ellps="WGS84")
        self.a_star_path_finder = AStarPathFinder(self.serializer)

    def test_heuristic(self):
        expected_distance = 1000
        actual_distance = AStarPathFinder.heuristic(self.a_star_path_finder, self.start_cell_id,
                                                    self.start_next_cell_id)
        self.assertEqual(expected_distance, round(actual_distance, 0))

    def test_cost(self):
        expected_cost_water = 1
        expected_cost_land = 10000000
        actual_cost_water = AStarPathFinder.cost(self.a_star_path_finder, self.start_cell_id, self.start_next_cell_id)
        actual_cost_land = AStarPathFinder.cost(self.a_star_path_finder, self.land_cell_id, self.land_neighbour_cell_id)
        self.assertEqual(expected_cost_water, actual_cost_water)
        self.assertEqual(expected_cost_land, actual_cost_land)

    def test_astar_generator(self):

        camefrom_cost_actual_tuple = AStarPathFinder.a_star_path_finder(self.a_star_path_finder,
                                                                        self.start_route_point_id,
                                                                        self.end_route_point_id,
                                                                        self.graph)
        self.assertIsNotNone(camefrom_cost_actual_tuple[0])
        self.assertIsNotNone(camefrom_cost_actual_tuple[1])

    def test_route_reconstructor(self):
        camefrom_cost_actual_tuple = AStarPathFinder.a_star_path_finder(self.a_star_path_finder,
                                                                        self.start_route_point_id,
                                                                        self.end_route_point_id,
                                                                        self.graph)
        self.assertIsNotNone(camefrom_cost_actual_tuple[0])


class HTTPRequestsTestCases(TestCase):

    def setUp(self):
        self.route_request = "GET /planner/calc_route?start_lat=28.948211669922&" \
                             "start_lon=-89.29183959961&end_lat=28.937225341797&end_lon=-89.214935302735 HTTP/1.1"
        self.display_route_request = "GET /planner/display_route/50 HTTP/1.1"
        self.get_site = "GET /planner/display_route/50 HTTP/1.1"
        self.display_map_request = "GET /tms/1.0/50/3/5/5.png HTTP/1.1"
        self.start_route_point_id = 563378568
        self.end_route_point_id = 563379106
        self.client = Client()

    def test_calc_route(self):

        self.assertEqual(200, views.calc_route(HttpRequest).status_code)

    def test_existing_routes(self):
        response = self.client.post('/planner/existing_routes')
        self.assertEqual(200, response.status_code)

    def a_star_route_test(self):
        route = views.a_star_route(self.start_route_point_id, self.end_route_point_id)
        self.assertTrue(isinstance(route, int))
        self.assertIsNotNone(PathGrid.objects.get(pk=route))

    def test_display_route(self):
        response = self.client.post('/planner/display_route/1')
        self.assertEqual(200, response.status_code)

    def test_display_map(self):
        response = self.client.post('/planner/index/0')
        self.assertEqual(200, response.status_code)


class GraphInitializerTestCase(TestCase):
    def setUp(self):
        pass

    def test_graph_init(self):
        pass

    def test_weight_init(self):
        pass


class DataStructuresTestCases(TestCase):
    def setUp(self):
        self.queue = queue.Queue()
        self.priority_queue = priority_queue.PriorityQueue()
        self.graph = graph.Graph()

    def test_queue_push_pop(self):
        self.queue.enqueue(1)
        self.assertEqual(1, self.queue.dequeue())

    def test_priority_queue(self):
        self.priority_queue.put(3, 10)
        self.priority_queue.put(4, 12)
        self.priority_queue.put(2, 6)
        self.assertEqual(2, self.priority_queue.pop())

    def test_graph_structure(self):

        self.assertTrue(self.graph.graph_dict.__sizeof__() != 0)
        self.assertTrue(self.graph.weights.__sizeof__() != 0)
