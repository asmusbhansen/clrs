from clrs.data_structures.edge_weighted_graph import EdgeWeightedGraph
from clrs.data_structures.edge import Edge

import queue
import heapq as hq

ewg = EdgeWeightedGraph(graph_filename='data/graph_files/tinyEWG.txt')

class PrimsAlgorithm:

    def __init__(self, edge_weighted_graph : EdgeWeightedGraph):

        self.edge_weighted_graph = edge_weighted_graph

        self.marked = [False for vertice in range(edge_weighted_graph.num_vertices)]

        self.edges_on_tree = []#[None for vertice in range(edge_weighted_graph.num_vertices)]#queue.Queue()

        self.crossing_edges = []

    def compute(self):

        self.visit(self.edge_weighted_graph, 0)

        while len(self.crossing_edges) > 0:
            print(f'Next iteration. PQ: {[edge.to_string() for edge in sorted(self.crossing_edges)]}')
            
            min_edge = hq.heappop(self.crossing_edges)

            v = min_edge.either()
            w = min_edge.other(v)

            if self.marked[v] == False or self.marked[w] == False:
                print(f'Put edge {min_edge.to_string()} on MST')
                #self.edges_on_tree[v] = min_edge
                self.edges_on_tree += [min_edge]

            if self.marked[v] == False:
                self.visit(self.edge_weighted_graph, v)
                
            if self.marked[w] == False:
                self.visit(self.edge_weighted_graph, w)


    def visit(self, edge_weighted_graph : EdgeWeightedGraph, vertex : int):

        self.marked[vertex] = True

        for edge_adjacent in edge_weighted_graph.get_adjacent(vertex):

            if self.marked[edge_adjacent.other(vertex)] == False:
                #print(f'Adding edge: {edge_adjacent.to_string()} to heap')
                hq.heappush(self.crossing_edges, edge_adjacent)


pa = PrimsAlgorithm(edge_weighted_graph=ewg)
pa.compute()
print([edge.to_string() for edge in pa.edges_on_tree])
