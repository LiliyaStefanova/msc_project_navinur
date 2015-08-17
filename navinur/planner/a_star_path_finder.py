__author__ = 'lstefa'


class AStarPathFinder:

    closed_nodes = []
    open_nodes = []


    def astar_path_find(start, end, graph, direction):

        # add starting location to opening list and empty closed list
        open_nodes = [start]
        current = start
        visited ={}

        #while there are more possible next steps in the open list and we have not found the target
        # while open_nodes.__len__()!=0 or current == end:
            #select more likely next step based on heuristic and path cost
            #remove from the open list and add to closed
            # consider each neighbour of the steps
            #for each neighour, calculate path cost in reaching the neighbour
            #if the cost if less than hte cost known for this location then remove it from the open and closed lists, this is now a better route
            #if the location is not in open or closed record the costs and add it to the open list.
            #record how location was reached


    def get_cost(graph, start, end):
        return None

