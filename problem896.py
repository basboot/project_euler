import math
import time
from functools import cache

import numpy as np
import sympy



@cache
def get_dividers(n, N):
    # returns a set of all dividers of n up to N (inclusive)
    dividers = {1}
    for i in range(2, N + 1):
        if n % i == 0:
            dividers.add(i)

    return dividers


# use backtracking to find
@cache
def find_range(dividers, N):
    # sort by length, to start with most restricted
    sorted_dividers = sorted(dividers, key=len)
    used_dividers = set()

    # TODO: could be optimized by caching
    def dfs(i):
        # found all
        if i == N:
            return True

        for divider in sorted_dividers[i]:
            if divider not in used_dividers:
                used_dividers.add(divider)
                found = dfs(i + 1)
                if found:
                    return True
                # not found, try next
                used_dividers.remove(divider)
        return False

    return dfs(0)



def is_divisible_range(n, N):
    dividers = set()
    divider_lists = []
    # returns if the range [n, n + N] is a divisible range
    for i in range(N):
        new_dividers = get_dividers(n + i, N)
        dividers = dividers.union(new_dividers)

        divider_lists.append(tuple(new_dividers))

    # having all dividers is necessary, but not sufficient!
    if len(dividers) == N:
        return find_range(tuple(divider_lists), N)
    else:
        # It seems this (almost) never happens
        return False

def check_ranges(start, n, N):
    for i in range(n):
        is_div = is_divisible_range(start + i, N)
        # print("Check: ", list(range(start + i, start + i + N)))
        if is_div:
            yield start + i


def first_illegal_number(start, end):
    for n in range(start, end, 2 if end > start else -2): # start is always odd
        # we can skip 2, because we only look at odd  numbers
        if n % 3 == 0 or\
                n % 5 == 0 or\
                n % 7 == 0 or\
                n % 11 == 0 or\
                n % 13 == 0 or\
                n % 17 == 0 or\
                n % 19 == 0 or\
                n % 23 == 0 or\
                n % 29 == 0 or\
                n % 31 == 0:
            continue
        return n
    return end # not shorter


# start with 0, 37
def find_next_range(lower_illegal_number, middle_illegal_number, N):
    while True:
        upper_illegal_number = sympy.nextprime(middle_illegal_number)
        double_gap = upper_illegal_number - lower_illegal_number - 1  # no boundaries, one prime + space before and after

        if double_gap >= N:
            # TODO: try to narrow range by finding relative primes
            lower_illegal_number = first_illegal_number(middle_illegal_number - 2, lower_illegal_number) # skip first because it is even
            upper_illegal_number = first_illegal_number(middle_illegal_number + 2, upper_illegal_number)

            if double_gap >= N:
                return lower_illegal_number, middle_illegal_number, upper_illegal_number

        lower_illegal_number = middle_illegal_number
        middle_illegal_number = upper_illegal_number

N = 36

def find_ranges(N, end=math.inf):
    # [1,  first prime after N] is always a legal range
    middle_illegal_number = 0
    upper_illegal_number = sympy.nextprime(N)

    # start_time = time.time()

    while True:
        lower_illegal_number, middle_illegal_number, upper_illegal_number = find_next_range(middle_illegal_number, upper_illegal_number, N)

        for result in list(check_ranges(lower_illegal_number + 1, upper_illegal_number - lower_illegal_number - N , N)):
            yield result

        if lower_illegal_number > end:
            break

    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"With range check. Elapsed time: {elapsed_time} seconds")

# ChatGPT
def factorize(n):
    """Return the prime factors of the given integer n."""
    factors = []
    current_prime = 2

    # Check for prime factors starting from the smallest prime
    while current_prime <= n:
        while n % current_prime == 0:
            factors.append(current_prime)
            n //= current_prime
        current_prime = sympy.nextprime(current_prime)

    return factors

# for result in find_ranges(22, 1000000):
#     print("--:", result, factorize(result))


for N in range(2, 6):
    dividers = np.array(list(range(1, N + 1)))
    previous_result = 0
    for result in check_ranges(1, 10000000, N):
        if result > 10:
            print(N, ":",  result, factorize(result))
            print(np.mod(result, dividers))




            break
        previous_result = result



# print(math.lcm(*list(range(1, N))))





    # end_time = time.time()
    # elapsed_time = end_time - start_time
#
# print(f"Full range. Elapsed time: {elapsed_time} seconds")
# for N in range(36, 37):
#     for result in check_ranges(2 ** 4 * 3 ** 3 * 5 ** 2  * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31, 20, N):
#         print(N, ":",  result)
#
# print(math.lcm(*list(range(1, 37))))

# for N in range(15, 16):
#     for result in check_ranges(2 ** 2 * 3 * 5 * 7 * 11 * 13, 20, N):
#         print(N, ":",  result)

# 72201776446800 52407739, 204786077

# N= 30, 1 - 2000000
# [1, 2, 3, 4, 5, 6, 7]
# With range check. Elapsed time: 16.287874937057495 seconds
# 30 : 1
# 30 : 2
# 30 : 3
# 30 : 4
# 30 : 5
# 30 : 6
# 30 : 7
# Full range. Elapsed time: 34.0038583278656 seconds

# https://stackoverflow.com/questions/25661519/find-the-number-of-multiples-for-a-number-in-range