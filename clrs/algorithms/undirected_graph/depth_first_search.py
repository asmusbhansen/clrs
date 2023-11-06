import random
import time
import matplotlib.pyplot as plt

from clrs.data_structures.undirected_graph import UndirectedGraph

class DepthFirstSearch:

    def __init__(self, graph : UndirectedGraph, source_vertex : int):

        self._count = 0
        self._marked = [False for n in range(graph.num_vertices)]
        self._path_to = [None for n in range(graph.num_vertices)]
        self._source_vertex = source_vertex

        self.search(graph=graph, vertex=source_vertex)

    def search(self, graph : UndirectedGraph, vertex : int) -> None:

        self._marked[vertex] = True

        adjacent = graph.adjacent(vertex)
        
        self._count += 1

        #print(f'Vertex {vertex}, adjacency: {adjacent}')

        for adj_vertex in adjacent:

            #print(f'Vertex: {vertex}, Adjacency vertex: {adj_vertex}, adjacency vertex marked: {self._marked[adj_vertex]}')

            if self._marked[adj_vertex] is False:
                self._path_to[adj_vertex] = vertex
                #print(f'Set path_to - to {adj_vertex} from {vertex}')
                self.search(graph=graph, vertex=adj_vertex)

    def has_path_to(self, vertex : int) -> bool:
        return self._marked[vertex]

    def path_to(self, vertex : int) -> list:

        if self.has_path_to(vertex=vertex) is False:
            return None

        path = []

        current_vertex = vertex

        while current_vertex != self._source_vertex:
            next_vertex = self._path_to[current_vertex]

            #print(f'Source vertex: {self._source_vertex}, Search vertex: {vertex}, Current vertex: {current_vertex}, next_vertex: {next_vertex}, path: {path}')

            path = [next_vertex] + path 

            current_vertex = next_vertex

        path = path + [vertex] 

        return path

    @property
    def count(self):
        return self._count

edges_tiny_g = [[0,5], 
         [4,3],
         [0,1],
         [9,12],
         [6,4],
         [5,4],
         [0,2],
         [11,12],
         [9,10],
         [0,6],
         [7,8],
         [9,11],
         [5,3]
         ]

edges_tiny_g = [[0,5],
                [2,4],
                [2,3],
                [1,2],
                [0,1],
                [3,4],
                [3,5],
                [0,2]
                ]

udg = UndirectedGraph(num_vertices=6, edges=edges_tiny_g)
udg.print_adjacent()

source_vertex = 0
destination_vertex = 5

dfs = DepthFirstSearch(graph=udg, source_vertex=source_vertex)

print(f'Connected to source vertex {source_vertex}: {dfs.count}')

path = dfs.path_to(vertex=destination_vertex)

print(f'Path from vertex {source_vertex} to {destination_vertex}: {path}')


num_tests = 100
max_vertices = 200
edge_proportion = 10
results_search = []
results_path = []
num_vertices_results = []

for n in range(num_tests):
    print(f'Test {n+1} of {num_tests}')
    num_vertices = random.randint(1,max_vertices) + 1
    num_edges = int(num_vertices * edge_proportion)

    #print(f'num_vertices: {num_vertices}, num_edges: {num_edges}')

    edges = [[] for n in range(num_edges)]

    for n in range(num_edges):
        v = random.randint(0,num_vertices-1)
        w = random.randint(0,num_vertices-1)
        edges[n] = [v, w]

   

    udg = UndirectedGraph(num_vertices=num_vertices, edges=edges)

    
    time_search_aggr = 0
    time_path_aggr = 0
    for vertex in range(num_vertices):
        t0 = time.time()
        dfs = DepthFirstSearch(graph=udg, source_vertex=vertex)
        time_search_aggr += time.time() - t0

        t0 = time.time()
        dfs.path_to(vertex=random.randint(0,num_vertices-1))
        time_path_aggr += time.time() - t0

   

    results_search += [time_search_aggr / num_vertices]
    results_path += [time_path_aggr / num_vertices]
    num_vertices_results += [num_vertices]



plt.figure()
plt.scatter(num_vertices_results, results_search, alpha=1, label='Depth First Search Time')
plt.scatter(num_vertices_results, results_path, alpha=1, label='Depth First Path Time')
plt.title(f'Simulation output: Egde proportion = {edge_proportion}')
plt.xlabel('Number of Vertices')
plt.ylabel('Time [s]')
plt.legend()
plt.savefig('simulation_output/undirected_graph/dfs.png')

plt.close()
'''
'''