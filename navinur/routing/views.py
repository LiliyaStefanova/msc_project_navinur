import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid
from navinur.shared.models import TestRoutes
from django.contrib.gis.geos import LineString
import pickle
from navinur.planner import queue, grid_utils


# Create your views here.


class Graph(object):

    def __init__(self, graph_dict=None):
        self.graph_dict = {} if graph_dict is None else graph_dict

    # depth first implementation - does not work
    def find_path(self, start_vertex, end_vertex, path=None):
        path = [] if path is None else path
        # print("Current vertex is: {}".format(start_vertex))
        # print("Path contains: {}".format(path))
        graph = self.graph_dict
        path = path + [start_vertex]
        # print("Path after adding current start vertex contains: {}".format(path))
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        # print("Neighbours of current vertex are: {} ".format(graph[start_vertex]))
        for vertex in graph[start_vertex]:
            if vertex not in path:
                # if vertex == end_vertex:
                #     path = path + [vertex]
                #     return path
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    # print("Extended path contains: {}".format(extended_path))
                    return extended_path
        return None

    def __unicode__(self):
        return self.name

# if __name__ == "__main__":

processed = [False] * (grid_utils.number_cells_in_grid()+1)
discovered = [False] * (grid_utils.number_cells_in_grid()+1)
parents = [-1] * (grid_utils.number_cells_in_grid()+1)


def bfs(graph, start):
    q = queue.Queue()

    q.enqueue(start)
    discovered[start] = True

    while not q.isempty():
        v = q.dequeue()
        # process_vertex_early(v)
        processed[v] = True
        y = graph[v]
        for item in y:
            if not processed[item]:
                process_edge(v, item)
            if not discovered[item]:
                q.enqueue(item)
                discovered[item] = True
                parents[item] = v
        process_vertex_late(v)


def process_vertex_late(v):
    return None


def process_vertex_early(v):
    return None


def process_edge(x, y):
    return None


def find_path_bfs(start, end, ps, path=[]):
    path = [] if path is None else path
    if start == end:
        path = path + [start]
        return path
    else:
        path = path + [end] + find_path_bfs(start, parents[end], parents)
        return path


"""alternative implementation """


def iterative_bfs(graph, start, path=[]):
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = q + graph[v]
        return path

start_point = grid_utils.start_and_end_points()[0]
end_point = grid_utils.start_and_end_points()[1]
print ("Start point: {}", start_point)
print ("End point: {}", end_point)
g = pickle.load(open('outfile.txt', 'rb'))
gra = Graph(g)
print("Graph generated...")
bfs(gra.graph_dict, grid_utils.start_and_end_points()[0])
route_cell_gids = find_path_bfs(start_point, end_point, parents)[::-1]
print(route_cell_gids)
waypoints = []
for item in route_cell_gids:
    cell = PathGrid.objects.get(pk=item)
    centre_point = cell.geom.centroid
    waypoints.append(centre_point)
route_line = LineString(waypoints)
route = TestRoutes(name='Test BFS', start=start_point, end=end_point, distance=0, geom=route_line)
route.save()
print(route_line)
# p = iterative_bfs(gra.graph_dict, grid_utils.start_and_end_points()[0])
# print(find_path_bfs(start_point, end_point, p))
print waypoints

