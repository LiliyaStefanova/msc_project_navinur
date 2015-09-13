import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import pyproj
import heapq
from navinur.shared.models import PathGrid
import grid_utils
import pickle
from navinur.planner.data_structures import priority_queue


class AStarPathFinder:

    def __init__(self, serializer):
        """
        :type serializer: navinur.planner.graph_initializer.GraphSerializer
        """
        self.qs = PathGrid.objects.all()
        self.serializer = serializer
        self.weights = pickle.load(open(serializer.weightfile_location))

    def heuristic(self, current, target):
        """
        Generates a heuristic for determining the priority of the current node based on the
        great cicle distance between it and the target node
        :param current: the current node in the graph
        :param target:  the target node of the route
        :return: great circle distance
        """
        geod = pyproj.Geod(ellps="WGS84")
        tlon, tlat = grid_utils.GridUtilities.find_cell_centre_coord(target, self.qs)
        clon, clat = grid_utils.GridUtilities.find_cell_centre_coord(current, self.qs)
        return geod.inv(clon, clat, tlon, tlat)[2]

    def cost(self, a, b):
        """
        Retrieves the weight of an edge between two nodes from the weights dictionary
        :param a: the first node of the edge
        :param b: the second node of the edge
        :return: the weight between them
        """
        for n in self.weights[a]:
            if n[0] == b:
                return n[1]

    def find_path(self, start, target, graph):
        """
        A* path finding implementation between two points based on a spatial geometry grid where
        each cell is a node in the graph
        :param start: start cell
        :param target: end cell
        :param graph: the graph traversed to find the path
        :return: a list of nodes part of the path in reverse order
        """
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

            for n in graph[current]:
                new_cost = cost_so_far[current] + self.cost(current, n)
                if n not in cost_so_far or new_cost < cost_so_far[n]:
                    cost_so_far[n] = new_cost
                    priority = new_cost + self.heuristic(target, n)
                    frontier.put(n, priority)
                    came_from[n] = current

        return came_from, cost_so_far

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        """
        Takes a list of nodes which track the parents of each node on the path between two nodes
        :param came_from: list of all parent nodes in reverse order
        :param start: start point of path
        :param goal: end point of path
        :return: path which can be used in correct order
        """
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


class AStarPathFinderAlternative(object):
        """
        Alternative A* implementation which leads to zigzagging and looping
        paths
        Not displayed via GUI but included for completeness
        """

        def __init__(self, serializer):
            """
           :type serializer: navinur.planner.graph_initializer.GraphSerializer
           """
            self.qs = PathGrid.objects.all()
            self.serializer = serializer
            self.weights = serializer.weightfile_location
            print("Weights initialized...")

        @staticmethod
        def initialize_parents(self, graph):
            parents = {}
            for node in graph:
                parents[node] = -1
            return parents

        @staticmethod
        def initialize_heuristic(self, graph):
            h = {}
            for node in graph:
                h[node] = 0
            return h

        def heuristic(self, current, target):
            geod = pyproj.Geod(ellps="WGS84")
            tlon, tlat = grid_utils.GridUtilities.find_cell_centre_coord(target, self.qs)
            clon, clat = grid_utils.GridUtilities.find_cell_centre_coord(current, self.qs)
            return geod.inv(clon, clat, tlon, tlat)[2]

        def astar_alternative_impl(self, current, target, graph):
            h = self.initialize_heuristic(self, graph)

            parents = self.initialize_parents(self, graph)
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

