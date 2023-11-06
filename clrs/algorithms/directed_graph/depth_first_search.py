import random
import time
import matplotlib.pyplot as plt

from clrs.data_structures.directed_graph import DirectedGraph

class DirectedDepthFirstSearch:

    def __init__(self, graph : DirectedGraph, source_vertex : int):

        self._count = 0
        self._marked = [False for n in range(graph.num_vertices)]
        self._source_vertex = source_vertex

        self.search(graph=graph, vertex=source_vertex)

    def search(self, graph : DirectedGraph, vertex : int) -> None:

        self._marked[vertex] = True

        adjacent = graph.adjacent(vertex)
        
        self._count += 1

        for adj_vertex in adjacent:

            if self._marked[adj_vertex] is False:

                self.search(graph=graph, vertex=adj_vertex)


edges_tiny_dg =  [[4,2],
 [2, 3],
 [3, 2],
 [6, 0],
 [0, 1],
 [2, 0],
[11, 12],
[12, 9],
 [9, 10],
 [9, 11],
 [8, 9],
[10, 12],
[11, 4],
 [4, 3],
 [3, 5],
 [7, 8],
 [8, 7],
 [5, 4],
 [0, 5],
 [6, 4],
 [6, 9],
 [7, 6]]

digraph = DirectedGraph(num_vertices=13, edges=edges_tiny_dg)
print(digraph._adjacent)

ddfs = DirectedDepthFirstSearch(graph=digraph, source_vertex=6)

for m, marked in enumerate(ddfs._marked):
    if marked is True:
        print(f'{m} is reachable from {ddfs._source_vertex}')