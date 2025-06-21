from collections import defaultdict
from itertools import combinations

from sympy import nextprime

primesets = defaultdict(set)

LEN = 6

p = 1
while True:
    p = nextprime(p)
    p_lst = list(str(p))
    if len(p_lst) < LEN:
        continue

    if len(p_lst) > LEN:
        break

    for digit in range(10):
        indices = [i for i, x in enumerate(p_lst) if x == str(digit)]

        if len(indices) > 0:
            # print(">", indices)
            for subset_len in range(1, len(indices) + 1):
                for subset in combinations(indices, subset_len):
                    # print(subset)
                    mask = p_lst.copy()
                    for index in subset:
                        mask[index] = "_"

                    # print(mask)

                    primesets[tuple(mask)].add(p)


for ps in primesets:
    if len(primesets[ps]) == 8:
        print(primesets[ps], min(primesets[ps]))
