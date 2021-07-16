import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_one():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'E': 1},
        'D': {'A': 5},
        'E': {'F': 2, 'B': 4},
        'F': {'D': 11}
    }
    g._size = 6
    return g


@pytest.fixture()
def graph_two():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    g._size = 7
    return g


def test_graph_class_exist(graph_empty):
    assert not graph_empty


def test_pring(capsys, graph_empty):
    print(graph_empty)
    captured = capsys.readouterr()
    assert captured.out == "This is an empty graph.\n"


def test_print2(capsys, graph_one):
    print(graph_one)
    captured = capsys.readouterr()
    assert captured.out == f'This is a graph with {graph_one._size} nodes : {graph_one.graph.keys()}\n'


def test_has_vert1(graph_empty):
    assert not graph_empty.has_vert(1)


def test_has_vert2(graph_one):
    assert graph_one.has_vert("A")


def test_has_vert3(graph_one):
    assert not graph_one.has_vert("Z")


def test_add_vert(graph_empty):
    assert len(graph_empty) == 0
    graph_empty.add_vert("Toby")
    assert len(graph_empty) == 1
    assert graph_empty.has_vert("Toby")


def test_add_vert2(graph_one):
    assert len(graph_one) == 6
    graph_one.add_vert("Z")
    assert len(graph_one) == 7
    assert graph_one.has_vert("Z")


def test_add_vert3(graph_one):
    """
    check see the non-duplicate exception for add_vert function
    """
    with pytest.raises(Exception):
        graph_one.add_vert("A")


def test_add_edge1(graph_empty):
    assert len(graph_empty) == 0
    graph_empty.add_vert("hello")
    graph_empty.add_vert("world")
    assert len(graph_empty) == 2

    graph_empty.add_edge("hello", "world", 25)
    assert graph_empty.graph["hello"]["world"] == 25


def test_add_edge2(graph_one):
    assert graph_one.graph["F"]["D"] == 11
    graph_one.add_edge("F","D",1)
    assert graph_one.graph["F"]["D"] == 1


def test_add_edge3(graph_empty):
    with pytest.raises(Exception):
        graph_empty.add_edge("Super", "Smash", 99)


def test_get_neightbor1(graph_empty):
    assert not graph_empty.get_neighbors("A")


def test_get_neightbor2(graph_one):
    assert graph_one.get_neighbors("C") == {'E': 1}


def test_get_neightbor3(graph_two):
    assert graph_two.get_neighbors('B') == {'D': 15, 'E': 5, 'C': 2}


def test_init_with_iterable():
    test_dict = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'E': 1},
        'D': {'A': 5},
        'E': {'F': 2, 'B': 4},
        'F': {'D': 11}
    }
    test_graph = Graph(test_dict)
    assert test_graph
    assert test_graph.has_vert("A")
    assert test_graph.get_neighbors("C") == {'E': 1}
    assert len(test_graph) == 6
