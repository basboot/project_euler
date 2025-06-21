from itertools import permutations, combinations, combinations_with_replacement, product

import numpy as np

N = 3

options = list(range(N))

n = 0
agree = 0

# for option in product(permutations(options), repeat=3):
#     for i in range(N):
#
#         for j in range(N):
#             if i == j:
#                 continue
#
#
#
# print(f"{agree}/{n}")

options = np.array(list(product(permutations(options), repeat=3)))[113]

print(options.shape)

print(options)

first_index = np.argsort(options)

print(first_index)

for i in range(N):
    for j in range(N): # TODO: optimize to avoid double checks
        if i == j:
            continue
        print()