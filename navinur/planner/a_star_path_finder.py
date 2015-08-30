__author__ = 'lstefa'

import pyproj
import heapq
from navinur.shared.models import PathGrid
import grid_utils
import priority_queue
import pickle


class AStarPathFinder:

    def __init__(self):
        self.qs = PathGrid.objects.all()
        self.weights = pickle.load(open('/home/lstefa/repos/project_navinur/navinur/planner/weights.txt', 'rb'))
        print("Weights initialized...")

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

    def heuristic(self, current, target):
        geod = pyproj.Geod(ellps="WGS84")
        tlon, tlat = grid_utils.find_cell_centre_coords(target, self.qs)
        clon, clat = grid_utils.find_cell_centre_coords(current, self.qs)
        return geod.inv(clon, clat, tlon, tlat)[2]

    def cost(self, a, b):
        for n in self.weights[a]:
            if n[0] == b:
                return n[1]

    def a_star_path_finder(self, start, target, graph):
        frontier = priority_queue.PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        while not frontier.empty():
            current = frontier.pop()
            if current == target:
                break

            for next in graph[current]:
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(target, current)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def astar_alternative_impl(self, current, target, graph):
        h = self.initialize_heuristic(self, graph)
        parents = self.initialize_parents(self, graph)
        tlon, tlat = grid_utils.find_cell_centre_coords(target, self.qs)
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
                        h[cell] = 1000000 + self.heuristic(current, target)
                    else:
                        h[cell] = self.heuristic(current, target)
                    if cell not in open_nodes:
                        open_nodes.add(cell)
                        heapq.heappush(open_heap, (h[cell], cell))
                    parents[cell] = current
        return []




