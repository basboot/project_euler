from collections import Counter
from functools import cache
import sys

import numpy as np
from numpy.ma.core import remainder
from sympy import divisors, factorint, nextprime

from time import sleep
from tqdm import tqdm

sys.setrecursionlimit(100000)

@cache
def roundness(n, b):
    if b == 1:
        return 0
    r = 0
    while n % b == 0:
        r += 1
        n = n // b

    return r

@cache
def dividers(n):
    return divisors(n)

def factorize(n):
    results = []
    res = factorint(n)
    for factor, multiplicity in res.items():
        results += [factor] * multiplicity

    return results

@cache
def total_roundness(n):
    r = 0
    for b in dividers(n):
        rnds = roundness(n, b)
        # if rnds > 0:
        #     print(f"roundness {rnds} for base {b} {factorize(b)}")
        r += rnds
    return r

# print(roundness(20, 1))

# print(factors(20))

# a = 3
# b = 2
# c = 5
# d = 17
# print(total_roundness(a), total_roundness(b), total_roundness(c), total_roundness(d), total_roundness(a * b * c * d))


# n = 3 * 3 * 3 * 5 * 5 * 5 * 5 * 5 * 5
# print(f"Roundness for {n}, {factors(n)}")
#
# print(total_roundness(n))

# prime only zeros in base of prime
# prime * prime => two zeros in base of prime + zero in base prime^2

# prime1 * prime2, zero in base prime1, prime2 and prime1*prime2
# p1 * p2 * pn, combinations 1-n

# prime1 * prime1 * prime2 => 2 zeros in p1, zero in p1^2, zero in p2, 2 zeros in p1*p2, zero in pi^2*p2


def factors_of_factorial(n):
    print("start fact")
    factor = 2
    result = {}

    while factor < n:
        multiplicity = 0
        remainder = n
        while remainder > 0:
            remainder //= factor
            multiplicity += remainder
        if multiplicity > 0:
            result[factor] = multiplicity
        factor = nextprime(factor)

    return result


from itertools import product
from math import comb

def calculate_roundness2(factor_multiplicities):
    multiplicities = np.array(list(factor_multiplicities))
    roundness = 0
    for i in tqdm(range(1, np.max(multiplicities) + 1)):
        result = np.prod(multiplicities // i + 1) - 1

        roundness = (roundness + result) % 1000000007

    return roundness

def calculate_roundness3(factor_multiplicities):
    multiplicities = Counter(list(factor_multiplicities))

    roundness = 0
    for i in tqdm(range(1, max(multiplicities.keys()) + 1)):
        r = 1
        for prime in multiplicities:
            if prime < i: # skip when too low
                continue
            m = prime // i + 1
            r = (r * pow(m, multiplicities[prime], 1000000007)) % 1000000007
        roundness = (roundness + r - 1) % 1000000007

    return roundness

def calculate_roundness(factor_multiplicities):
    print("start round")
    # Create lists
    factor_options = [list(range(n + 1)) for n in list(factor_multiplicities)]

    # generate all combinations
    all_combinations = list(product(*factor_options))

    print(len(all_combinations))

    roundness = 0
    print(len (all_combinations))
    for combination in product(*factor_options):
        # print("next comb", combination)
        if np.sum(combination) == 0:
            # print("skip")
            continue # skip zero
        # for every combination check how many times we can create it from the factors
        remainder = np.array(list(factor_multiplicities))
        # print("add default")

        combination = np.where(combination == 0, np.inf, combination)

        # Perform integer division and find the minimum
        roundness += int(np.min(remainder // combination))

        roundness = roundness % (1000000007)
            # print("add +1")
        # roundness += np.sum(np.array(combination) > 0)

    return roundness


# print(factors_of_factorial(10))

n = 3 * 3 * 3 * 5 * 5 * 17

factors = factorint(n)
# print(factors)
# # print("> ", total_roundness(n))
# # print("< ", calculate_roundness(list(factors.values())))
# print("<<", calculate_roundness2(list(factors.values())))
# print("<<", calculate_roundness3(list(factors.values())))


# exit()
# print(":", calculate_roundness3(list(factors_of_factorial(10000000).values())))

print(":", calculate_roundness3(list(factors_of_factorial(10000).values())))





