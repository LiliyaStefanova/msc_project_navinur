__author__ = 'lstefa'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
from navinur.shared.models import PathGrid
import pickle


class GraphInitializer:

    def __init__(self):
        self.qs_all_grid = PathGrid.objects.all()

    def generate_graph(self):
        g = {}
        for cell in self.qs_all_grid:
            y = []
            for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
                n = neighbour.gid
                y.append(n)
            g[cell.gid] = y
        f = open('outfile.txt', 'wb')
        pickle.dump(g, f)
        f.close()

    def generate_heurstic_graph(self):
        g = {}
        h = 0
        for cell in self.qs_all_grid:
            y = []
            for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
                n = neighbour.gid
                y.append(n)
            g[(cell.gid, h)] = y

        f = open('heuristic_outfile.txt', 'wb')
        pickle.dump(g, f)
        f.close()

    def initialize_weights(self):
        weights = {}
        for cell in self.qs_all_grid:
            temp = []
            for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
                if neighbour.land_flag or neighbour.zero_depth_flag or neighbour.part_land_flag:
                    w = 10000000
                    temp.append((neighbour.gid, w))
                else:
                    w = 1
                    temp.append((neighbour.gid, w))
            weights[cell.gid] = temp
        for value in weights.itervalues():
            print(value == 10000000)
        f = open('weights.txt', 'wb')
        pickle.dump(weights, f)
        f.close()


initializer = GraphInitializer()
initializer.generate_graph()
initializer.initialize_weights()
