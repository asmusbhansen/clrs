from clrs.data_structures.edge import Edge

class GraphReader:

    def __init__(self, edge_type):

        self.edge_type = edge_type

    def read(self, filename):

        with open(filename) as file:

            self.weights = []

            self.num_vertices = int(next(file).rstrip())
            self.num_edges = int(next(file).rstrip())
            
            for line in file:
                edge_params = line.rstrip().split(' ')
                edge_params = {'v': int(edge_params[0]), 'w': int(edge_params[1]), 'weight': float(edge_params[2])}

                self.weights += [self.edge_type(**edge_params)]

            #print(self.num_vertices)
            #print(self.num_edges)
            #print(self.weights)
        return self.num_vertices, self.num_edges, self.weights
#GraphReader(filename='data/graph_files/tinyEWG.txt')

            