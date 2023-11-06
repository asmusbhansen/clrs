import random
import time
import matplotlib.pyplot as plt

from clrs.data_structures.directed_graph import DirectedGraph

class DirecteCycle:

    def __init__(self, graph : DirectedGraph):

        self._marked = [False for n in range(graph.num_vertices)]
        self._path_to = [None for n in range(graph.num_vertices)]
        self._on_stack = [False for n in range(graph.num_vertices)]
        self._cycle = None

        for n in range(graph.num_vertices):
            if self._marked[n] == False:
                self.search(graph=graph, vertex=n)

    def search(self, graph : DirectedGraph, vertex : int) -> None:

        self._marked[vertex] = True
        self._on_stack[vertex] = True

        adjacent = graph.adjacent(vertex)
       
        for adj_vertex in adjacent:

            print(f'Vertex: {vertex}, adj vertex: {adj_vertex}, adj vertex marked: {self._marked[adj_vertex]}, adj vertex on stack: {self._on_stack[adj_vertex]}')

            if self.has_cycle():
                return True

            elif self._marked[adj_vertex] is False:
                 
                self._path_to[adj_vertex] = vertex
                print(f'Set path_to - to {adj_vertex} from {vertex}')
                self.search(graph=graph, vertex=adj_vertex)

            elif self._on_stack[adj_vertex]:
                self._cycle = self.path_to(vertex, adj_vertex)

        self._on_stack[vertex] = False
            

    def has_cycle(self):
        return self._cycle != None

    def has_path_to(self, vertex : int) -> bool:
        return self._marked[vertex]

    def path_to(self, vertex : int, adj_vertex : int) -> list:

        if self.has_path_to(vertex=vertex) is False:
            return None

        path = []

        current_vertex = vertex

        while current_vertex != adj_vertex and self._path_to[current_vertex] != None:

            print(f'Path to - Search vertex: {vertex}, Current vertex: {current_vertex}')

            next_vertex = self._path_to[current_vertex]

            path = [next_vertex] + path 

            print(f"Path to - Next_vertex: {next_vertex}, path: {path}")

            current_vertex = next_vertex

        path = path + [vertex] 

        return path

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

ddfs = DirecteCycle(graph=digraph)

print(ddfs.has_cycle(), ddfs._cycle)