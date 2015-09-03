import unittest
from navinur.shared.models import PathGrid
from navinur.planner import graph, graph_initializer
from django.contrib.gis.geos import Point, LineString

from django.test import TestCase

class RoutePlannerTestCases(TestCase):

    def setUp(self):

        self.start_pt = Point(-89.51, 28.95, srid=4326)
        self.end_pt = Point(-88.99, 29.43, srid=4326)
        self.graph = graph.Graph
        self.graph = graph_initializer.GraphInitializer.generate_graph()
        self.weights = graph_initializer.GraphInitializer.initialize_weights()


    #TODO how to test http request and response
  #  display_map_test(self):


   # display_route_test(self):

   #calculate_route_test(self):



