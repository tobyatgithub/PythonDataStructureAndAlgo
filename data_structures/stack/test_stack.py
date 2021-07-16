from .stack import Stack
from node import Node
import pytest

@pytest.fixture()
def empty_stack():
    return Stack()

@pytest.fixture()
def single_stack():
    tmp = Stack()
    tmp.push(2)
    return tmp

@pytest.fixture()
def mid_stack():
    tmp = Stack()
    tmp.push(2)
    tmp.push("4")
    tmp.push(['6'])
    return tmp

@pytest.fixture()
def long_stack():
    return Stack([5,4,3,2,1])



def test_empty_stack(empty_stack):
    # because empty stack is empty, pytest test whether assert True
    assert not empty_stack

def test_input_rasie():
    # tmp = Stack(2)
    with pytest.raises(TypeError):
        Stack(2)
    # assert TypeError("Stack only take <None> or a <list> as input init value")

def test_singly_stack(single_stack):
    assert len(single_stack) == 1
    single_stack.push(22)
    assert len(single_stack) == 2

def test_singly_stack2(single_stack):
    assert single_stack.peek().val == 2
    assert len(single_stack) == 1

def test_stack_length(empty_stack):
    assert len(empty_stack) == 0

def test_iterable_input_stack(long_stack):
    assert long_stack
    assert long_stack.peek().val == 1

def test_stack_pop_empty(empty_stack):
    assert empty_stack.pop() == None


def test_stack_pop1(single_stack):
    # before
    assert len(single_stack) == 1
    assert single_stack.pop().val == 2
    #after
    assert len(single_stack) == 0


def test_stack_pop3(mid_stack):
    assert mid_stack.pop().val ==['6']

def test_stack_pop2(long_stack):
    assert long_stack.pop().val == 1
