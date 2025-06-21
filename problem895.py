# 3 stacks
# silver and gold equal amount (balanced)
# max m per stack
# take top of stack until own color
# first player not able to move loses
# when playing optimal, first player must lose (fair)

# notes:
# game is symmetric
# stack representations can be binary + stack height

# silver = 0
# gold = 1

def count_ones(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

print(2**9898)