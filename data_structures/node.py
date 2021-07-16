class Node(object):
    """
    """

    def __init__(self, val = None, _next = None):
        # we use _next bcz next is a globally defined function,
        # we use an _ to differentiate.
        """
        """
        self.val = val
        self._next = _next

    def __str__(self):
        output = f'{ self.val }'
        return output
        # return self.val

    def __repr__(self):
        output = f'< This Node has value = { self.val }, _next - { self._next }>'
        output = f'{ self.val }'
        return output
        # return self.val
