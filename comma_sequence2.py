
# comma sequence
# http://neilsloane.com/doc/Commas1.pdf


import math
import time
from functools import cache

max_start = (-math.inf, 0, 0)

FF = True

def find_next(n, ff=False):
    count = 0

    # fast forward if requested
    if ff:
        n, count = find_next_ff(n)

    # return if fast forward succeeded
    if count > 0:
        return n, count

    # else use naive approach to try to go further
    ten_str = str(n)
    ten = int(ten_str[-1])
    most_likely_one = int(ten_str[0])

    for i in range(10):
        one = (most_likely_one + i) % 10 # start with current first number

        option = n + 10 * ten + one
        if int(str(option)[0]) == one:
            return option, count + 1 # return first legal option found

    return n, 0 # not found, we cannot go any further


def find_next_ff(n):
    n_str = str(n)
    first = int(n_str[0])

    max_value = (10 ** (len(n_str) - 1)) * (int(first) + 1)

    start_value = n
    start_number = n_str[-1]
    count = 0

    while True:
        one_str = str(n)[-1]
        one = int(one_str)
        option = n + 10 * one + first # first stays the same until overflow, one changes after adding an interval

        if option < max_value: # only allowed if not overflowing
            n = option
            count += 1

            one_str = str(n)[-1]
            # We can fast forward if the last number repeats, to just before overflowing the first digit
            if one_str == start_number:
                to_go = max_value - n - 1 # amount to go before overflow
                rounds = to_go // (n - start_value)
                n += rounds * (n - start_value)
                count += rounds * count
        else:
            return n, count

for start in range(1, 30000):
    n = start
    max_n = n

    count = 1 # don't forget to count the first
    while True:
        # print(count, n)
        max_n = max(max_n, n)
        n, c = find_next(n, FF)
        count += c

        n_str = str(n)

        if c == 0: # not possible to go forward
            break

    if count > max_start[0]:
        max_start = (count, start, max_n)

    print(f"Sequence starting with {start}, has length {count} and ends with {max_n}")

    print(f"MAX: Sequence starting with {max_start[1]}, has length {max_start[0]} and ends with {max_start[2]}")

# Sequence starting with 2, has length 194697747222393 and ends with 9999999999999918