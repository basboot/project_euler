from collections import defaultdict
from functools import cache
import sys

import numpy as np

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
def get_right_possibilities(n_disagreement):
    n_right1 = N - 1 - n_disagreement
    n_right2 = N - 1
    factorials = [factorial(i) for i in range(n_right1, n_right2 + 1)]
    reversed_factorials = list(reversed(factorials))
    products = [f * r for f, r in zip(factorials, reversed_factorials)]
    return sum(products)


# warming up factorial
for i in range(N):
    factorial(i)
print(f"warmup: {N}! = {factorial(N)}")

total_agreements = 0
# p1 is fixed, n_agreement is the position of the number to agree on for p1
for n_agreement in range(1, N+1):
    print(f"number to agree on {n_agreement}")
    max_disagreement = N - n_agreement # -1, p2 and p3 cannot disagree on n_agreement, or choices p1 disagrees on

    for n_disagreement in range(max_disagreement + 1):

        print("calc left p")
        left_possibilities = permutations(N - n_agreement, n_disagreement) # from n (all numbers except the agreement) make permutations of length k (n_disagreemant) mogelijkheden om disagreements te verdelen

        print("caclc right p")
        right_p = get_right_possibilities(n_disagreement)
        n_agreements_for_option = left_possibilities * right_p

        print("calc subtotal")
        total_agreements += n_agreements_for_option
        print(f"number of diagreements {n_disagreement} on {n_agreement}")# has {n_agreements_for_option} agreements")


total_options = factorial(N)**2 # Actually ^3, because p1 can be permutated if we want to have to absolurte number, but not needed since we are interested in the probability only
print(f"{total_agreements} / {total_options} = {total_agreements / total_options}")

