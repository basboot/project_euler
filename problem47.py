from collections import deque

from sympy import factorint

N = 4

i = 1

n_factors = deque([0] * N)

while True:
    i += 1
    n = len(factorint(i))
    n_factors.append(n)
    n_factors.popleft()

    if n == N: # candidate
        if len(set(n_factors)) == 1:
            print(f"Found: {i - N + 1}")
            break

