class DirectedGraph:

    def __init__(self, num_vertices, edges):

        self._num_vertices = num_vertices
        self._num_edges = 0

        self._adjacent = [[] for n in range(self.num_vertices)]

        for n, edge in enumerate(edges):

            v = edge[0]
            w = edge[1]

            self.add_edge(v=v, w=w)

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def num_edges(self) -> int:
        return self._num_edges

    def add_edge(self, v : int, w : int) -> None:

        self.set_adjacent(v=v, w=w)

        self._num_edges += 1

    def adjacent(self, v) -> list:
        return self._adjacent[v]

    def set_adjacent(self, v : int, w : int) -> None:

        print(f'v = {v}, w = {w}, len _adjacent = {len(self._adjacent)}')

        self._adjacent[v] = [w] + self._adjacent[v]

    def print_adjacent(self):

        for a in self._adjacent:
            print(a)

    def reverse(self):

        digraph = DirectedGraph()


