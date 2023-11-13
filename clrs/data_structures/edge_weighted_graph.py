from clrs.data_structures.edge import Edge, DirectedEdge
from clrs.data_structures.graph_reader import GraphReader

    
class EdgeWeightedGraph:
    
    def __init__(self, graph_filename):

        num_vertices, num_edges, edges = GraphReader(edge_type=Edge).read(filename=graph_filename)

        self._num_vertices = num_vertices
        self._num_edges = num_edges

        self._adjacent = [[] for n in range(self.num_vertices)]

        for edge in edges:
            self.add_edge(edge)

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def num_edges(self) -> int:
        return self._num_edges

    def add_edge(self, e : Edge) -> None:

        v = e.either()
        w = e.other(v)
        
        print(f'Add edge: {e.to_string()}')

        self._adjacent[v] = [e] + self._adjacent[v]
        self._adjacent[w] = [e] + self._adjacent[w]

    def get_adjacent(self, v):
        return self._adjacent[v]

    def print_adjacent(self):

        for a in self._adjacent:
            print([e.to_string() for e in a])


#e1 = Edge(v=1, w=2, weight=0.1)
#e2 = Edge(v=4, w=2, weight=0.2)

#print(e1 == e2, e1 > e2, e1 < e2)

#ewg = EdgeWeightedGraph(graph_filename='data/graph_files/tinyEWG.txt')

#ewg.add_edge(e1)
#ewg.add_edge(e2)

#ewg.print_adjacent()


class EdgeWeightedDigraph:
    
    def __init__(self, graph_filename):

        num_vertices, num_edges, edges = GraphReader(edge_type=DirectedEdge).read(filename=graph_filename)

        self._num_vertices = num_vertices
        self._num_edges = num_edges

        self._adjacent = [[] for n in range(self.num_vertices)]

        for edge in edges:
            self.add_edge(edge)

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def num_edges(self) -> int:
        return self._num_edges

    def add_edge(self, e : DirectedEdge) -> None:

        v = e.vfrom()
        self._adjacent[v] = [e] + self._adjacent[v]

    def get_adjacent(self, v):
        return self._adjacent[v]
    
    def get_edges(self):

        edges = []

        for a in self._adjacent:
            edges += [e for e in a]

        return edges


    def to_string(self):

        str_out = ''

        for a in self._adjacent:
            str_out += '. '.join([e.to_string() for e in a]) + '\n'
        
        return str_out



ewdg = EdgeWeightedDigraph(graph_filename='data/graph_files/tinyEWD.txt')

#ewg.add_edge(e1)
#ewg.add_edge(e2)

print(ewdg.to_string())
