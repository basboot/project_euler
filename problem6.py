import numpy as np


def sum_of_squares(n):
    # 1-n inclusive
    values = np.array(list(range(1, n+1)))
    values = values ** 2
    return np.sum(values)

def square_of_sum(n):
    # 1-n inclusive
    values = np.array(list(range(1, n+1)))
    return np.sum(values) ** 2


print(square_of_sum(100) - sum_of_squares(100))