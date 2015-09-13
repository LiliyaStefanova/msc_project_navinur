import os
import sys
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
from navinur.shared.models import PathGrid
import pickle
from django.conf import settings


class GraphSerializer(object):

    def __init__(self):
        self.cache_dir = settings.NAVINUR_GRAPH_CACHE_DIR
        self.outfile_location = os.path.join(self.cache_dir, 'outfile.txt')
        self.heuristic_location = os.path.join(self.cache_dir, 'heuristic_outfile.txt')
        self.weightfile_location = os.path.join(self.cache_dir, 'weights.txt')

    def write_outfile(self, graph):
        f = open(self.outfile_location, 'wb')
        pickle.dump(graph, f)
        f.close()

    def write_heuristic_outfile(self, graph):
        f = open(self.heuristic_location, 'wb')
        pickle.dump(graph, f)
        f.close()

    def write_weights_outfile(self, graph):
        f = open(self.weightfile_location, 'wb')
        pickle.dump(graph, f)
        f.close()


class GraphInitializer:

    PROHIBITED_WEIGHT = 10000000    # used for land, partial land and zero depth nodes
    REGULAR_WEIGHT = 1              # used for remaining water based nodes

    def __init__(self, serializer):
        """
        :type serializer: GraphSerializer
        """
        self.qs_all_grid = PathGrid.objects.all()
        self.serializer = serializer

    def generate_graph(self):
        g = {}
        for cell in self.qs_all_grid:
            y = []
            for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
                n = neighbour.gid
                y.append(n)
            g[cell.gid] = y
        self.serializer.write_outfile(g)

    def initialize_weights(self):
        weights = {}
        for cell in self.qs_all_grid:
            temp = []
            for neighbour in PathGrid.objects.filter(geom__touches=cell.geom):
                if neighbour.land_flag or neighbour.zero_depth_flag or neighbour.part_land_flag:
                    w = GraphInitializer.PROHIBITED_WEIGHT
                    temp.append((neighbour.gid, w))
                else:
                    w = GraphInitializer.REGULAR_WEIGHT
                    temp.append((neighbour.gid, w))
            weights[cell.gid] = temp
        self.serializer.write_weights_outfile(weights)


def main():
    initializer = GraphInitializer(GraphSerializer())
    initializer.generate_graph()
    initializer.initialize_weights()

if __name__ == '__main__':
    sys.exit(main())

