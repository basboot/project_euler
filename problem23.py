from sympy import divisors


def sum_proper_divisors(n):
    return sum(divisors(n)[0:-1])

abundants = []
# find abundants up to 28123
for i in range(1, 28124):
    if sum_proper_divisors(i) > i:
        abundants.append(i)

abundants.sort()

abundants_set = set(abundants)

abundants_not_possible_as_sum = 0

# can this abundant be made with a sum?
for i in range(1, 28124):
    possible = False
    for x in abundants:
        if x > i >> 1:
            break
        if i - x in abundants_set:
            possible = True
            break
    if not possible:
        # print(i)
        abundants_not_possible_as_sum += i

print(abundants_not_possible_as_sum)
