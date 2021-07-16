from node import Node


class linked_list(object):
    """
    A Linked List is a sequence of Nodes that are connected/linked to each other.
    The most defining feature of a linked List is that each Node references the
    next Node in the link.
    """

    def __init__(self, iterable = []):
        # iterable allows you to pass in a list
        self.head = None
        self._size = 0

        # iterable has to be a list (or at least immutable),
        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for i in iterable:
            self.insert(i)

    def __str__(self):
        output = f'Linked List: Head val - { self.head }'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - { self.head }, size - { self._size }>'
        return output

    def __len__(self):
        return self._size

    def insert(self, val):
        """
        This function takes any value as input and add this value as a node instance
        into the head location of the linked list, and make this new insertion the new
        head.
        input: value, can be in any type (*)
        output: update the linked list inplace. (self.head, self._size)
        """
        # val can be any value as Node has no restriction on what data it takes in.
        # if isinstance(val, int):
        #     new_node = Node(val)
        if isinstance(val, Node):
            new_node = val
        else:
            new_node = Node(val)
        # new_node = val
        new_node._next = self.head
        self.head = new_node

        # self.head = Node(val, self.head)

        self._size += 1
        # return

    def includes(self, target):
        """
        This function takes any value as an argument and returns True or False
        depending on whether that value exists as a Node value within the list.
        input: a target value, could be anything (*)
        output: True of False whether this linkedlist contain this target value (boolean)
        """

        # if the linked list is empty, there won't be any value
        # notice you need to create a new varabile to point to self.head instead of
        # modifying self.head (set self.head = self.head._next in while loop will ops
        # the structure and make ll useless.)
        current = self.head
        while current:
            if target == current.val:
                return True
            current = current._next
        return False


    def append(self, value):
        """
        addes a new node with the given value to the end of the linked list.
        input: a value to add into the linked list. Any datatype shall be fine. (*)
        output: None. as it changes inplace (on the self).
        """
        node_to_add = Node(value)

        # case 1, current ll is empty
        if self.head is None:
            self.head = node_to_add
            self._size += 1
            return

        # otherwise, we traverse to the end of the linked list, and add
        current = self.head
        while current._next:
            current = current._next
        current._next = node_to_add
        self._size += 1
        return

    def insertBefore(self, target_value, new_value):
        """
        this function adds a new node with the given new_value and insert it before the first
        node with target_value.
        input1: a target_value to look upto in the linked list. any datatype shall be fine (*)
        input2: a new_value to add into the linked list. any datatype shall be fine (*)
        output: None. as it changes inplace (on the self).
        """
        node_to_add = Node(new_value)

        # make sure the linked list contains the value we want to find
        if self.includes(target_value) is False:
            print(f'Target value { target_value } not found in the linked list.')
            return

        current = self.head
        # case 1, self.head.val == target_val
        if current.val == target_value:
            node_to_add._next = current
            self.head = node_to_add
            self._size += 1
            return

        # else cases:
        while current._next.val != target_value:
            current = current._next

        node_to_add._next = current._next
        current._next = node_to_add
        self._size += 1
        return


    def insertAfter(self, target_value, new_value):
        """
        this function adds a new node with the given new_value and insert it after the first
        node with target_value.
        input1: a target_value to look upto in the linked list. any datatype shall be fine (*)
        input2: a new_value to add into the linked list. any datatype shall be fine (*)
        output: None. as it changes inplace (on the self).
        """
        node_to_add = Node(new_value)

        # make sure the linked list contains the value we want to find
        if self.includes(target_value) is False:
            print(f'Target value { target_value } not found in the linked list.')
            return

        current = self.head

        while current.val != target_value:
            current = current._next

        # case 1, if the target value is the last value in the ll
        # the current._next shall be None and thus it shall be fine.

        # else cases
        node_to_add._next = current._next
        current._next = node_to_add
        self._size += 1
        return

    def delete_node(self, target_value):
        """
        this function removes the first node contains the given value from the linked list.
        intput: a target_value to remove from the linked list. any datatype shall be fine (*)
        output: None. as it changes inplace (on the self).
        """
        # make sure the linked list contains the value we want to remove
        # this shall also take care of the empty input case
        if self.includes(target_value) is False:
            print(f'Target value { target_value } not found in the linked list.')
            return

        current = self.head

        # case1, head == target value we want to remove.
        if current.val == target_value:
            self.head = self.head._next
            self._size -= 1
            return

        # else cases:
        while current._next.val != target_value:
            current = current._next

        current._next = current._next._next
        self._size -= 1
        return

    def ll_kth_from_end(self, k):
        """
        This function takes a number, k, as a parameter. Return the node’s value
        that is k from the end of the linked list.
        input: k (int)
        output: node's value of k from the end of the linked list (int)
            or 'Exception' if k is out of range (str)
        """
        if not isinstance(k, int):
            print("please input an integer k.")
            return 'Exception'

        if k < 1:
            print("please input a positive integer k.")
            return 'Exception'

        current = self.head
        if current is None:
            return 'Exception'

        position = self.head

        # here we set position to be (k-1) from current
        for _ in range(k-1):
            if position._next is not None:
                position = position._next
            else:
                return 'Exception'

        while position._next is not None:
            current = current._next
            position = position._next

        return current.val

