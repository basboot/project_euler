from itertools import permutations

digits = list("0123456789")

print(list(permutations(digits))[1000000 - 1])
