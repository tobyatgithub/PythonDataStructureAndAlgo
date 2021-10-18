# cache = {}  # key = (r, s)


# def winningRate(r, s):
#     """
#     Code for 5800 Problem set 4, Q5-d.
#     We need to use dp to calculate the winning rate of a game, where:
#     r: int = remaining round of game
#     s: int = current score

#     The game contains two choices, flip coin X or coin Y, both are fair coins.
#     Wining X = +1, losing X = -1, winning Y = +3, losing Y = -3.
#     Our goal in part d is to find p_100(0)
#     """

#     def rec(r, s):
#         if (r, s) not in cache:
#             if r < 1:
#                 raise (TypeError("r can not be smaller than 1."))
#             if r == 1:
#                 if s <= -3:
#                     cache[(r, s)] = 0
#                     return cache[(r, s)]
#                 if s >= -2 and s <= 1:
#                     cache[(r, s)] = 0.5
#                     return cache[(r, s)]
#                 if s >= 2:
#                     cache[(r, s)] = 1
#                     return cache[(r, s)]

#             cache[(r, s)] = max(
#                 (rec(r - 1, s + 1) + rec(r - 1, s - 1)) / 2,
#                 (rec(r - 1, s + 3) + rec(r - 1, s - 3)) / 2,
#             )
#         return cache[(r, s)]

#     return rec(r, s)


# print(winningRate(100, 0))
# res = [_ for _ in filter(lambda x: x[0] == 1, cache)]
# print(res)


# # print(winningRate(1, 1), 0.5)
# # print(winningRate(1, 0), 0.5)
# # print(winningRate(1, -3), 0)
# for i in range(1, 101):
#     print(f"i = {i}, and winning rate = {winningRate(i, 0)}")


cache = {}


def winningRate2(r, s, X, Y):
    """
    revised version, now we want to investigate how value of X and Y will affect.
    r: int = remaining round of game
    s: int = current score
    X: int = points winning for X-head
    Y: int = points wining for Y-head
    (assuming X and Y are both fair, and we always assume Y > X)
    """
    if X > Y:
        X, Y = Y, X

    def rec(r, s):
        if (r, s) not in cache:
            if r < 1:
                raise (TypeError("r can not be smaller than 1."))
            if r == 1:
                if s <= -Y:  # only Y head for the win.
                    cache[(r, s)] = 0
                    return cache[(r, s)]
                if s >= (-Y + 1) and s <= X:  # play X or Y shall be the same
                    cache[(r, s)] = 0.5
                    return cache[(r, s)]
                if s > X:  # play X, guarenteed win
                    cache[(r, s)] = 1
                    return cache[(r, s)]

            cache[(r, s)] = max(
                (rec(r - 1, s + X) + rec(r - 1, s - X)) / 2,
                (rec(r - 1, s + Y) + rec(r - 1, s - Y)) / 2,
            )
        return cache[(r, s)]

    return rec(r, s)


print(winningRate2(500, 0, 1, 4))
