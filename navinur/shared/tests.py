from django.test import TestCase
from navinur.shared.models import PathGrid


# Create your tests here.

class PathGridTestCase(TestCase):
    def setUp(self):
        PathGrid.objects.create()

    def test_path_grid_valid(self):
        cell = PathGrid.objects.get(gid=1)
        self.assertEqual()