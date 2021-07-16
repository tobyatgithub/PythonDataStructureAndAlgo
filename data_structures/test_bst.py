import pytest
from .bst import BST, Node


def test_BST():
    assert BST()


def test_printNode():
    tmp = Node(5)
    assert str(tmp) == "This is a tree node with value = 5 and left = None and right = None"


def test_printTree():
    tmp = BST([1])
    # import pdb; pdb.set_trace()
    assert str(tmp) == 'This is a binay search tree with root = 1'


def test_badinput():
    with pytest.raises(TypeError):
        BST(22)


def test_insert1():
    tmp = BST()
    tmp.insert(1)
    assert tmp.root.val == 1


def test_insert2():
    tmp = BST()
    tmp.insert(5)
    tmp.insert(2)
    tmp.insert(6)
    assert tmp.root.val == 5
    assert tmp.root.right.val == 6
    assert tmp.root.left.val == 2


def test_insertmany():
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    assert tmp.root.right.val == 40
    assert tmp.root.right.right == None
    assert tmp.root.left.val == 18
    # import pdb; pdb.set_trace()
    assert tmp.root.left.right.val == 19


def test_preOrder(capsys):
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    tmp.preOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '20\n18\n12\n11\n14\n19\n40\n31\n22\n33\n'


def test_preOrder2(capsys):
    tmp = BST([20])
    tmp.preOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '20\n'


def test_postOrder(capsys):
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    tmp.postOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '11\n14\n12\n19\n18\n22\n33\n31\n40\n20\n'


def test_postOrder2(capsys):
    tmp = BST([33])
    tmp.postOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '33\n'


def test_inOrder1(capsys):
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    tmp.inOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '11\n12\n14\n18\n19\n20\n22\n31\n33\n40\n'


def test_inOrder2(capsys):
    tmp = BST([1])
    tmp.inOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == '1\n'


def test_find_max1():
    tmp = BST()
    assert tmp.find_maximum_value() == None


def test_find_max2():
    tmp = BST([1])
    assert tmp.find_maximum_value() == 1


def test_find_max3():
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    assert tmp.find_maximum_value() == 40


def test_inOrder2(capsys):
    tmp = BST([9,3,4,8])
    tmp.inOrder(tmp.root)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    # assert captured.out == '1\n'
    print(captured)
