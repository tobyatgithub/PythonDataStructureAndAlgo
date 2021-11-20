import random
import math
import numpy
import matplotlib.pyplot as plt
import keyboard

RANGE_X = 30
RANGE_Y = 30

PAUSE = 0.8
PAUSE_SLOW = 3
PAUSE_FAST = 0.5


#define a function to distinguish the distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


#define a function to get a series of random points in the range.
def get_point_list(number):
    point_list = []
    for i in range(number):
        random_pair = [random.randint(0, RANGE_X), random.randint(0, RANGE_Y)]
        if random_pair not in point_list:
            point_list.append(random_pair)
    return point_list


#sort the point list with the rule of (1) find the point with the lowest y position as the first element
#(2) For other points, the order is with the angle of the vector of (first point, i point) with x axix.
#need to notice that there can be only one lowest point, if there are two or more points with same y pos which is the lowest,
#We will forcely make their y pos a little bigger
def sort_points(points):
    points.sort(key=lambda y: y[1])
    curr_index = 1
    if len(points) < 2:
        return points
    # while (points[curr_index][1] == points[0][1]):
    #     points[curr_index][1] += 1
    points[1:] = sorted(points[1:],
                        key=lambda x:
                        ((-round(((x[0] - points[0][0]) / distance(
                            x, points[0])), 5)), -distance(x, points[0])))

    print("points = ", points)
    return points


#define a function to create a vector for two pointers
def vector(start, end):

    return [end[0] - start[0], end[1] - start[1]]


#Define graham_scan function
def graham_scan(points):
    xlist = sorted([_[0] for _ in points])
    ylist = sorted([_[1] for _ in points])
    print(xlist)
    plt.axis([xlist[0] - 1, xlist[-1] + 1, ylist[0] - 1, ylist[-1] + 1])
    plt.ion()
    points = sort_points(points)

    for i in points:
        plt.scatter(i[0], i[1])
        plt.pause(0.3)
    if len(points) < 2:
        return points

    # while True:
    #     if keyboard.read_key() == "q":
    #         break

    stack = [points[0]]

    for i in range(1, len(points)):
        if len(stack) == 1:
            stack.append(points[i])
            print(f" stack1: {stack[-2]}, stack2: {stack[-1]}")
            plt.plot((stack[-2][0], stack[-1][0]),
                     (stack[-2][1], stack[-1][1]))
            plt.pause(0.1)
            continue
        former_vector = vector(stack[-2], stack[-1])

        now_vector = vector(stack[-1], points[i])
        while numpy.cross(former_vector, now_vector) < 0:
            stack.pop()
            if len(stack) < 2:
                break
            former_vector = vector(stack[-2], stack[-1])
            now_vector = vector(stack[-1], points[i])

        stack.append(points[i])
        print(f"i={i}, stack1: {stack[-2]}, stack2: {stack[-1]}")
        x1, y1 = stack[-2]
        x2, y2 = stack[-1]
        print(x1, x2, y1, y2)
        plt.plot((x1, x2), (y1, y2))
        plt.pause(0.2)

    print(stack)
    plt.plot((stack[0][0], stack[-1][0]), (stack[0][1], stack[-1][1]))
    plt.pause(PAUSE)

    while True:
        if keyboard.read_key() == "q":
            break
        else:
            plt.pause(PAUSE)

    result_x = [_[0] for _ in stack]
    result_y = [_[1] for _ in stack]

    print("test")
    plt.plot(result_x, result_y, color="red")
    plt.plot((stack[0][0], stack[-1][0]), (stack[0][1], stack[-1][1]),
             color="red")

    while True:
        plt.pause(PAUSE)

    return stack


#Two tests from web, maybe need more tests in the future.

#https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
# input_test1 = [(0, 0), (0, 3), (1, 2), (1, 1), (2, 2), (3, 3), (4, 4), (3, 1)]
# print(graham_scan(input_test1))

#https://www.tutorialspoint.com/Graham-Scan-Algorithm
# input_test2 = [(-7,8), (-4,6), (2,6), (6,4), (8,6), (7,-2), (4,-6), (8,-7),(0,0), (3,-2),(6,-10),(0,-6),(-9,-5),(-8,-2),(-8,0),(-10,3), (-2,2),(-10,4)]
# output = graham_scan(input_test2)

input_test3 = [[3, 7], [6, 8], [7, 8], [11, 10], [4, 3], [8, 5], [7, 13],
               [4, 13]]
output = graham_scan(input_test3)

#random_test = get_point_list(50)
#output = graham_scan(random_test)