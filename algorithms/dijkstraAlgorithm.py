import sys
import math

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

import json
from data_structures.graph import Graph


def buildTrainRideGraph():
    tmp = Graph(directional=False)
    tmp.add_edge("atlanta", "new orleans", 4)
    tmp.add_edge("atlanta", "nashville", 1)
    tmp.add_edge("atlanta", "charleston", 2)

    tmp.add_edge("boston", "new york", 2)
    tmp.add_edge("boston", "montreal", 2)

    tmp.add_edge("calgary", "vancouver", 3)
    tmp.add_edge("calgary", "seattle", 4)
    tmp.add_edge("calgary", "winnipeg", 6)
    tmp.add_edge("calgary", "helena", 4)

    tmp.add_edge("chicago", "duluth", 3)
    tmp.add_edge("chicago", "omaha", 4)
    tmp.add_edge("chicago", "saint louis", 2)
    tmp.add_edge("chicago", "pittsburge", 3)
    tmp.add_edge("chicago", "toronto", 4)

    tmp.add_edge("dallas", "el paso", 4)
    tmp.add_edge("dallas", "houston", 1)
    tmp.add_edge("dallas", "little rock", 2)
    tmp.add_edge("dallas", "oklahoma city", 2)
    tmp.add_edge("denver", "helena", 4)
    tmp.add_edge("denver", "salt lake city", 3)
    tmp.add_edge("denver", "phoenix", 5)
    tmp.add_edge("denver", "santa fe", 2)
    tmp.add_edge("denver", "oklahoma city", 4)
    tmp.add_edge("denver", "kansas city", 4)
    tmp.add_edge("denver", "omaha", 4)
    tmp.add_edge("duluth", "winnipeg", 4)
    tmp.add_edge("duluth", "helena", 6)
    tmp.add_edge("duluth", "omaha", 2)
    tmp.add_edge("duluth", "chicago", 3)
    tmp.add_edge("duluth", "toronto", 6)
    tmp.add_edge("duluth", "sault st marie", 3)

    tmp.add_edge("el paso", "houston", 6)
    tmp.add_edge("el paso", "santa fe", 2)
    tmp.add_edge("el paso", "oklahoma city", 5)
    tmp.add_edge("el paso", "phoenix", 3)

    tmp.add_edge("helena", "winnipeg", 4)
    tmp.add_edge("helena", "seattle", 6)
    tmp.add_edge("helena", "salt lake city", 3)
    tmp.add_edge("helena", "omaha", 5)
    tmp.add_edge("houston", "new orleans", 2)

    tmp.add_edge("kansas city", "saint louis", 2)
    tmp.add_edge("kansas city", "omaha", 1)
    tmp.add_edge("kansas city", "oklahoma city", 2)

    tmp.add_edge("los angeles", "san francisco", 3)
    tmp.add_edge("los angeles", "el paso", 6)
    tmp.add_edge("los angeles", "las vegas", 2)
    tmp.add_edge("los angeles", "phoenix", 3)
    tmp.add_edge("little rock", "new orleans", 3)
    tmp.add_edge("little rock", "dallas", 2)
    tmp.add_edge("little rock", "oklahoma city", 2)
    tmp.add_edge("little rock", "saint louis", 2)
    tmp.add_edge("little rock", "nashville", 3)
    tmp.add_edge("las vegas", "salt lake city", 3)

    tmp.add_edge("miami", "new orleans", 6)
    tmp.add_edge("miami", "atlanta", 5)
    tmp.add_edge("miami", "charleston", 4)
    tmp.add_edge("montreal", "sault st marie", 5)
    tmp.add_edge("montreal", "toronto", 3)
    tmp.add_edge("montreal", "new york", 3)
    tmp.add_edge("montreal", "boston", 2)

    tmp.add_edge("new york", "washington", 2)
    tmp.add_edge("new york", "pittsburge", 2)
    tmp.add_edge("nashville", "saint louis", 2)

    tmp.add_edge("portland", "salt lake city", 6)
    tmp.add_edge("portland", "san francisco", 5)
    tmp.add_edge("portland", "seattle", 1)
    tmp.add_edge("pittsburge", "washington", 2)
    tmp.add_edge("pittsburge", "saint louis", 5)
    tmp.add_edge("pittsburge", "nashville", 4)
    tmp.add_edge("pittsburge", "raleich", 2)
    tmp.add_edge("pittsburge", "toronto", 2)
    tmp.add_edge("phoenix", "santa fe", 3)

    tmp.add_edge("oklahoma city", "santa fe", 3)

    tmp.add_edge("raleich", "nashville", 3)
    tmp.add_edge("raleich", "atlanta", 2)
    tmp.add_edge("raleich", "charleston", 2)
    tmp.add_edge("raleich", "washington", 2)

    tmp.add_edge("san francisco", "salt lake city", 5)
    tmp.add_edge("sault st marie", "winnipeg", 6)
    tmp.add_edge("sault st marie", "toronto", 2)
    tmp.add_edge("seattle", "vancouver", 1)
    return tmp


tmp = buildTrainRideGraph()
print(json.dumps(tmp.graph, sort_keys=True, indent=4))


def find_index_minValue(all_index_set, seen_index_set, distance_list):
    """
    all_index_set: a set with all the initial indexs {1,2,3...}
    seen_index_set: a set with seen indexs {4,8,...}
    distance_list: the list containing distance info of each index node, from which we determine the minValue
    """
    if not isinstance(all_index_set, set) and not isinstance(
            seen_index_set, set):
        raise TypeError("Inputs have to be set type.")
    candidate_index = all_index_set.difference(seen_index_set)
    min_value = max(distance_list)
    min_value_index = -1
    for index in candidate_index:
        if distance_list[index] <= min_value:
            min_value = distance_list[index]
            min_value_index = index
    return min_value_index


def dijkstra(graph, source="vancouver"):
    """
    Assuming non-negative edges, dijkstra solves the single-source 
    shortest-paths problem on a weighted directed graph.
    It maintains a set S of vertices whose final shortest-path 
    weights from the source s have already been determined.
    """

    Seen_index = set()  # the S in pesudo code
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

    def relax(from_Node, to_Node, weight):
        nonlocal distance
        nonlocal prev
        from_index, to_index = mapping.get(from_Node), mapping.get(to_Node)
        if distance[to_index] > distance[from_index] + weight:
            distance[to_index] = distance[from_index] + weight
            prev[to_index] = from_Node

    for i in range(NUM_VERTEX):
        node_index = find_index_minValue(candidate_index, Seen_index, distance)
        Seen_index.add(node_index)
        node = Q[node_index]
        print(f"node = {node}")
        for v in graph.get_neighbors(node):
            print(f"examing neighbor of {node} = {v}")
            relax(node, v, graph.get_weight(node, v))
        # break
    print(distance)
    return distance


dijkstra(tmp)