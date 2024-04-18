import math
from itertools import permutations

import numpy as np

file1 = open('problem81.txt', 'r')
lines = file1.readlines()

import heapq


def dijkstra(matrix, start, end):
    queue = [(matrix[start], start, [start])]
    explored = set()

    while queue:
        current_distance, current_position, path = heapq.heappop(queue)

        if current_position == end:
            # If we've reached the end position, return the distance
            return current_distance, path

        if current_position in explored:
            # Skip processing this position if we've found a shorter path to it already
            continue
        explored.add(current_position)

        # Get the cost of moving to neighboring positions
        neighbors = next_positions(current_position)

        for neighbor in neighbors:
            total_cost = current_distance + matrix[neighbor]
            heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))



    # If no path is found, return infinity
    return float('inf')

def next_positions(position):
    i, j = position
    next = []
    if i < matrix.shape[0] - 1:
        next.append((i + 1, j))
    if j < matrix.shape[1] - 1:
        next.append((i, j + 1))

    return next

rows = []
for line in lines:
    row = [int(x) for x in line.rstrip().split(",")]
    # print(row)
    rows.append(row)

matrix = np.array(rows)

print(matrix.shape)

start_position = (0, 0)
end_position = (len(matrix) - 1, len(matrix[0]) - 1)

shortest_distance = dijkstra(matrix, start_position, end_position)
print("Shortest distance from", start_position, "to", end_position, "is:", shortest_distance)

# 420740 is not correct
# 701307 ook niet
# 705752 ook niet
# 262091 ook niet

# 428327 ook niet :-(


def minimal_path_sum():
  matrix = rows.copy()

  size = len(matrix)
  # calculate minimal sums for bottom row and last column
  # as they don't have any other way to be reached
  for i in reversed(range(0, size - 1)):
    matrix[size - 1][i] += matrix[size - 1][i + 1]
    matrix[i][size - 1] += matrix[i + 1][size - 1]

  for i in reversed(range(0, size - 1)):
    for j in reversed(range(0, size - 1)):
      matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

  return matrix[0][0]

print("validate", minimal_path_sum())



