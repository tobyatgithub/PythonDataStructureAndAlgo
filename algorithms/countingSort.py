"""
Refer to <Introduction to Algorithms 3rd edition> 
Chapter 8. Sorting in Linear time -> 8.2 Counting sort.
"""


def countingSort(A, B, k, demo=False):
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
    if demo:
        print(f"Step 1: intput = {A}. init an empty C array for 0,...,k: {C}")

    # counting
    for num in A:
        C[num] += 1
    if demo:
        print(f"Step 2: counting the frequency of each occurance C = {C}")

    for i in range(1, k + 1):  # to include i = k
        C[i] += C[i - 1]
    if demo:
        print(
            f"Step 3: make C[i] means the number of elements less than or equal to i = {C} "
        )

    if demo:
        print("Step 4: now we start reordering based on info from array C.")
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
        if demo:
            print(
                f"j = {j}, A[j] = {A[j]}, C[A[j]] = {C[A[j]] + 1}. "
                + f"Subtract C[A[j]] by 1 and update C->{C}"
            )
            print(f"We swap that A[j] = {A[j]} into B, and change B to: {B}")

    if demo:
        print(f"Finished: A = {A}, B = {B}, C={C}.")
    return


# array = [2, 5, 3, 0, 2, 3, 0, 3]
# array = [6, 5, 4, 3, 2, 1, 0]
array = [4, 5, 0, 1, 3, 4, 3, 4, 3, 0, 3]
save = [0 for _ in range(len(array))]
k = max(array)
countingSort(array, save, k, True)

print(array, save)
