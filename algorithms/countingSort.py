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
        print(f"Step 1: intput = {A}. init an empty C array for 0,...,k: {C}\n")

    # counting
    for num in A:
        C[num] += 1
    if demo:
        print(f"Step 2: counting the frequency of each occurance C = {C}\n")

    for i in range(1, k + 1):  # to include i = k
        C[i] += C[i - 1]
    if demo:
        print(
            f"Step 3: make C[i] means the number of elements less than or equal to i = {C} \n"
        )

    if demo:
        print("Step 4: now we start reordering based on info from array C.\n")
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        if demo:
            # latex homework print
            print(
                f"j = {j}, we go find $A[j] = A[{j}] = {A[j]}$. "
                f"And we look up $C[A[j]] = C[{A[j]}] = {C[A[j]]}$. "
                f"This means that there are {C[A[j]]} values less or equal to {A[j]} in the input array. "
                f"We thus put the object $A[j] = A[{j}]] = {A[j]}$ to the correct output position $B[C[A[j]]] = B[{C[A[j]]-1}]$. "
            )
            ## human-read print
            # print(f"dsadas" f"{A}" f"{C}")
            # print(f"We swap that A[j] = {A[j]} into B, and change B to: {B}")

        C[A[j]] -= 1
        if demo:
            print(
                f"We update the output array B to ${B}$. And we subtract $C[A[j]]$ by 1 and update C to ${C}$.\n"
            )

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
