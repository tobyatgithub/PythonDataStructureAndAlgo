import sys
import math

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

import json
from data_structures.graph import Graph

tmp = Graph(directional=False)
tmp.add_edge("boston", "miami", 12)
tmp.add_edge("calgary", "phoenix", 13)
tmp.add_edge("calgary", "salt lake city", 7)
tmp.add_edge("chicago", "new orleans", 7)
tmp.add_edge("chicago", "santa fe", 9)
tmp.add_edge("dallas", "new york", 11)
tmp.add_edge("denver", "el paso", 4)
tmp.add_edge("denver", "pittsburgh", 11)
tmp.add_edge("duluth", "el paso", 10)
tmp.add_edge("duluth", "houston", 8)
tmp.add_edge("helena", "los angeles", 8)
tmp.add_edge("kansas city", "houston", 5)
tmp.add_edge("los angeles", "chicago", 16)
tmp.add_edge("los angeles", "miami", 20)
tmp.add_edge("los angeles", "new york", 21)
tmp.add_edge("montreal", "atlanta", 9)
tmp.add_edge("montreal", "new orleans", 13)
tmp.add_edge("new york", "atlanta", 6)
tmp.add_edge("portland", "nashville", 17)
tmp.add_edge("portland", "phoenix", 11)
tmp.add_edge("san francisco", "atlanta", 17)
tmp.add_edge("sanult st marie", "nashville", 8)
tmp.add_edge("sanult st marie", "oklahoma city", 9)
tmp.add_edge("seattle", "los angeles", 9)
tmp.add_edge("seattle", "new york", 22)
tmp.add_edge("toronto", "miami", 10)
tmp.add_edge("vancouver", "montreal", 20)
tmp.add_edge("vancouver", "santa fe", 13)
tmp.add_edge("winnipeg", "houston", 12)
tmp.add_edge("winnipeg", "little rock", 11)

print(json.dumps(tmp.graph, sort_keys=True, indent=4))


def dijkstra(graph, source="vancouver"):
    """
    Assuming non-negative edges, dijkstra solves the single-source 
    shortest-paths problem on a weighted directed graph.
    It maintains a set S of vertices whose final shortest-path 
    weights from the source s have already been determined.
    """

    S = set()
    Q = graph.get_vertexs()
    NUM_VERTEX = len(graph)

    # we also need a map between city names to index
    mapping = {}
    for i in range(NUM_VERTEX):
        mapping[Q[i]] = i

    # initializing
    distance = [math.inf for _ in range(NUM_VERTEX)]
    prev = [None for _ in range(NUM_VERTEX)]
    distance[mapping[source]] = 0

    def relax(from_Node, to_Node, weight):
        nonlocal distance
        nonlocal prev
        from_index, to_index = mapping.get(from_Node), mapping.get(to_Node)
        if distance[to_index] > distance[from_index] + weight:
            distance[to_index] = distance[from_index] + weight
            prev[to_index] = from_Node

    for i in range(NUM_VERTEX):
        node = Q(distance.index(min(distance)))  # find min city from Q
        S.add(node)
        print(f"node = {node}")
        for v in graph.get_neighbors(node):
            print(f"examing neighbor of {node} = {v}")
            relax(node, v, graph.get_weight(node, v))
        # break
    print(distance)
    return


dijkstra(tmp)