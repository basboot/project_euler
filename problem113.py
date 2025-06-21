from functools import cache


@cache
def increasing(current, depth):
    if depth == 0:
        return 1

    count = 0
    for i in range(current, 10):
        count += increasing(i, depth - 1)
    return count

@cache
def decreasing(current, depth, first=True):
    if depth == 0:
        return 1

    count = 0
    for i in range(current, 0 if first else -1, -1): # avoid all zeros
        count += decreasing(i, depth - 1, False)
    return count


def not_bouncy_below(digits):
    total = 0
    for max_depth in range(1, digits + 1):
        total += increasing(1, max_depth)
        total += decreasing(9, max_depth)
        total -= 9 # remove doubles

    return total


print(not_bouncy_below(100))