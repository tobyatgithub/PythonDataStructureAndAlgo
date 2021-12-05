
class Graph:
    """
    Here we implement the famous data structure--graph.
    It's a data structure made up by nodes and edges.
    Generally tehre's no limitation on number of nodes, and number of edges.
    Edges can also be weighted or non-weighted.
    """
    def __init__(self, iterable={}, directional=True):
        """
        For here iterable only takes in vertices and weighted edges.
        Right now it only support format as:
        Graph({
            'A': {'B': 10},
            'B': {'A': 5, 'D': 15, 'C': 20},
            })
        """
        self.graph = {}
        self._size = 0
        self.directional = directional
        if isinstance(iterable, dict):
            for v1 in iterable.keys():
                self.add_vertex(v1)
                for v2, weight in iterable[v1].items():
                    self.add_edge(v1, v2, weight)

    def __repr__(self):
        if self._size == 0:
            print("This is an empty graph.")
        return str(self.graph)

    def __str__(self):
        if self._size == 0:
            return "This is an empty graph."
        return str(self.graph)

    def __len__(self):
        return self._size

    def add_vertex(self, val):
        if not self.has_vertex(val):
            self.graph[val] = {}
            self._size += 1
        return self

    def add_edge(self, v1, v2, weight=1):
        """
        adding edge from v1 to v2 with given weight.
        if no weight is imported, it's set to default value 1.
        """
        if not self.has_vertex(v1):
            self.add_vertex(v1)
        if not self.has_vertex(v2):
            self.add_vertex(v2)
            
        self.graph[v1][v2] = weight

        # if bi-directional, then we also need to add the second direction
        if not self.directional:
            self.graph[v2][v1] = weight
        return self

    def has_vertex(self, val):
        """
        checks for a key in the graph
        input: self of graph class, and a value to check
        output: a boolean value
        """
        return val in self.graph

    def get_vertexs(self):
        return sorted(list(self.graph.keys()))

    def get_weight(self, fromNode, toNode):
        return self.graph.get(fromNode, {}).get(toNode)

    def get_neighbors(self, val):
        """
        Given a val (key), return all adjacent verts
        """
        if not self.has_vertex(val):
            print(f'Input value {val} is not in this graph.')
            return {}
        return self.graph[val]

    def get_all_edges(self, sortResult=False):
        """
        Return a list of edges in the form of:
        [(from_node, to_node, weight), ()...]
        """
        res = set()
        V = self.get_vertexs()
        for vertex in V:
            for neighbor in self.get_neighbors(vertex):
                res.add((vertex, neighbor, self.get_weight(vertex, neighbor)))
        if sortResult:
            res = sorted(res, key=lambda x: (x[0],x[1]))
        return list(res)