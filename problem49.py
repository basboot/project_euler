from collections import defaultdict

from sympy import nextprime, isprime

BELOW = 10000

i = 2
prime_permutations = defaultdict(list)
while i < BELOW:
    if i > 999: # only 4 digits
        prime_permutations[tuple(sorted(list(str(i))))].append(i)

    i = nextprime(i)


for prime_permutation in prime_permutations.values():
    if len(prime_permutation) < 3:
        continue

    seq_len = 2
    seq_size = prime_permutation[1] - prime_permutation[0]
    for i in range(2, len(prime_permutation)):
        new_seq_size = prime_permutation[i] - prime_permutation[i - 1]
        if new_seq_size == seq_size:
            seq_len += 1
        else:
            seq_len = 2
            seq_size = new_seq_size

        if seq_len == 3:
            print(prime_permutation)

# [2699, 2969, 6299, 9629]

