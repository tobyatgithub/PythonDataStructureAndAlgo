class binaryNode():
    """
    This is a node where you will have two child by default -> one on left and one on right.
    """
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        output = f"binaryNode:[val = {val}; left = {left}; right = {right}]"
        return output

    def __repr__(self)
        output = f"binaryNode:[val = {val}"
        if self.left:
            output += " left=Yes;"
        if self.right:
            output += " right=Yes."
        return output