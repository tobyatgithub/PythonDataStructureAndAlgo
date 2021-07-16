class Vertex:
    def __init__(self, value):
        self.value = value
        self.connectedTo = {}
        self.visited = False

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def get_value(self):
        return self.value

    def getNeighbor(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        out = f'Vertex { self.value } is connected to:'
        for n, w in self.connectedTo.items():
            out += f'\t { n }: { w },'
        return out

    def __repr__(self):
        out = f'Vertex { self.value } is connected to:'
        for n, w in self.connectedTo.items():
            out += f'\t { n }: { w },'
#         out += '\n'
        return out


class graph:
    def __init__(self):
        self.vertices = {}
        self._size = 0

    def addVertex(self, value):
        """
        Assuming vertex value is unique for any given graph.
        """
        if value in self.vertices:
            out = f'Value { value } already exist!'
            print(out)
        else:
            out = f'Vertex { value } added!'
            self.vertices[value] = Vertex(value)
            print(out)

    def getVertex(self, value):
        """
        Get vertex with value == value, you can assume
        it's unique for now.
        """
        if value not in self.vertices:
            out = f'Value { value } does not exist!'
            print(out)
        else:
            return self.vertices[value]

    def __contains__(self, value):
        pass

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(t, weight)

    def addTwoWayEdges(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(t, weight)
        self.vertices[t].addNeighbor(f, weight)

    def getVertices(self):
        return self.vertices

    def __iter__(self):
        pass

    def __srt__(self):
        pass

    def search_helper(self):
        tmp_dict = self.getVertices() # a dict
        for v in tmp_dict.keys():
            tmp_v = self.getVertex(v)
            if tmp_v.visited:
                print(f'cleaned vertex { tmp_v }')
                tmp_v.visited = False

        print("finished cleaning. All vertices visited false.")

    def BreadthFirstSearch(self, start):
        """
        print out vertices in the order of breadth first with respect to the starting node
        """
        # first we init visited status
        self.search_helper()

        queue = [start]
        start.visited = True
        out = ""
        while len(queue) >= 1:
            current = queue.pop(0)
            out += f'{current.value} '
            # print("while looping", current)
            nbrs = current.getNeighbor()
            for n in nbrs:
                node = self.getVertex(n)
                if not node.visited:
                    queue.append(node)
                    node.visited = True

        # clean up the visit history
        self.search_helper()
        print(out)
        return self



