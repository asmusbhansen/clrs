from clrs.data_structures.undirected_graph import UndirectedGraph


class BreadthFirstSearch:

    def __init__(self, graph : UndirectedGraph, source_vertex : int) -> None:

        self._count = 0
        self._marked = [False for n in range(graph.num_vertices)]
        self._edge_to = [None for n in range(graph.num_vertices)]
        self._source_vertex = source_vertex
        self.vertex_queue = []

        self.enqueue(vertex=None, adjacent_vertex=source_vertex)

        self.search(graph=graph)

    def enqueue(self, vertex : int, adjacent_vertex : int) -> None:

        if self._marked[adjacent_vertex] == False:
            self.vertex_queue += [adjacent_vertex]
            self._marked[adjacent_vertex] = True
            self._edge_to[adjacent_vertex] = vertex

            print(f'Enqueue: Marked = {self._marked}, Edge to = {self._edge_to}')

    def dequeue(self) -> int:

        vertex = self.vertex_queue[0]
        self.vertex_queue = self.vertex_queue[1:]
        return vertex 

    def search(self, graph : UndirectedGraph) -> None:

        while len(self.vertex_queue) > 0:

            vertex = self.dequeue()

            adjacent_vertices = graph.adjacent(vertex)

            for adjacent_vertex in adjacent_vertices:
            
                self.enqueue(vertex=vertex, adjacent_vertex=adjacent_vertex)

            
        
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

bfs = BreadthFirstSearch(graph=udg, source_vertex=source_vertex)