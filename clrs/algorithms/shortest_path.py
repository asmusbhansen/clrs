from clrs.data_structures.edge_weighted_graph import EdgeWeightedDigraph
from clrs.data_structures.edge import DirectedEdge
from clrs.data_structures.binary_heap import MinIndexBinaryHeap

import numpy as np
import heapq as hq

class ShortestPath:

    def __init__(self, edge_weighted_graph : EdgeWeightedDigraph, source : int):
        self.edge_weighted_graph = edge_weighted_graph
        self.source = source

        self._edge_to = [None for vertex in range(self.edge_weighted_graph.num_vertices)]
        self._dist_to = [np.inf for vertex in range(self.edge_weighted_graph.num_vertices)]
        self._dist_to[source] = 0
        self.is_elegible = [True for edge in self.edge_weighted_graph.get_edges()]

        self.compute()
    
    def compute(self):

        while any(self.is_elegible):

            for n, edge in enumerate(self.edge_weighted_graph.get_edges()):

                self.is_elegible[n] = self.relax_edge(edge)
                print(self.is_elegible)

    def has_path_to(self, vertex : int):

        return self._dist_to[vertex] < np.inf

    def dist_to(self, vertex : int):

        return self._dist_to[vertex]
    
    def path_to(self, vertex : int):

        if self.has_path_to(vertex=vertex) == False:
            return None

        path = []

        edge = self._edge_to[vertex]

        while isinstance(edge, DirectedEdge):
            path.append(edge)
            edge = self._edge_to[edge.vfrom()]

        return path

    def relax(self, vertex : int):

        edges_adjacent = self.edge_weighted_graph.get_adjacent(vertex)

        for edge_adjacent in edges_adjacent:
            self.relax_edge(edge_adjacent)

    def relax_edge(self, edge : DirectedEdge):

        v = edge.vfrom()
        w = edge.vto()

        if self._dist_to[w] > self._dist_to[v] + edge.weight():
            self._dist_to[w] = self._dist_to[v] + edge.weight()
            self._edge_to[w] = edge
            return True
        
        else:
            return False
        
     
class DjikstrasShortestPath(ShortestPath):

    
    def __init__(self, edge_weighted_graph : EdgeWeightedDigraph, source : int):
        self.edge_weighted_graph = edge_weighted_graph
        self.source = source

        self._edge_priority_queue = MinIndexBinaryHeap(max_size=self.edge_weighted_graph.num_vertices)

        self._edge_to = [None for vertex in range(self.edge_weighted_graph.num_vertices)]

        self._dist_to = [np.inf for vertex in range(self.edge_weighted_graph.num_vertices)]
        self._dist_to[source] = 0

        self.compute()

    def compute(self):

        self.visit(self.source)

        while self._edge_priority_queue.size > 0: 

            top_key, top_index = self._edge_priority_queue.extract_top()

            self.visit(top_index)

    def visit(self, vertex : int):

        for edge_adjacent in self.edge_weighted_graph.get_adjacent(vertex):

            # If the edge is eligeble
            if self.relax_edge(edge_adjacent):
                print(f'Adding edge {edge_adjacent.to_string()} to priority Queue')

                w = edge_adjacent.vto()
                
                self._edge_priority_queue.upsert(index=w, key=self.dist_to(w))


ewdg = EdgeWeightedDigraph(graph_filename='data/graph_files/tinyEWD.txt')

#sp = ShortestPath(ewdg, 0)

sp = DjikstrasShortestPath(ewdg, 0)

print([edge.to_string() + f' dist_to = {dist}' for edge, dist in zip(sp._edge_to,sp._dist_to) if isinstance(edge, DirectedEdge)])

for i in range(ewdg.num_vertices):
    print(f'{sp.source}->{i}', [edge.to_string() for edge in sp.path_to(i)])