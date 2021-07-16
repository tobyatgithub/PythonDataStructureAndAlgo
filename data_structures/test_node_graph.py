from .node_graph import Vertex, graph
import pytest


@pytest.fixture()
def vertex1():
    tmp = Vertex("A")
    tmp.addNeighbor("B", 5)
    tmp.addNeighbor("C", 3)
    tmp.addNeighbor("D", 10)
    return tmp


@pytest.fixture()
def small_graph():
    tmp = graph()
    tmp.addVertex("A")
    tmp.addVertex("B")
    tmp.addVertex("C")
    tmp.addVertex("D")
    tmp.addVertex("E")
    tmp.addEdge("A", "B", 2)
    tmp.addEdge("B", "A", 2)
    tmp.addEdge("B", "C", 1)
    tmp.addEdge("B", "D", 3)
    tmp.addEdge("B", "E", 5)
    tmp.addEdge("D", "E", 5)
    return tmp


def test_vertex_import():
    assert Vertex


def test_vertex_print(capsys, vertex1):
    print(vertex1)
    captured = capsys.readouterr()
    assert 'Vertex A is connected to:' in captured.out


def test_breadthfirstsearch1(capsys, small_graph):
    start = small_graph.getVertex("B")
    small_graph.BreadthFirstSearch(start)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert 'B A C D E \n' in captured.out


def test_breadthfirstsearch2(capsys, small_graph):
    start = small_graph.getVertex("A")
    small_graph.BreadthFirstSearch(start)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert 'A B C D E \n' in captured.out


def test_breadthfirstsearch3(capsys, small_graph):
    start = small_graph.getVertex("D")
    small_graph.BreadthFirstSearch(start)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert 'D E \n' in captured.out
