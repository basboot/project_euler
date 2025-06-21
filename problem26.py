def decimals(n, max_decimals=10):
    result = []
    remainder = 10 # only iterested in decimals, so skip first 0
    start_repeat = 0
    current_repeat = 0
    while remainder > 0 and len(result) < max_decimals:
        if remainder < n:
            remainder *= 10
            result.append(0)
        else:
            result.append(remainder // n)
            remainder = (remainder % n) * 10

        # print(current_repeat, start_repeat)

        if len(result) > 1: # start watching
            if result[current_repeat] == result[-1]:
                # print("found possible repeat", result[-1])
                if current_repeat == 0:
                    start_repeat = len(result) - 1
                current_repeat += 1

                if current_repeat == start_repeat:
                    return start_repeat
            else:
                current_repeat = 0

    return 0

# md = 0
# for d in range(2, 1001):
#     md = max(decimals(d), md)
#
# print(md)

from math import gcd

def repeating_cycle_length(q):
    # Reduce denominator to its non-terminating part
    while q % 2 == 0:
        q //= 2
    while q % 5 == 0:
        q //= 5

    if q == 1:  # Terminating decimal
        return 0

    # Find the order of 10 modulo q
    k = 1
    remainder = 10 % q
    while remainder != 1:
        remainder = (remainder * 10) % q
        k += 1
    return k

md = 0
best_d = 0
for d in range(2, 1001):
    rc = repeating_cycle_length(d)
    if rc > md:
        md = rc
        best_d = d

print(md, best_d)

# 982 niet goed

