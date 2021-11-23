import numpy as np
import math
import copy


def floydWarshall(matrix):
    N_ROWS = len(matrix)
    D_prev = copy.deepcopy(matrix)

    for k in range(N_ROWS):
        D_cur = np.zeros((N_ROWS, N_ROWS))
        for i in range(N_ROWS):
            for j in range(N_ROWS):
                D_cur[i][j] = min(D_prev[i][j], D_prev[i][k] + D_prev[k][j])
        print("We update the matrix to: \n", D_cur, "\n")
        D_prev = D_cur
    return D_cur


m = np.array([[0, 3, math.inf, 4], [4, 0, math.inf, -2],
              [2, math.inf, 0, math.inf], [math.inf, math.inf, -1, 0]])
print("initial matrix = \n", m, "\n")

res_m = floydWarshall(m)
print(res_m)
print("==" * 20)
print(floydWarshall(res_m))

# def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]],
#                         queries: List[List[int]]) -> List[bool]:
# def checkIfPrerequisite(numCourses, prerequisites, queries):
#     matrix = np.ones((numCourses, numCourses)) * np.inf

#     for pair in prerequisites:
#         pre, cur = pair
#         matrix[pre][cur] = 1

#     D_prev = copy.deepcopy(matrix)
#     # print(D_prev)

#     for k in range(numCourses):
#         D_cur = np.zeros((numCourses, numCourses))
#         for i in range(numCourses):
#             for j in range(numCourses):
#                 D_cur[i][j] = min(D_prev[i][j], D_prev[i][k] + D_prev[k][j])
#         # print("We update the matrix to: \n", D_cur, "\n")
#         D_prev = D_cur

#     # print(D_cur)
#     res = []
#     for q in queries:
#         pre, cur = q
#         res.append(D_cur[pre][cur] < np.inf)
#     return res

# numCourses = 5
# prereq = [[0, 1], [1, 2], [2, 3], [3, 4]]
# query = [[0, 4], [4, 0], [1, 3], [3, 0]]
# print(checkIfPrerequisite(numCourses, prereq, query))