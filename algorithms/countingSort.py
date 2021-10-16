"""
Refer to <Introduction to Algorithms 3rd edition> 
Chapter 8. Sorting in Linear time -> 8.2 Counting sort.
"""


def countingSort(A, B, k):
    """
    Counting sort assumes that each of the n input elements 
    is an integer in the range 0 to k, for some (small) integer k.
    Notice that we will use the variable names in the textbook's
    pseudo code.

    Inputs:
    - A: input array to sort
    - B: holds the sorted output array 
    - k: the max integer of the input array
    """
    # a temporary working storage
    C = [0 for _ in range(k + 1)]

    # counting
    for num in A:
        C[num] += 1

    for i in range(1, k + 1):  # to include i = k
        C[i] += C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        print(f"j = {j}, A[j] = {A[j]}, C[A[j]] = {C[A[j]]}.")
        print(f"A = {A}, B = {B}, C={C}.")
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    print(f"A = {A}, B = {B}, C={C}.")
    return


array = [2, 5, 3, 0, 2, 3, 0, 3]
# array = [6, 5, 4, 3, 2, 1, 0]
save = [0 for _ in range(len(array))]
k = max(array)
countingSort(array, save, k)

print(array, save)
