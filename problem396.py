# https://projecteuler.net/problem=396
import numpy as np


def number_to_binary_numpy(n, digits=4): # numpy does not support large ints
    result = [0] * digits
    for i in range(digits):
        result[i] = n % 2
        n = n >> 1
        # print(n)
    return result

# TODO: no protection against underflow
def minus_one(g, digit, base):
    if digit == 0:
        base += 1

    if g[digit] > 0:
        if digit == 0:
            # even uit
            # base += (g[digit] - 1)
            # g[digit] = 0
            g[digit] -= 1
        else:
            if digit == 1:
                value = g[digit] - 1
                for i in range(value):
                    base += base
                g[digit] = 0
            else:
                g[digit] -= 1
    else:
        g, base = minus_one(g, digit + 1, base)
        g[digit] = base - 1
    return g, base

def goodwin(G):
    base = 2
    g = number_to_binary_numpy(G) # start

    while True:
        print(base, g)
        g, base = minus_one(g, 0, base)
        if (sum(g) == 0):
            break

    print(g, base - 2)
    return base - 2

print(goodwin(8))

# total = 0
# for i in range(1, 8):
#     b = goodwin(i)
#     total += b
#     print(b)
#
# print("Total:", total)

# 1, 1
# 2, 3
# 3, 5
# 4, 21
# 5, 61
# 6, 381
# 7, 2045


# 2 [1, 0, 1, 0]
# 3 [0, 0, 1, 0]
# 4 [3, 3, 0, 0]
# 5 [2, 3, 0, 0]
# 6 [1, 3, 0, 0]
# 7 [0, 3, 0, 0]
# 8 [7, 2, 0, 0]
# 9 [6, 2, 0, 0]
# 10 [5, 2, 0, 0]
# 11 [4, 2, 0, 0]
# 12 [3, 2, 0, 0]
# 13 [2, 2, 0, 0]
# 14 [1, 2, 0, 0]
# 15 [0, 2, 0, 0]
# 16 [15, 1, 0, 0]
# 17 [14, 1, 0, 0]
# 18 [13, 1, 0, 0]
# 19 [12, 1, 0, 0]
# 20 [11, 1, 0, 0]
# 21 [10, 1, 0, 0]
# 22 [9, 1, 0, 0]
# 23 [8, 1, 0, 0]
# 24 [7, 1, 0, 0]
# 25 [6, 1, 0, 0]
# 26 [5, 1, 0, 0]
# 27 [4, 1, 0, 0]
# 28 [3, 1, 0, 0]
# 29 [2, 1, 0, 0]
# 30 [1, 1, 0, 0]
# 31 [0, 1, 0, 0]
# 32 [31, 0, 0, 0]
# 33 [30, 0, 0, 0]
# 34 [29, 0, 0, 0]
# 35 [28, 0, 0, 0]
# 36 [27, 0, 0, 0]
# 37 [26, 0, 0, 0]
# 38 [25, 0, 0, 0]
# 39 [24, 0, 0, 0]
# 40 [23, 0, 0, 0]
# 41 [22, 0, 0, 0]
# 42 [21, 0, 0, 0]
# 43 [20, 0, 0, 0]
# 44 [19, 0, 0, 0]
# 45 [18, 0, 0, 0]
# 46 [17, 0, 0, 0]
# 47 [16, 0, 0, 0]
# 48 [15, 0, 0, 0]
# 49 [14, 0, 0, 0]
# 50 [13, 0, 0, 0]
# 51 [12, 0, 0, 0]
# 52 [11, 0, 0, 0]
# 53 [10, 0, 0, 0]
# 54 [9, 0, 0, 0]
# 55 [8, 0, 0, 0]
# 56 [7, 0, 0, 0]
# 57 [6, 0, 0, 0]
# 58 [5, 0, 0, 0]
# 59 [4, 0, 0, 0]
# 60 [3, 0, 0, 0]
# 61 [2, 0, 0, 0]
# 62 [1, 0, 0, 0]
# [0, 0, 0, 0] 61