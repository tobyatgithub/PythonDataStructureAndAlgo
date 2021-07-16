import pytest
from .queue import Queue



@pytest.fixture()
def empty_queue():
    return Queue()

@pytest.fixture()
def single_queue():
    tmp = Queue()
    tmp.enqueue(3)
    return tmp

def test_empty_queue(empty_queue):
    assert not empty_queue
    assert len(empty_queue) == 0

def test_input_error_raise1():
    with pytest.raises(TypeError):
        Queue("balala")

def test_iterat_queue_input():
    tmp = Queue([1,2,3,4,5])
    assert len(tmp) == 5
    assert tmp.dequeue().val == 1
    assert len(tmp) == 4

def test_enqueue1(single_queue):
    assert len(single_queue) == 1
    assert single_queue.peek().val == 3

def test_enqueue2(empty_queue):
    # before
    assert len(empty_queue) == 0

    empty_queue.enqueue(4)
    # after
    assert len(empty_queue) == 1
    assert (empty_queue.peek().val) == 4

def test_enqueue3(empty_queue):
    empty_queue.enqueue(['come on'])
    assert len(empty_queue) == 1
    assert empty_queue.peek().val == ['come on']


def test_dequeue1(empty_queue):
    assert empty_queue.dequeue() == None

def test_dequeue2(single_queue):
    assert len(single_queue) == 1
    assert single_queue.dequeue().val == 3
    assert len(single_queue) == 0

def test_dequeue3(empty_queue):
    empty_queue.enqueue(3)
    empty_queue.enqueue("2")
    empty_queue.enqueue([4])

    assert empty_queue.dequeue().val == 3
    assert empty_queue.dequeue().val == "2"
    assert empty_queue.dequeue().val == [4]
    assert len(empty_queue) == 0
