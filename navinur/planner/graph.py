__author__ = 'lstefa'


class Graph(object):
    def __init__(self, graph_dict=None):
        self.graph_dict = {} if graph_dict is None else graph_dict
        self.weights = {}

    # depth first implementation - does not work

    def cost(self, a, b):
        return self.weights.get(b, 1)

    def __unicode__(self):
        return self.name
