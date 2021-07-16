class HashTable:
    """
    A class for a hash table. We solve data coliision here by inforcing
    unique key. If a same key is passed in, it will replace the previous one.
    The default size is 17 so as easy to debug, but is subject to change as
    one input variable.
    Noitce that we only take in str as key.
    """

    def __init__(self, size=17):
        self.entries_count = 0
        self.alphabet_size = 52
        self.table_size = size
        self.hashtable = [[] for _ in range(size)]
        # usually we would like size to be a prime number
        #  to reduce chance of data collision

    def __repr__(self):
        return "<HashTable: {}>".format(self.hashtable)

    def __len__(self):
        return self.entries_count

    def _hash_key(self, key):
        """
        Takes in string key and turn that into a hash result.
        input: key (str)
        output: hash value (int)
        """
        if len(key) == 0:
            return 0
        _key = ''.join(str(ord(c)) for c in key)
        return int(_key) % self.table_size

    def put(self, key, value):
        """
        Add a key and value into the hash table.
        input: key(str), value(*)
        output: None
        """
        if not isinstance(key, str):
            raise TypeError("Only strings can be used as keys")

        hash_ = self._hash_key(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                del self.hashtable[hash_][i]
                self.entries_count -= 1
        self.hashtable[hash_].append((key, value))
        self.entries_count += 1

    def get(self, key):
        """
        Retrieve a value from the hash table by key.
        input: key (str)
        output: associated value (*)
        """
        hash_ = self._hash_key(key)
        for i, item in enumerate(self.hashtable[hash_]):
            # why enumerate as we don't really use i?
            if item[0] == key:
                return item[1]
        # raise KeyError("Key not in hash table.")
        return False



