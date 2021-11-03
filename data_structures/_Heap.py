"""
In this file, we make a simple implementation of heap data structure.
Surprisingly, we don't use a tree structure or node here.
We can do it simply with array.
"""


class _Heap(object):
    def __init__(self, DEBUG=False):
        self.DEBUG = DEBUG
        pass

    def buildMaxHeap(self, A):
        n = int(len(A) // 2) - 1  # -1 for 0 indexing
        for i in range(n, -1, -1):
            A = self.maxHeapify(A, i)
        return A

    def maxHeapify(self, A, k):
        l = 2 * k + 1
        r = 2 * k + 2

        if l < len(A) and A[l] > A[k]:
            largest = l
        else:
            largest = k
        if r < len(A) and A[r] > A[largest]:
            largest = r

        if self.DEBUG:
            print(f"Performing maxHeapify on arrary A = {A}, with k = {k}," +
                  f" and A[k] = {A[k] if len(A) > 0 else []}.")

        if largest != k:
            A[k], A[largest] = A[largest], A[k]
            if self.DEBUG:
                print(
                    f"Performing maxHeapify swap: l = {l}, r = {r}, largest = {largest}."
                    + f"Result A = {A}",
                    end="\n\n")
            self.maxHeapify(A, largest)
        else:
            if self.DEBUG:
                print("No swap needed.", end="\n\n")
        return A


# array = [3, 9, 2, 1, 4, 5]
# test = _Heap(DEBUG=True).maxHeapify(array, 0)
# print(test)

array = [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15]
test = _Heap(DEBUG=True).buildMaxHeap(array)
print(f"A = {test}")

# class maxHeap(object):
#     """
#     """
#     def __init__(self, A, DEBUG=False):
#         self.A = A
#         self.LEN = len(self.A)
#         self.DEBUG = DEBUG
#         self.buildMaxHeap()

#     def buildMaxHeap(self):
#         n = int(self.LEN // 2) - 1
#         for i in range(n, -1, -1):
#             self.maxHeapify(i)

#     def getLeftIndex(self, k):
#         return 2 * k + 1

#     def getRightIndex(self, k):
#         return 2 * k + 2

#     def getArray(self):
#         return self.A

#     def maxHeapify(self, k):
#         l = self.getLeftIndex(k)
#         r = self.getRightIndex(k)

#         if l < self.LEN and self.A[l] > self.A[k]:
#             largest = l
#         else:
#             largest = k
#         if r < self.LEN and self.A[r] > self.A[largest]:
#             largest = r

#         if self.DEBUG:
#             print(f"maxHeapify: k = {k}, A[k] = {self.A[k]}, A = {self.A}.")
#             print(f"maxHeapify: l = {l}, r = {r}, largest = {largest}")
#             # import pdb
#             # pdb.set_trace()
#         if largest != k:
#             self.A[k], self.A[largest] = self.A[largest], self.A[k]
#             self.maxHeapify(largest)

#     def __str__(self):
#         return str(self.A)

# array = [3, 9, 2, 1, 4, 5]
# test = maxHeap(array, True)
# print(test)
