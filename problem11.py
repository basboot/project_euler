import functools
import math

import numpy as np

file1 = open('problem11.txt', 'r')
lines = file1.readlines()

matrix = []
for line in lines:
    matrix.append([int(x) for x in line.rstrip().split(" ")])

matrix = np.array(matrix)

def find_largest_adjacent(values, n_adjacent):
    largest_product = -math.inf

    if n_adjacent > len(values):
        return -math.inf

    for i in range(len(values) - n_adjacent + 1):
        largest_product = max(largest_product,
                              functools.reduce(lambda a, b: a * b, values[i:i + n_adjacent], 1))

    return largest_product


m, n = matrix.shape
assert m == n, "we assume the matrix is square"

largest = -math.inf

for i in range(m):
    largest = max(largest, find_largest_adjacent(matrix[i, :], 4)) # left right
    largest = max(largest, find_largest_adjacent(matrix[:, i], 4)) # up down
    largest = max(largest, find_largest_adjacent(np.diagonal(matrix, i, 0), 4))  # diag 1
    largest = max(largest, find_largest_adjacent(np.diagonal(np.flip(matrix, 1), i, 0), 4)) # diag 2


print(largest)

# up, down, left, right, diag. order does not matter for product: down, right, diag (2x)