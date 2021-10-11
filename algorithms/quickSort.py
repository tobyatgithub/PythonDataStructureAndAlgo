DEBUG = True


def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    if DEBUG:
        print(f"Init partition, pivot={pivot}, i={i}, A={A}, p={p}, r={r}")
    for j in range(p, r):
        if DEBUG:
            print(f"LOOP: j={j}, A={A}.")
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            if DEBUG:
                print(
                    f"Swap for j={j}, i={i}, where A[i]={A[i]} and A[j]={A[j]}. "
                    + f"A={A} after the swap."
                )
        else:
            if DEBUG:
                print(f"No swap for j={j}, A[j]={A[j]}, continue.")
    A[i + 1], A[r] = A[r], A[i + 1]
    if DEBUG:
        print(f"Last swap, we switch A[r]={A[r]} and A[i+1]={A[i+1]}.")
        print(f"We end up with list A={A}, return i+1={i+1}.\n")
    return i + 1


def test_partition(A, p, r):
    tmp = partition(A, p, r)


# array = [2, 8, 7, 1, 3, 5, 6, 4]
# array = [3, 1, 5, 7, 6, 2, 4]
# test_partition(array, 0, len(array) - 1)


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


array = [3, 1, 5, 7, 6, 2, 4]
quickSort(array, 0, len(array) - 1)

