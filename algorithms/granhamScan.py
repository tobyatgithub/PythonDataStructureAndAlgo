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
    elif len(output) < len(expected):
        longer = expected
        shorter = output
        print("Output is shorter than expected!")
    else:
        print("Output is SAME LEN to expected!")

    res = []
    for element in longer:
        if element not in shorter:
            res.append(element)
    return res


def calculateDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return round(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)


def calculateCosine(point, origin):
    """
    calculate the polar angle of the given point to the origin point
    """
    x1, y1 = point
    x0, y0 = origin
    if y1 == y0:
        return 1.0
    return round((x1 - x0) / calculateDistance(point, origin), 3)


# def countNumberOfSameY(in_array, y):
#     count = 0
#     for element in in_array:
#         if element[1] == y:
#             count += 1
# return count
def countNumberOfSameCosine(in_array, cosValue):
    count = 0
    for element in in_array[1:]:  # need to skip the first point
        if calculateCosine(element, in_array[0]) == cosValue:
            count += 1
    return count


def granhamScan(in_array):
    """
    Input: a list of tuples [(x1, y1), (x2, y2), (x3, y3), ...]
    Output: a list of tuples indicating the boundary points.

    first patch: ok, now there is an issue that in lc 587,
    we want all the points on the boundary. And our current 
    algorithm will likely to miss the ones who have same y
    value as the original point (due to our second sorting).
    first patch idea is that, for the ones who have same y 
    value as the original point, we keep there position in the
    'sorted_origin' list, count the number and only apply the 
    second sort to the elements after them.

    second patch: cool... same Y is not enough, we need find
    all points with same original cosine...
    """
    if len(in_array) <= 1:
        return in_array
    # step 1: find origin
    sorted_origin = sorted(in_array, key=lambda x: (x[1], x[0]))
    origin = sorted_origin[0]
    # num = countNumberOfSameY(sorted_origin, origin[1])
    num = countNumberOfSameCosine(
        sorted_origin, calculateCosine(sorted_origin[1], origin)
    )
    if DEBUG:
        print(f"origin point = {origin}.")
        print(f"sorted origin list = {sorted_origin}")
    # step 2: sort the remaining array other than the origin point
    remaining_points = sorted(
        sorted_origin[num:],
        key=lambda x: (-calculateCosine(x, origin), -calculateDistance(x, origin)),
    )
    combined_points = sorted_origin[:num] + remaining_points
    assert len(combined_points) == len(in_array)
    if DEBUG:
        print(f"sorted remaining list = {remaining_points}")
        print(f"final combined list = {combined_points}")
    # import pdb

    # pdb.set_trace()
    # cosine is a decreasing function from 0 to pi, thus negative sign
    # and we want the fartherest distance if same angle, thus the negative sign.

    # step 3: managing the stack to find our final results.
    stack = combined_points[:3]
    # stack.append(combined_points[0])
    # stack.append(combined_points[1])
    # stack.append(combined_points[2])
    if DEBUG:
        print(f"stack initialized = {stack}.")
    for i in range(3, len(combined_points)):
        while True:
            cur_point = combined_points[i]
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

array = [
    [0, 2],
    [0, 4],
    [0, 5],
    [0, 9],
    [2, 1],
    [2, 2],
    [2, 3],
    [2, 5],
    [3, 1],
    [3, 2],
    [3, 6],
    [3, 9],
    [4, 2],
    [4, 5],
    [5, 8],
    [5, 9],
    [6, 3],
    [7, 9],
    [8, 1],
    [8, 2],
    [8, 5],
    [8, 7],
    [9, 0],
    [9, 1],
    [9, 6],
]
print(granhamScan(array))

print(
    showDifference(
        [
            [9, 0],
            [9, 6],
            [7, 9],
            [5, 9],
            [3, 9],
            [0, 9],
            [0, 5],
            [0, 4],
            [0, 2],
            [2, 1],
        ],
        [
            [0, 4],
            [7, 9],
            [9, 0],
            [9, 1],
            [9, 6],
            [5, 9],
            [3, 9],
            [2, 1],
            [0, 2],
            [0, 5],
            [0, 9],
        ],
    )
)
plotAllPoints(array)
