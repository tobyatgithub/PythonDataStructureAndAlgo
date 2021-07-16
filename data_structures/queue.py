from node import Node

class Queue(object):
    """
    Queue is a classic data structure built upon Node. It follows the FIFO rule, such that
    the first element in shall be the first one out. Like a queue in line.
    """

    def __init__(self, iterable = []):
        self.front = None
        self.back = None
        self._size = 0

        if isinstance(iterable, list):
            for i in iterable:
                self.enqueue(i)
        else:
            raise TypeError(f'Queue only take <None> or a <list> as input init value, but \n{ type(iterable) } given')

    def __len__(self):
        return self._size

    def __str__(self):
        output = f'This is a Queue with front = { self.front }, and back = { self.back }.'
        return output

    def __repr__(self):
        output = f'This is a Queue with front = { self.front }, and back = { self.back }.'
        return output

    def enqueue(self, value):
        """
        takes any value as an argument and adds that value to the back of
        the queue with an O(1) Time performance
        input: the element to put at the end of the queue (*)
        """
        new_node = Node(value)

        # empty queue situation
        if (self.front is None) and (self.back is None):
            self.front = new_node
            self.back = new_node

        else:
            current = self.back
            current._next = new_node
            self.back = new_node

        self._size += 1

    def dequeue(self):
        """
        This function takes no arguments and removes / returns the Node at the front of the queue
        output: remove the first element from the queue and return that element as a node (Node or None)
        """
        current = self.front

        # queue not empty
        if current:
            son_node = current._next
            self.front = son_node
            current._next = None
            self._size -= 1

        # else: # no need
        #     current._next = None
        return current


    def peek(self):
        """
        This function return the first element in the queue.
        output: first element in the queue (Node or None)
        """
        return self.front
