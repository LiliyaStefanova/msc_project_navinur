from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
import django
django.setup()
from navinur.shared.models import PathGrid
from navinur.shared.models import TestRoutes
from django.contrib.gis.geos import LineString
import pickle
from navinur.planner import queue, grid_utils, graph


# Create your views here.


def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"

    return render(request, "main.html",
                  {'tms_url': tms_url})


def get_route(request):

    tms_url = "http://"+request.get_host()+ "/tms/"
    get_route_url = "http://" + request.get_host() + "/planner/get_route"
    return render(request, "main.html",
                  {'get_route_url': get_route_url,
                   'tms_url': tms_url})


processed = [False] * (grid_utils.number_cells_in_grid() + 1)
discovered = [False] * (grid_utils.number_cells_in_grid() + 1)
parents = [-1] * (grid_utils.number_cells_in_grid() + 1)


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
gra = graph.Graph(g)
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

