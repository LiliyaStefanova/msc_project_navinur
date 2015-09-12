import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
from django.test import TestCase
from navinur.shared.models import PathGrid
from navinur.shared.models import TestRoutes
from django.contrib.gis.geos import LineString
import random


# Create your tests here.

class PathGridTestCase(TestCase):
    def setUp(self):
        PathGrid.objects.create()


class RouteTestCases(TestCase):

    def setUp(self):
        self.start_cell_id = 563371035
        self.end_cell_id = 563384794

    def test_get_route(self):
        route = TestRoutes.objects.get(gid=1)
        self.assertEqual("Test BFS", route.name)

    def test_new_route(self):
        line = LineString((0, 0), (0, 50), (50, 50), (50, 0), srid=32616)
        line_4326 = LineString((0, 0), (0, 50), (50, 50), (50, 0), srid=4326)
        route = TestRoutes(name='Route No {}'.format(random.randint(1, 100000)),
                           start=self.start_cell_id,
                           end=self.end_cell_id,
                           distance=0, geom=line,
                           geom_4326=line_4326)
        route.save()
        self.assertEqual(0, TestRoutes.objects.get(start=self.start_cell_id).distance)
