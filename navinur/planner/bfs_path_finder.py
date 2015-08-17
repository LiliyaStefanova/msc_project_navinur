__author__ = 'lstefa'
from navinur.shared.models import PathGrid
import queue

processed = {}
discovered = {}
parents = {}

for cell in PathGrid.objects.all():
    processed[cell.gid] = False
    discovered[cell.gid] = False
    parents[cell.gid] = -1


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

