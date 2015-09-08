
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import unittest
from django.http import HttpRequest, HttpResponse
import views


class TMSTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_tms_root(self):
        expected_tms_url = "http://127.0.0.1:8000/tms/1.0"

    def test_tms_tilemapservice(self):
        pass

    def test_tms_tilemap(self):
        pass

    def tms_tile(self):

        tile = views.tile(HttpRequest, 1.0, "1", 5, 5, 6)
        self.assertEqual(200, tile.status_code)



