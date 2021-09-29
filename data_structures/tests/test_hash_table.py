from hashTable import HashTable


def test_import():
    assert HashTable


def test_hash_table1():
    tmp = HashTable()
    tmp.put("two", 2)
    tmp.put("twenty three", 23)
    tmp.put("one-two", 12)
    # import pdb; pdb.set_trace()
    assert tmp.get("two") == 2
    assert tmp.get("one-two") == 12


def test_hash_table2():
    tmp = HashTable()
    tmp.put("two", 2)
    tmp.put("twenty three", 23)
    tmp.put("one-two", 12)
    # import pdb; pdb.set_trace()
    assert not tmp.get("das")


def test_hash_table3():
    tmp = HashTable()
    tmp.put("two", 2)
    tmp.put("twenty three", 23)
    tmp.put("one-two", 12)
    assert not tmp.get("")


def test_hash_table4():
    tmp = HashTable()
    tmp.put("two", 2)
    tmp.put("twenty three", 23)
    tmp.put("one-two", 12)
    assert len(tmp) == 3
    tmp.put("two", 22)
    assert len(tmp) == 3
    assert tmp.get("two") == 22
