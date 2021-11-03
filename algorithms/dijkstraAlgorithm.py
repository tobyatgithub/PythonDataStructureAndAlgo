import sys

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

from data_structures.graph import Graph

tmp = Graph({"Vancouver": {"Seattle": 1, "Portland": 2}})
print(tmp)