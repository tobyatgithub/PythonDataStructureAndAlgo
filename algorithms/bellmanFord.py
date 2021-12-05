import sys
import math
import numpy as np

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

import json
from data_structures.graph import Graph


def bellmanFord(graph: Graph, source: str, DEBUG: bool = False) -> list:
    """
    Idea: It uses idea of dp, and maintains a table to store all
    the possible shortest path from the source to every other node.
    The brilliance is that we actually can be sure that we at most 
    only need to run num_of_vertice times to update to the optimal
    (assuming no negative cycle.)
    That being said, we can run it one more time afterward to detect
    wheter the graph contains any negative cycle.

    Process:
    One major difference of bellman and dijkstra is that bellman
    update the dp table by iterating through every edge.
    """
    def relax(from_Node, to_Node, weight):
        """
        Update the distance by the new minimum, 
        and if so update the to_node's partent
        to from node (we remember this info by index).
        """
        nonlocal distance
        nonlocal prev
        from_index, to_index = mapping.get(from_Node), mapping.get(to_Node)
        if distance[to_index] > distance[from_index] + weight:
            distance[to_index] = distance[from_index] + weight
            prev[to_index] = from_Node

    Q = graph.get_vertexs()
    NUM_VERTEX = len(graph)
    candidate_index = set([_ for _ in range(NUM_VERTEX)])

    # we also need a map between city names to index
    mapping = {}
    for i in range(NUM_VERTEX):
        mapping[Q[i]] = i

    # initializing
    distance = [math.inf for _ in range(NUM_VERTEX)]
    prev = [None for _ in range(NUM_VERTEX)]
    distance[mapping[source]] = 0

    for edge in graph.get_edges():
    return []


def task1():
    def buildTmpGraph():
        tmp = Graph(directional=True)
        tmp.add_edge("G", "E", 9)
        tmp.add_edge("F", "G", 11)
        tmp.add_edge("E", "F", 8)
        tmp.add_edge("E", "D", -15)
        tmp.add_edge("E", "C", 5)
        tmp.add_edge("D", "F", 6)
        tmp.add_edge("D", "B", 9)
        tmp.add_edge("C", "B", -8)
        tmp.add_edge("B", "E", 7)
        tmp.add_edge("B", "A", -7)
        tmp.add_edge("A", "D", 5)
        return tmp

    tmp = buildTmpGraph()
    print(tmp.get_vertexs())
    # if DEBUG: print(json.dumps(tmp.graph, sort_keys=True, indent=4))
    return bellhamFord(tmp, source="A", DEBUG=True)