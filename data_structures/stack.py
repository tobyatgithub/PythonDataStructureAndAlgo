from node import Node

class Stack(object):
    """
    Stack is a classic data stucture built upon Node. It follows the FILO rule such that
    the first input element shall be the last one out. Like a stack of books.
    """

    def __init__(self, iterable=[]):
        """
        """
        # be careful about the init value
        self.top = None
        self._size = 0

        # if not iterable:
        #     iterable = []

        if isinstance(iterable, list):
            for i in iterable:
                self.push(i)
        else:
            raise TypeError("Stack only take <None> or a <list> as input init value")


    def __len__(self):
        return self._size

    def __str__(self):
        output = f'This is a Stack with top node = { self.top } .'
        return output

    def __repr__(self):
        output = f'This is a Stack with top node = { self.top } .'
        return output

    def push(self, val):
        """
        This function takes any value as an argument and adds that
        value to the top of the stack with an O(1) Time performance
        input: the element you want to pyt on the top of the stack (*)
        """
        new_top = Node(val)
        new_top._next = self.top
        self.top = new_top
        self._size += 1


    def pop(self):
        """
        This function takes no arguments and removes / returns the
        Node at the top of the stack
        output: the element at the top of the stack (Node or None)
        """
        output = self.top

        # in the Stack is not empty
        if output:
            # different case when we only have one element in the stack
            if output._next:
                new_top = output._next
                self.top = new_top
            else:
                self.top = None

            self._size -= 1
            output._next = None

        # if Stack is empty, just return None

        return output

    def peek(self):
        """
        This function takes no arguments and returns the Node at the top of the stack.
        Notice that, different from push, peek doesn't remove that element from the stack.
        output: the element at the top of the stack (Node or None)
        """
        return self.top
