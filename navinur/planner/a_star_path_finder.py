__author__ = 'lstefa'

import shapely
import heapq
from navinur.shared.models import PathGrid


class AStarPathFinder:

    closed_nodes = []
    open_nodes = []
    visited = {}
    qs = PathGrid.objects.all()

    def __init__(self):
        None

    def astar_path_find(current, end, graph):

        open_nodes = set()
        closed_nodes = set()
        open_heap = []
        # add starting location to opening list and empty closed list

        # uses appending and reversing for faster traversing through the path
        def find_path(c):
            path = [c]
            while c.parent is not None:
                c = c.parent
                path.append(c)
            path.reverse()
            return path

        open_nodes.add(current)
        open_heap.append((0, current))
        while open_nodes:
            current = heapq.heappop(open_heap)[1]
            if current == end:
                return find_path(current)
            open_nodes.remove(current)
            closed_nodes.add(current)
            for cell in graph[current]:
                if cell not in closed_nodes:
                    # assign heuristics value to cell
                    if cell not in open_nodes:
                        open_nodes.add(cell)
                        heapq.heappush(open_heap, (cell.h, cell))
        return []


    def get_cost(graph, current, end):
        distance = current.distance(end)
        return distance


