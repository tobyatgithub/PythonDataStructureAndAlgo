from pprint import pprint

cache = {}  # key = (r, s)


def winningRate(r, s):
    """
    Code for 5800 Problem set 4, Q5-d.
    We need to use dp to calculate the winning rate of a game, where:
    r: int = remaining round of game
    s: int = current score

    The game contains two choices, flip coin X or coin Y, both are fair coins.
    Wining X = +1, losing X = -1, winning Y = +3, losing Y = -3.
    Our goal in part d is to find p_100(0)
    """

    def rec(r, s):
        if (r, s) not in cache:
            if r < 1:
                raise (TypeError("r can not be smaller than 1."))
            if r == 1:
                if s <= -3:
                    cache[(r, s)] = 0
                    return cache[(r, s)]
                if s >= -2 and s <= 1:
                    cache[(r, s)] = 0.5
                    return cache[(r, s)]
                if s >= 2:
                    cache[(r, s)] = 1
                    return cache[(r, s)]

            cache[(r, s)] = max(
                (rec(r - 1, s + 1) + rec(r - 1, s - 1)) / 2,
                (rec(r - 1, s + 3) + rec(r - 1, s - 3)) / 2,
            )
        return cache[(r, s)]

    return rec(r, s)


print(winningRate(100, 0))
# pprint(cache)
res = [_ for _ in filter(lambda x: x[0] == 1, cache)]
print(res)


# print(winningRate(1, 1), 0.5)
# print(winningRate(1, 0), 0.5)
# print(winningRate(1, -3), 0)
# for i in range(-6, 4):
#     print(f"i = {i}, and winning rate = {winningRate(2, i)}")

