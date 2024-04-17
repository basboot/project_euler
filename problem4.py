import itertools
import math

values = list(range(100, 1000))

largest = -math.inf

for a, b in itertools.combinations_with_replacement(values, 2):
    c = a * b
    # print(c)
    if str(c) == str(c)[::-1]:
        largest = max(c, largest)

print(largest)