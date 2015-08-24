__author__ = 'lstefa'

import pyproj
import heapq
from navinur.shared.models import PathGrid
import grid_utils


class AStarPathFinder:

    def __init__(self):
        self.qs = PathGrid.objects.all()

    @staticmethod
    def initialize_heuristic(self, graph):
        h = {}
        for node in graph:
            h[node] = 0
        return h

    @staticmethod
    def initialize_parents(self, graph):
        parents = {}
        for node in graph:
            parents[node] = -1
        return parents

    def astar_path_find(self, current, target, graph):
        h = self.initialize_heuristic(self, graph)
        parents = self.initialize_parents(self, graph)
        geod = pyproj.Geod(ellps="WGS84")
        # open and closed lists implemented as sets for better performance
        open_nodes = set()
        closed_nodes = set()
        # heapq priority queue structure included in order to efficiently provide the minimum next heuristic value
        open_heap = []

        # uses appending and reversing for faster traversing through the path
        def find_path(c):
            path = [c]
            while parents[c] is not -1:
                c = parents[c]
                path.append(c)
            path.reverse()
            return path

        open_nodes.add(current)
        open_heap.append((0, current))
        while open_nodes:
            current = heapq.heappop(open_heap)[1]
            if current == target:
                return find_path(current)
            open_nodes.remove(current)
            closed_nodes.add(current)
            for cell in graph[current]:
                if cell not in closed_nodes:
                    db_entry = PathGrid.objects.get(pk=cell)
                    if db_entry.land_flag or db_entry.zero_depth_flag or db_entry.part_land_flag:
                        h[cell] = 1000000
                    else:
                        clon, clat = grid_utils.find_cell_centre_coords(current, self.qs)
                        tlon, tlat = grid_utils.find_cell_centre_coords(target, self.qs)
                        h[cell] = geod.inv(clon, clat, tlon, tlat)[2]
                    if cell not in open_nodes:
                        open_nodes.add(cell)
                        heapq.heappush(open_heap, (h[cell], cell))
                    parents[cell] = current
        return []

