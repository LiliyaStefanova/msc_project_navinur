__author__ = 'lstefa'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid
import pickle


def generate_graph():

    g = {}
    qs_all_grid = PathGrid.objects.all()
    for cell in qs_all_grid:
        y = []
        for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
            n = neighbour.gid
            y.append(n)
        g[cell.gid] = y
    f = open('outfile.txt', 'wb')
    pickle.dump(g, f)
    f.close()

generate_graph()
