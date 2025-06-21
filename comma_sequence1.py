import time
from functools import cache

start = 2

def find_next(n):
    ten_str = str(n)

    ten = int(ten_str[-1])
    most_likely_one = int(ten_str[0])

    for i in range(10):
        one = (most_likely_one + i) % 10 # start with current first number

        option = n + 10 * ten + one
        if int(str(option)[0]) == one:

            return option

    return None

# def find_next_pruned_helper(first, rest, top=False):
#     if len(rest) > 2:
#
#         next_number = rest[1:]
#         count = 0
#         for i in range(10 - int(rest[0]) if not top else 1):
#             next_number, next_count = find_next_pruned_helper(first, next_number, False)
#             count += next_count
#         return "9" + next_number[1:], count
#     else:
#         return find_next_pruned_helper2(first, rest, not top)
#
#
#
#

def add_leading_zeros(n_str, len_str):
    while len(n_str) < len_str:
        n_str = "0" + n_str
    return n_str

def find_next_pruned_helper2(first, rest, overflow=False):
    # perform lower levels first
    if len(rest) > 3:
        current = rest[0]
        rest = rest[1:]
        count = 0
        for i in range(int(current), 10):
            next_number, next_count = find_next_pruned_helper2(first, rest, True if i < 9 else overflow)
            rest = next_number
            count += next_count
        return ("0" if overflow else "9") + rest, count
    else:

        most_likely_one = int(first) # first number of second number is one of interval (.X)
        n = int(rest)
        max_next = 10 ** len(rest) - 1
        count = 0

        while True:
            ten = int(str(n)[-1])  # last digit of first number is ten of interval (X.)
            option = n + 10 * ten + most_likely_one

            if option > max_next:
                if overflow: # perform overflow for lower levels
                    n = option
                    count += 1
                    n_str = str(n)
                    return add_leading_zeros(n_str[1:], len(rest)), count # remove overflow
                else:

                    n_str = str(n)
                    return add_leading_zeros(n_str, len(rest)), count

            else:
                n = option
                count += 1


# def find_next_pruned_helper(first, remainder, top_level):
#     if len(remainder) > 2:
#         current = remainder[0]
#         rest = remainder[1:]
#         count = 0
#
#         if top_level:
#             # only one iteration without overflow
#             next_number, next_count = find_next_pruned_helper(first, rest, False)
#             count += next_count
#
#             # perform overflow
#             return first + next_number, count
#         else:
#             for i in range(9 - int(current)): # overflow possible until, next overflow
#                 next_number, next_count = find_next_pruned_helper(first, rest, False)
#                 count += next_count
#                 rest = next_number
#
#                 # perform overflow
#                 next_number = str(int(rest) + 10 * int(rest[-1]) + int(first))
#                 assert len(next_number) == len(rest) + 1, "Overflow went wrong"
#                 rest = next_number[1:] # remove overflow
#                 count += 1
#             return "9" + rest, count
#     else:
#         return find_next_pruned_helper2(first, remainder)

@cache
def find_next_pruned_helper(first, full_number, top_level=True):


    # print(">>>", first, remainder, next_number, next_count)
    if top_level:
        next_number, next_count = find_next_pruned_helper2(first, full_number[1:], False)
        return first + next_number, next_count
    else:
        next_number, next_count = find_next_pruned_helper2(first, full_number[1:])
        return next_number, next_count

def find_next_pruned(n, prune=True):
    n_str = str(n)

    if not prune or len(n_str) < 3: # small always without pruning
        return find_next(n), 1 # next, skip 1

    next_number, next_count = find_next_pruned_helper(n_str[0], n_str, True)
    # print("<<<", next_number, next_count)

    next_number_bak, next_count_bak = next_number, next_count

    print(next_number)
    next_number = find_next(int(next_number))


    if next_number is None:
        return int(next_number_bak), next_count_bak
    else:

        return find_next(int(next_number)), next_count + 1


start_time = time.process_time()

n = start
max_n = n

count = 0

history = {}

while n is not None:
    print(count, n)
    max_n = max(max_n, n)
    n, c = find_next_pruned(n, False) # 2137401 and ends with 99999945 lengte?
    count += c

    n_str = str(n)

    if c == 0:
        break





print(f"sequence staring with {start}, has length {count} and ends with {max_n}")
print(f"execution time was {round(time.process_time() - start)} seconds")

# 1 => 4 s

# sequence staring with 1, has length 2137453 and ends with 99999945
# execution time was 4 seconds\

