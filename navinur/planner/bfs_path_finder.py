from navinur.shared.models import PathGrid
from navinur.planner.data_structures import queue

"""
Alternative routing implementation using Breadth First Search
Included for completeness
"""


class BFSPathFinder(object):

    def __init__(self):

        self.processed = {}
        self.discovered = {}
        self.parents = {}
        for cell in PathGrid.objects.all():
            self.processed[cell.gid] = False
            self.discovered[cell.gid] = False
            self.parents[cell.gid] = -1

    def bfs(self, graph, start):
        q = queue.Queue()

        q.enqueue(start)
        self.discovered[start] = True

        while not q.isempty():
            v = q.dequeue()
            # process_vertex_early(v)
            self.processed[v] = True
            y = graph[v]
            for item in y:
                if not self.discovered[item]:
                    q.enqueue(item)
                    self.discovered[item] = True
                    self.parents[item] = v

    def find_path_bfs(self, start, end, ps, path=[]):
        """
        reconstructs the path following a traversal
        """
        path = [] if path is None else path
        if start == end:
            path = path + [start]
            return path
        else:
            path = path + [end] + self.find_path_bfs(start, self.parents[end], self.parents)
            return path




