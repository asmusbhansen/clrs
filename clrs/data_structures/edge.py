import functools

@functools.total_ordering
class Edge:

    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight
    
    def either(self):
        return self._v
    
    def other(self, vertex):
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise ValueError(f'Vertex {vertex}, is none of v = {self._v} or w = {self._w}')
        
    def compare_to(self, other):

        if self < other:
            return -1
        elif self > other:
            return 1
        else:
            return 0
        
    def to_string(self):
        return f"{self._v}-{self._w}, {self._weight}"
    
    def __eq__(self, other):
        if self.weight() == other.weight():
            return True
        else:
            return False
        
    def __lt__(self, other):
        if self.weight() < other.weight():
            return True
        else:
            return False
    


@functools.total_ordering
class DirectedEdge:

    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight
    
    def vfrom(self):
        return self._v
    
    def vto(self):
        return self._w
        
    def compare_to(self, other):

        if self < other:
            return -1
        elif self > other:
            return 1
        else:
            return 0
        
    def to_string(self):
        return f"{self._v}->{self._w}, {self._weight}"
    
    def __eq__(self, other):
        if self.weight() == other.weight():
            return True
        else:
            return False
        
    def __lt__(self, other):
        if self.weight() < other.weight():
            return True
        else:
            return False

'''
@functools.total_ordering
class SPEdgeWrapper:

    def __init__(self, index : int, edge : DirectedEdge, priority : float):
        self._index = index
        self._edge = edge
        self._priority = priority

    @property
    def index(self):
        return self._index
    
    @property
    def priority(self):
        return self._priority

    def to_string(self):
        return f"{self._index} {self._edge.to_string()}, {self._priority}"
    
    def __eq__(self, other):
        if self.priority == other.priority:
            return True
        else:
            return False
        
    def __lt__(self, other):
        print(f'self.priority: {self.priority}')
        if self.priority < other.priority:
            return True
        else:
            return False

'''
    