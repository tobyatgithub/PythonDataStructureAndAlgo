import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left } and right = { self.right }'
        return out

    def __repr__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left }'
        f'and right = { self.right }'
        return out


class BST:
    def __init__(self, iterable=[]):
        self.root = None

        if iterable:
            if isinstance(iterable, collections.Iterable):
                for i in iterable:
                    self.insert(i)
            else:
                raise TypeError(f'BST shall take None or Iterable value as input, { iterable } given')


    def __str__(self):
        out = f'This is a binay search tree with root = { self.root.val }'
        return out

    def __repr__(self):
        out = f'This is a binay search tree with root = { self.root.val }'
        return out

    def insert(self, val):
        """
        """

        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def preOrder(self, root, methodToRun=print):
        """
        """
        if root:
            methodToRun(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root, methodToRun=print):
        """post order = visit the current node after its child nodes"""
        if root:  # if current node not empty
            # 1. check left child exist, if so, go to it
            self.postOrder(root.left)
            # 2. if left child finished, check right child
            self.postOrder(root.right)
            # 3. if both finished, print self.
            methodToRun(root.val)

    def inOrder(self, root, methodToRun=print):
        """in order = print left, node, then right"""
        if root:
            self.inOrder(root.left)
            methodToRun(root.val)
            self.inOrder(root.right)

    def find_maximum_value(self):
        """
        this function takes in a binary tree as input, and return
        the maximum value within the tree as output.
        There are two ways of doing that, one is modify the tree class such that
        we add one .max_val to the self. And modifying the insert process accordingly.
        The other one is to use any kind of traverse to visit every single node in
        the tree, and find out the one with maximum value
        """

        if self.root:
            max_val = self.root.val
            store = [self.root]
            while len(store) > 0:
                cur = store.pop(0)
                if cur.val > max_val:
                    max_val = cur.val
                if cur.right:
                    store.append(cur.right)
                if cur.left:
                    store.append(cur.left)
            return max_val

        print("Empty tree has no maximum value")
        return None



tmp = BST([9,3,4,8])
tmp.inOrder(tmp.root)
