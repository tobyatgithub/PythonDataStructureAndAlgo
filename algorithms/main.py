# to make the imports work.
import sys

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

from data_structures.node import Node

a = Node("sda")
print(a)


def partC(x):
    return (2 * x - 3) / (x - 2)


tmp = partC(2021)  #f1
print(f"the first time, = f1 = tmp = {tmp}")

for i in range(2021):
    tmp = partC(tmp)
    print(i, tmp)
