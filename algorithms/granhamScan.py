"""
Here we write the code for granham scan, and
then we try to solve leetcode 587.
"""
import numpy as np
import matplotlib.pyplot as plt

DEBUG = True


def plotAllPoints(in_array):
    Xs = [_[0] for _ in in_array]
    Ys = [_[1] for _ in in_array]
    plt.scatter(Xs, Ys)
    for i in range(len(Xs)):
        plt.text(Xs[i] + 0.2, Ys[i] - 0.2, f"({Xs[i]}, {Ys[i]})")
    plt.show()


def showDifference(output, expected):
    if len(output) > len(expected):
        longer = output
        shorter = expected
        print("Output is longer than expected!")
    else:
        longer = expected
        shorter = output
        print("Output is shorter than expected!")

    res = []
    for element in longer:
        if element not in shorter:
            res.append(element)
    return res


def calculateDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculateCosine(point, origin):
    """
    calculate the polar angle of the given point to the origin point
    """
    x1, y1 = point
    x0, y0 = origin
    if y1 == y0:
        return 1.0
    return (x1 - x0) / calculateDistance(point, origin)


def granhamScan(in_array):
    """
    Input: a list of tuples [(x1, y1), (x2, y2), (x3, y3), ...]
    Output: a list of tuples indicating the boundary points.
    """
    # step 1: find origin
    sorted_origin = sorted(in_array, key=lambda x: (x[1], x[0]))
    origin = sorted_origin[0]
    if DEBUG:
        print(f"origin point = {origin}.")
    # step 2: sort the remaining array other than the origin point
    remaining_points = sorted(
        sorted_origin[1:],
        key=lambda x: (-calculateCosine(x, origin), -calculateDistance(x, origin)),
    )

    if DEBUG:
        print(f"sorted remaining list = {remaining_points}")
    # cosine is a decreasing function from 0 to pi, thus negative sign
    # and we want the fartherest distance if same angle, thus the negative sign.

    # step 3: managing the stack to find our final results.
    stack = []
    stack.append(origin)
    stack.append(remaining_points[0])
    stack.append(remaining_points[1])
    if DEBUG:
        print(f"stack initialized = {stack}.")
    for i in range(2, len(remaining_points)):
        while True:
            cur_point = remaining_points[i]
            old_vector = [stack[-1][0] - stack[-2][0], stack[-1][1] - stack[-2][1]]
            new_vector = [cur_point[0] - stack[-1][0], cur_point[1] - stack[-1][1]]
            if np.cross(old_vector, new_vector) < 0:  # neg cross = clock-wise
                stack.pop(-1)
                if DEBUG:
                    print(
                        f"clock wise, we pop current point = {cur_point}, and stack becomes = {stack}"
                    )
            else:
                stack.append(cur_point)
                if DEBUG:
                    print(
                        f"counter clock wise, good, we add and stack becomes = {stack}"
                    )
                break

    return stack


# # test
# array = [(0, 0), (0, 3), (1, 2), (1, 1), (2, 2), (3, 3), (4, 4), (3, 1)]
# print(granhamScan(array))

# array = [[1, 2], [2, 2], [4, 2]]
# print(granhamScan(array))

# array = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
# print(granhamScan(array))

array = [
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 1],
    [7, 2],
    [7, 3],
    [7, 4],
    [6, 5],
    [5, 5],
    [4, 5],
    [3, 5],
    [2, 5],
    [1, 4],
    [1, 3],
    [1, 2],
    [2, 1],
    [4, 2],
    [0, 3],
]

print(granhamScan(array))

print(
    showDifference(
        [
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 1],
            [7, 2],
            [7, 3],
            [7, 4],
            [6, 5],
            [5, 5],
            [4, 5],
            [3, 5],
            [2, 5],
            [1, 4],
            [0, 3],
        ],
        [
            [7, 4],
            [3, 0],
            [1, 2],
            [2, 5],
            [5, 5],
            [4, 5],
            [1, 4],
            [2, 1],
            [3, 5],
            [0, 3],
            [6, 5],
            [7, 2],
            [7, 3],
            [4, 0],
            [5, 0],
            [6, 1],
        ],
    )
)
plotAllPoints(array)
