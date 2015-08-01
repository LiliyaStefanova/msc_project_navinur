import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from django.contrib.gis.geos import Point
from navinur.shared.models import PathGrid

# Create your views here.
def find_neighbours():
    start_pt = Point(-89.013977050782, 29.243133561686)
    start_cell = PathGrid.objects.filter(poly__contains=start_pt)
    print(start_cell)


find_neighbours()