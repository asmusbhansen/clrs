from clrs.data_structures.undirected_graph import UndirectedGraph

class ConnectedComponents:

    def __init__(self, graph : UndirectedGraph) -> None:

        self._count = 0
        self._marked = [False for n in range(graph.num_vertices)]
        self.id = [None for n in range(graph.num_vertices)]
        
        self.connected_components(graph=graph)

    def connected_components(self, graph : UndirectedGraph):
        
        for v in range(graph.num_vertices):

            if self._marked[v] == False:
                self.depth_first_search(graph=graph, vertex=v)
                self._count += 1

    def connected(self, v : int, w : int) -> bool:
        return self._id[v] == self._id[w]

    def depth_first_search(self, graph : UndirectedGraph, vertex : int) -> None:

        self._marked[vertex] = True

        adjacent = graph.adjacent(vertex)
        
        self.id[vertex] = self._count

        for adj_vertex in adjacent:

            if self._marked[adj_vertex] is False:

                self.depth_first_search(graph=graph, vertex=adj_vertex)


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

udg = UndirectedGraph(num_vertices=13, edges=edges_tiny_g)
udg.print_adjacent()

source_vertex = 0

cc = ConnectedComponents(graph=udg)

print(f'id: {cc.id}')