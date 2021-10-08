"""
In this file, we make a simple implementation of heap data structure.
Surprisingly, we don't use a tree structure or node here.
We can do it simply with array.
"""


class maxHeap():
    """
    """
    def __init__(self, A, DEBUG=False):
        self.A = A
        self.LEN = len(self.A)
        self.DEBUG = DEBUG
        self.buildMaxHeap()

    def buildMaxHeap(self):
        n = int(self.LEN // 2) - 1
        for i in range(n, -1, -1):
            self.maxHeapify(i)

    def getLeftIndex(self, k):
        return 2 * k + 1

    def getRightIndex(self, k):
        return 2 * k + 2

    def maxHeapify(self, k):
        l = self.getLeftIndex(k)
        r = self.getRightIndex(k)

        if l < self.LEN and self.A[l] > self.A[k]:
            largest = l
        else:
            largest = k
        if r < self.LEN and self.A[r] > self.A[largest]:
            largest = r

        if self.DEBUG:
            print(f"maxHeapify: k = {k}, A[k] = {self.A[k]}, A = {self.A}.")
            print(f"maxHeapify: l = {l}, r = {r}, largest = {largest}")
            # import pdb
            # pdb.set_trace()
        if largest != k:
            self.A[k], self.A[largest] = self.A[largest], self.A[k]
            self.maxHeapify(largest)

    def __str__(self):
        return str(self.A)


array = [3, 9, 2, 1, 4, 5]
test = maxHeap(array, True)
print(test)
