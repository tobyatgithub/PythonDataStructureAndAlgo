import sys

sys.path.append(
    "/Users/toby/Documents/PythonWorks/Python_data_structure_and_algo")

from data_structures._Heap import _Heap


def heapSort(array, DEBUG=False):
    heap = _Heap(DEBUG=DEBUG)
    LEN = len(array)
    output = []

    if DEBUG:
        print(f"Input array = {array}.")

    # init: build-max-heap
    print("BUILD MAX HEAP")
    heapified = heap.buildMaxHeap(array)
    print("BUILD MAX HEAP FINISHED, result = ", heapified, end="\n\n")
    heap.DEBUG = False  # no longer wanna see that

    for i in range(LEN - 1, -1, -1):  # len-1, ..., 1
        heapified[i], heapified[0] = heapified[0], heapified[i]
        output.append(heapified.pop(-1))
        heap.maxHeapify(heapified, 0)
        if DEBUG:
            print("By the end of the loop, A = ",
                  heapified,
                  ", output list = ",
                  output,
                  end="\n\n")
    return output[::-1]


array = [5, 2, 1, 7, 6, 3, 4]
test = heapSort(array, True)
print(test)

# array = [3, 9, 2, 1, 4, 5]
# test = heapSort(array, True)
# print(test)