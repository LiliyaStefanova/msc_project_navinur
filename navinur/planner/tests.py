import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import unittest
from navinur.shared.models import PathGrid
from navinur.planner import graph, graph_initializer, grid_utils
from grid_utils import GridUtilities
from django.contrib.gis.geos import Point, LineString
from django.test import TestCase


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

    # def test_grid_contains_cell(self):
    #     cell = 563371035
    #     self.assertTrue(GridUtilities.grid_contains_cell(self.utils, cell))

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


class GraphAlgorithmTestCases(TestCase):

    def setUp(self):
        self.start_pt = Point(-89.51, 28.95, srid=4326)
        self.end_pt = Point(-88.99, 29.43, srid=4326)
        self.graph = graph.Graph(self)