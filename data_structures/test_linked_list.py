from linked_list import linked_list
import pytest

@pytest.fixture(scope = "function")
def empty_ll():
    return linked_list()

@pytest.fixture(scope = "function")
def small_ll():
    ll = linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll

@pytest.fixture(scope = "function")
def random_ll():
    from random import randint
    ll = linked_list()
    for i in range(100):
        ll.insert(randint(0,100))
    return ll

# test definition
def test_ll_module_exists():
    assert linked_list

def test_ll_head_is_none(empty_ll):
    assert empty_ll.head is None


# test string method
def test_ll_str_method(empty_ll):
    assert str(empty_ll) == f'Linked List: Head val - { empty_ll.head }'

# test length
def test_size_of_empty_ll(empty_ll):
    assert len(empty_ll) == 0

def test_small_fixture_has_size_of_4(small_ll):
    assert len(small_ll) == 4

# test insert
def test_insert_new_node_into_empty(empty_ll):
    # test before
    assert empty_ll.head is None

    # do the thing,
    empty_ll.insert(1)

    # test after
    assert empty_ll.head.val == 1

def test_random_ll(random_ll):
    assert len(random_ll) == 100

# test iterable
def test_iterable_as_argument():
    ll = linked_list([1,2,3,4])
    assert ll.head.val == 4

# test includes
def test_empty_includes(empty_ll):
    assert empty_ll.includes(233) == False

def test_includes1(small_ll):
    assert small_ll.includes(4) == True
    assert small_ll.includes(1) == True

def test_includes2(small_ll):
    assert small_ll.includes(5) == False


# test append
def test_append(empty_ll):
    # empty_ll.append(2)
    empty_ll.append(3)
    print("empty_ll = ", empty_ll)
    assert len(empty_ll) == 1
    assert empty_ll.includes(3) == True
    assert empty_ll.head._next is None

def test_append1(empty_ll):
    empty_ll.append(2)
    empty_ll.append(3)
    assert len(empty_ll) == 2
    assert empty_ll.head.val == 2
    assert empty_ll.head._next.val == 3
    assert empty_ll.includes(3) is True
    # fixed: can't modify self.head in includes.
    assert empty_ll.includes(2) is True
    assert empty_ll.head._next._next is None


def test_append2(small_ll):
    small_ll.append(44)
    small_ll.append(55)
    assert len(small_ll) == 6
    assert small_ll.includes(44) is True
    assert small_ll.includes(55) is True
    assert small_ll.includes(66) is False

# test insertBefore

# test the edge case where we are given an empty ll,
# insert shall not happen and ll shall remain empty
def test_insertBefore1(empty_ll):
    empty_ll.insertBefore(50, 1)
    assert len(empty_ll) == 0
    assert empty_ll.includes(50) is False
    # assert empty_ll.head.val == 3

# edge case 2, where we try to insert before the head.
def test_insertBefore2(small_ll):
    # before
    assert len(small_ll) == 4
    assert small_ll.head.val == 4
    # due to the nature of insert. 4 is the head of small_ll
    small_ll.insertBefore(4, 50)

    # after
    assert len(small_ll) == 5
    assert small_ll.includes(50) is True
    assert small_ll.head.val == 50

def test_insertBefore3(small_ll):
    # before
    assert len(small_ll) == 4
    assert small_ll.head.val == 4
    # due to the nature of insert. 4 is the head of small_ll
    small_ll.insertBefore(1, 50)
    small_ll.insertBefore(50, 26)

    # after
    assert len(small_ll) == 6
    assert small_ll.includes(26) is True

# test insertAfter

# test the edge case where we are given an empty ll,
# insert shall not happen and ll shall remain empty
def test_insertAfter1(empty_ll):
    empty_ll.insertAfter(50, 1)
    assert len(empty_ll) == 0
    assert empty_ll.includes(50) is False

# edge case 2, where we try to insert at the end.
def test_insertAfter2(small_ll):
    # before
    assert len(small_ll) == 4
    assert small_ll.head.val == 4
    # due to the nature of insert. 1 is the end of small_ll
    small_ll.insertAfter(1, 50)
    # after
    assert len(small_ll) == 5
    assert small_ll.includes(50) is True
    assert small_ll.head._next._next._next._next.val == 50

def test_insertAfter3(small_ll):
    # before
    assert len(small_ll) == 4
    assert small_ll.head.val == 4
    #insert
    small_ll.insertAfter(1, 50)
    small_ll.insertAfter(50, 26)
    # after
    assert len(small_ll) == 6
    assert small_ll.includes(26) is True


# test delete_node
def test_delete_node(empty_ll):
    empty_ll.delete_node(10)
    assert len(empty_ll) == 0
    assert empty_ll.includes(10) is False

def test_delete_node2(small_ll):
    #before
    assert small_ll.includes(4) is True
    small_ll.delete_node(4)

    #after
    assert len(small_ll) == 3
    assert small_ll.includes(4) is False
    assert small_ll.includes(1) is True

def test_delete_node3(small_ll):
    #before
    assert small_ll.includes(1) is True
    small_ll.delete_node(1)

    #after
    assert len(small_ll) == 3
    assert small_ll.includes(1) is False
    assert small_ll.includes(4) is True

# testing ll_kth_from_end
def test_ll_kth_from_end(empty_ll):
    assert empty_ll.ll_kth_from_end(2) == 'Exception'
    assert empty_ll.ll_kth_from_end(44) == 'Exception'

def test_ll_kth_from_end2(small_ll):
    # small_ll: head-4-3-2-1-x
    assert small_ll.ll_kth_from_end(1) == 1
    assert small_ll.ll_kth_from_end(2) == 2
    assert small_ll.ll_kth_from_end(3) == 3
    assert small_ll.ll_kth_from_end(4) == 4
    assert small_ll.ll_kth_from_end(6) == 'Exception'

def test_ll_kth_from_end_input(small_ll):
    assert small_ll.ll_kth_from_end(1.2) == 'Exception'
    assert small_ll.ll_kth_from_end(-3) == 'Exception'
