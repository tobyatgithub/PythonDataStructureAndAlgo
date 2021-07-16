"""
In this file, we make a simple implementation of binary
tree.
"""
import collections


class TreeNode:
    def __init___(self, value=0):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left } and right = { self.right }'
        return out

    def __repr__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left }'
        f'and right = { self.right }'
        return out


class binary_tree:
    def __init__(self, iterable=[]):
        self.root = None
        self.index = 0
        if iterable:
            if isinstance(iterable, collections.Iterable):
                for i in iterable:
                    self.insert(i)
            else:
                raise TypeError('Binary_tree class takes None or Iterable \
                input, got {}'.format(type(iterable)))

    def __str__(self):
        out = f'This is a binay tree with root = { self.root.val }'
        return out

    def __repr__(self):
        out = f'This is a binay tree with root = { self.root.val }'
        return out

    def insert(self, value=0):
        pass
        # I just notice that...most implementation online
        # about binary tree is actually BST...
        # which is easier to implement insert
        # otherwise...shall we keep an index to keep track of
        # insertion?
