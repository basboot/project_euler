import itertools
import math

values = list(range(1, 1000))

for a, b in itertools.combinations_with_replacement(values, 2):
    c2 = a*a + b*b
    c = math.sqrt(c2)
    if c == int(c):
        if a + b + c == 1000:
            print(a * b * c)
            break