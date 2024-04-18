from functools import cache

import sys
sys.setrecursionlimit(20000)

@ cache
def n_collatz(n):
    if n <= 1:
        return 1
    n = n // 2 if n % 2 == 0 else (3 * n + 1)
    return 1 + n_collatz(n)

max_length = 1
max_n = -1

for n in range(1000000):
    col = n_collatz(n)
    if col > max_length:
        max_length = col
        max_n = n

print(max_n)
