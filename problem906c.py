from collections import defaultdict
from functools import cache
import sys

import numpy as np
from tqdm import tqdm

N = 10

@cache
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

@cache
def permutations(n, k):
    return factorial(n) // factorial(n - k)

@cache
def permutation_range(n_range, k):
    return factorial(n) // factorial(n - k)

@cache
def permutations_recursive_in_n(n, k):
    # Base cases
    if k == 0:
        return 1  # P(n, 0) = 1
    if n < k:
        return 0  # P(n, k) = 0 if k > n

    # Recursive case: P(n, k) = n * P(n-1, k-1)
    return n * permutations_recursive_in_n(n - 1, k - 1)


@cache
def get_right_possibilities(n_disagreement):
    n_right1 = N - 1 - n_disagreement
    n_right2 = N - 1
    factorials = [factorial(i) for i in range(n_right1, n_right2 + 1)]
    reversed_factorials = list(reversed(factorials))
    products = [f * r for f, r in zip(factorials, reversed_factorials)]
    return sum(products)


# warming up factorial
for i in tqdm(range(N)):
    factorial(i)
print(f"warmup: {N}! = {factorial(N)}")


sum_d = []

for d in tqdm(range(N + 1)):
    sum_d_sum = 0
    for i in range(d + 1):
        sum_d_sum += factorial(N - 1 - d + i) * factorial(N - 1 - i)

    sum_d.append(sum_d_sum)

sum_d = np.array(sum_d)
sum_d = sum_d.reshape((len(sum_d), 1))
print(sum_d.shape)

# print(sum_d)

sum_a = {}

# left_options = np.zeros((N + 1, N + 1), dtype=int)
# for a in tqdm(range(N + 1)):
#     # first is always 1
#     max_disagree = N - a
#
#     n_options = 1
#     left_options[0, a] = 1
#     for d in range(1, max_disagree + 1):
#         n_options *= (max_disagree - d + 1)
#         left_options[d, a] = n_options
#
# print(left_options)

left_options = np.zeros((N + 1, N + 1), dtype=int)
left_options[0, :] = 1

countdown = np.array(list(range(N, 0, -1)))
for i in tqdm(range(N)):
    left_options[1+i,0:len(countdown)] = left_options[i, 0:(len(countdown))] * countdown
    countdown = countdown[1:]

sum_a = np.sum(left_options * sum_d, 0)



total = 0
for n in range(1, N + 1):
    total += sum_a[n]

print(total)

total_options = factorial(N)**2 # Actually ^3, because p1 can be permutated if we want to have to absolurte number, but not needed since we are interested in the probability only
print(f"{total} / {total_options}")
print(f"p = {total / total_options}")

