
class Graph:
    """
    Here we implement the famous data structure--graph.
    It's a data structure made up by nodes and edges.
    Generally tehre's no limitation on number of nodes, and number of edges.
    Edges can also be weighted or non-weighted.
    """

    def __init__(self, iterable = {}):
        """
        For here iterable only takes in vertices and weighted edges.
        Right now it only support format as:
        Graph({
            'A': {'B': 10},
            'B': {'A': 5, 'D': 15, 'C': 20},
            })
        """
        # import collections
        self.graph = {}
        self._size = 0
        # if isinstance(iterable, collections.Iterable):
        if isinstance(iterable, dict):
            for v1 in iterable.keys():
                self.add_vert(v1)

            for v1 in iterable.keys():
                for v2, weight in iterable[v1].items():
                    self.add_edge(v1, v2, weight)

    def __repr__(self):
        if self._size == 0:
            return "This is an empty graph."
        out = f'This is a graph with {self._size} nodes : {self.graph.keys()}'
        return out

    def __str__(self):
        if self._size == 0:
            return "This is an empty graph."
        out = f'This is a graph with {self._size} nodes : {self.graph.keys()}'
        return out

    def __len__(self):
        return self._size

    def add_vert(self, val):
        """
        """
        # add vertice to self.graph
        # check to see if the vert already exists: if so raise exception
            # create a helper method
        if self.has_vert(val):
            raise Exception(f'Input Value { val } already exists in this graph. Bad Input.')
        self.graph[val] = {}
        self._size += 1
        return self

    def has_vert(self, val):
        """
        checks for a key in the graph
        input: self of graph class, and a value to check
        output: a boolean value
        """
        return val in self.graph.keys()

    def add_edge(self, v1, v2, weight=1):
        """
        adding edge from v1 to v2 with given weight.
        if no weight is imported, it's set to default value 1.
        """
        # add a relationship and weight between two verts
        # don't forget to validate
        if not self.has_vert(v1):
            raise Exception(f'Input Value { v1 } does not exist in this graph. Bad Input.')
        if not self.has_vert(v2):
            raise Exception(f'Input Value { v2 } does not exist in this graph. Bad Input.')

        v1_edges = self.graph[v1]
        v1_edges[v2] = weight
        return self

    def get_neighbors(self, val):
        """
        Given a val (key), return all adjacent verts
        """
        if not self.has_vert(val):
            print(f'Input value {val} is not in this graph.')
            return None
        return self.graph[val]
