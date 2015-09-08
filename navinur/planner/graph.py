__author__ = 'lstefa'


class Graph(object):
    def __init__(self, graph_dict=None):
        self.graph_dict = {} if graph_dict is None else graph_dict
        self.weights = {}

    def __unicode__(self):
        return self.graph_dict
