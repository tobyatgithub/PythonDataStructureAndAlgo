"""
Similar to maxheap, here we have a class for min heap.
Implementing via array
"""


class minHeap():
    def __init__(self, A, DEBUG=False):
        self.A = A
        self.LEN = len(A)
        self.DEBUG = DEBUG
        self.buildMinHeap()

    def getLeftIndex(self, k):
        return 2 * k + 1

    def getRightIndex(self, k):
        return 2 * k + 2

    def minHeapify(self, k):
        l = self.getLeftIndex(k)
        r = self.getRightIndex(k)

        if l < self.LEN and self.A[l] < self.A[k]:
            smallest = l
        else:
            smallest = k
        if r < self.LEN and self.A[r] < self.A[smallest]:
            smallest = r

        if self.DEBUG:
            print(f"minHeapify: k = {k}, A[k] = {self.A[k]}, A = {self.A}.")
            print(f"minHeapify: l = {l}, r = {r}, smallest = {smallest}.")

        if k != smallest:
            self.A[k], self.A[smallest] = self.A[smallest], self.A[k]
            self.minHeapify(smallest)

    def buildMinHeap(self):
        n = int(self.LEN // 2) - 1
        for i in range(n, -1, -1):
            self.minHeapify(i)

    def __str__(self):
        return str(self.A)


array = [3, 9, 2, 1, 4, 5]
test = minHeap(array, True)
print(test)