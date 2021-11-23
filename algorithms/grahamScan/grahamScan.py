"""
Here we write the code for graham scan, and
then we try to solve leetcode 587.
"""
import numpy as np
import matplotlib.pyplot as plt

DEBUG = True
ROUND = 8
MULTIPLYER = 1000


def calculateDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return round(np.sqrt((x1 - x2)**2 + (y1 - y2)**2), ROUND)


def calculateCosine(point, origin):
    """
    calculate the polar angle of the given point to the origin point
    """
    x1, y1 = point
    x0, y0 = origin
    if y1 == y0:
        return 1.0
    return round((x1 - x0) / calculateDistance(point, origin), ROUND)


def countNumberOfSameCosine(in_array, origin):
    cosValue = calculateCosine(in_array[0], origin)
    count = 0
    for element in in_array:
        if calculateCosine(element, origin) == cosValue:
            count += 1
    return count


def grahamScan(in_array):
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

    third: shall do the same cos after the second sort.

    forth: well, it turns out that if points are getting too 
    close to each other. the precision gonna be a big issue.
    let's try whether the multiplyer can solve this.
    """
    if len(in_array) <= 1:
        return in_array

    # patch4 - step 0:
    in_array = [
        tuple([_[0] * MULTIPLYER, _[1] * MULTIPLYER]) for _ in in_array
    ]
    # step 1: find origin
    sorted_origin = sorted(in_array, key=lambda x: (x[1], x[0]))
    origin = sorted_origin[0]
    # num = countNumberOfSameY(sorted_origin, origin[1])
    if DEBUG:
        print(f"origin point = {origin}.")
        print(f"sorted origin list = {sorted_origin}")
    # step 2: sort the remaining array other than the origin point
    remaining_points = sorted(
        sorted_origin[1:],
        key=lambda x:
        (-calculateCosine(x, origin), -calculateDistance(x, origin)),
    )
    num = countNumberOfSameCosine(remaining_points, origin)

    # third patch: now we fix to the correct order.
    first_part = remaining_points[:num]
    second_part = remaining_points[num:]
    combined_points = ([origin] + sorted(
        first_part, key=lambda x: calculateDistance(x, origin)) + second_part)

    assert len(combined_points) == len(in_array)
    if DEBUG:
        print(f"Amount of same cos value = {num}.")
        print(f"sorted remaining list = {remaining_points}")
        print(f"final combined list = {combined_points}")
    # cosine is a decreasing function from 0 to pi, thus negative sign
    # and we want the fartherest distance if same angle, thus the negative sign.

    # step 3: managing the stack to find our final results.
    stack = combined_points[:3]
    if DEBUG:
        print(f"stack initialized = {stack}.")
    for i in range(3, len(combined_points)):
        while True:
            cur_point = combined_points[i]
            old_vector = [
                stack[-1][0] - stack[-2][0], stack[-1][1] - stack[-2][1]
            ]
            new_vector = [
                cur_point[0] - stack[-1][0], cur_point[1] - stack[-1][1]
            ]
            if np.cross(old_vector, new_vector) < 0:  # neg cross = clock-wise
                if DEBUG:
                    print(
                        f"clock wise, current point = {cur_point}, we pop value = {stack[-1]} out from stack."
                    )
                    print(
                        f"current last 5 elements of the stack = {stack[-5:]}")
                stack.pop(-1)
            else:
                stack.append(cur_point)
                if DEBUG:
                    print(
                        f"counter clock wise, good, we add current point = {cur_point}"
                    )
                    print(
                        f"current last 5 elements of the stack = {stack[-5:]}")
                break

    # patch4: step last, before output, we need to scale back
    stack = [
        tuple([int(_[0] / MULTIPLYER),
               int(_[1] / MULTIPLYER)]) for _ in stack
    ]
    return stack


# # test
# array = [(0, 0), (0, 3), (1, 2), (1, 1), (2, 2), (3, 3), (4, 4), (3, 1)]
# print(grahamScan(array))

# array = [[1, 2], [2, 2], [4, 2]]
# print(grahamScan(array))


def readNumbersFromFile(file_address):
    with open(file_address) as f:
        res = []
        for line in f:
            contents = line.split("],[")
            contents = [_.replace("[", "").replace("]", "") for _ in contents]
            # import pdb

            # pdb.set_trace()
            for element in contents:
                num1, num2 = element.split(",")
                res.append(tuple([int(num1), int(num2)]))
    return res


array = readNumbersFromFile("grahamLargeInput3.txt")
output = grahamScan(array)
print("final result = ", output)
expected = readNumbersFromFile("grahamLargeExpected3.txt")

diff = showDifference(output, expected)
print(diff[0], "hum0")
print(diff[1], "hum1")

# plotAllPoints(array)


def plotAllPoints(in_array):
    Xs = [_[0] * 10 for _ in in_array]
    Ys = [_[1] * 10 for _ in in_array]
    plt.scatter(Xs, Ys)
    for i in range(len(Xs)):
        plt.text(Xs[i] + 0.1, Ys[i] - 0.1, f"({Xs[i]}, {Ys[i]})")
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
        longer = output
        shorter = expected
    longer_res = set()
    for element in longer:
        if element not in shorter:
            longer_res.add(tuple(element))

    shorter_res = set()
    for element in shorter:
        if element not in longer:
            shorter_res.add(tuple(element))
    return longer_res, shorter_res


# test show difference
# print(showDifference([(1, 1), (1, 2)], [(2, 2), (3, 3), (1, 1)]))
# print(showDifference([[1, 1], [1, 2]], [[2, 2], [3, 3], [1, 1]]))

# def countNumberOfSameY(in_array, y):
#     count = 0
#     for element in in_array:
#         if element[1] == y:
#             count += 1
# return count