import sys
import math
import numpy as np

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

import json
from data_structures.graph import Graph

DEBUG = False


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


def dijkstra(graph, source="vancouver", DEBUG=False):
    """
    Assuming non-negative edges, dijkstra solves the single-source 
    shortest-paths problem on a weighted directed graph.

    Idea: it also uses idea of dp, and maintains two tables. One to
    remember all the possible shortest path from the source, the 
    other remember the parent node that provides the current shortest
    path.
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
    if DEBUG:
        print("Initializing...")
        print(f"Init distance to: {distance}")
        print(f"Init prev to: {prev}\n")

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

    for i in range(NUM_VERTEX):
        node_index = find_index_minValue(candidate_index, Seen_index, distance)
        Seen_index.add(node_index)
        node = Q[node_index]
        if DEBUG: print(f"node = {node}")
        for v in graph.get_neighbors(node):
            relax(node, v, graph.get_weight(node, v))
            if DEBUG:
                print(f"examing neighbor of {node} = {v}")
                print(f"Update distance to: {distance}")
                print(f"Update prev to: {prev}")
    if DEBUG: print(distance)
    return distance


def task1():
    tmp = buildTrainRideGraph()
    if DEBUG: print(json.dumps(tmp.graph, sort_keys=True, indent=4))
    dijkstra(tmp, source="vancouver")


# optional
def task2():
    tmp = buildTrainRideGraph()
    if DEBUG: print(json.dumps(tmp.graph, sort_keys=True, indent=4))
    Q = tmp.get_vertexs()
    cities = set(tmp.get_vertexs())
    for city in cities:
        tmp_distance = np.array(dijkstra(tmp, source=city))
        tmp_max = max(tmp_distance)
        for endCityIndex in np.where(tmp_distance == tmp_max)[0]:
            print(
                f"Source={city}, destination={Q[endCityIndex]}, with max distance={tmp_max}."
            )
        # break


def task3():
    def buildTmpGraph():
        tmp = Graph(directional=False)
        tmp.add_edge("A", "B", 7)
        tmp.add_edge("A", "D", 5)
        tmp.add_edge("D", "B", 9)
        tmp.add_edge("C", "B", 8)
        tmp.add_edge("C", "E", 5)
        tmp.add_edge("B", "E", 7)
        tmp.add_edge("D", "E", 15)
        tmp.add_edge("D", "F", 6)
        tmp.add_edge("E", "F", -8)
        tmp.add_edge("E", "G", 9)
        tmp.add_edge("G", "F", 11)
        return tmp

    tmp = buildTmpGraph()
    import pdb

    pdb.set_trace()
    print(tmp.get_vertexs())
    # if DEBUG: print(json.dumps(tmp.graph, sort_keys=True, indent=4))
    return dijkstra(tmp, source="G", DEBUG=True)


task3 = task3()

print(task3)
