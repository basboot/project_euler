from collections import deque

from sympy import nextprime, isprime

MAX_PRIME = 1000000

n_circular = 0

i = 2

while i < MAX_PRIME:

    option = deque(list(str(i)))
    is_circular = True
    for _ in range(len(option)):
        option.rotate()
        if not isprime(int("".join(option))):
            is_circular = False
            break
    if is_circular:
        n_circular += 1


    i = nextprime(i)

print(n_circular)