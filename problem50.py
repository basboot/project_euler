from sympy import nextprime, isprime

BELOW = 1000000

i = 2
partials = []
while i < BELOW:
    partials.append(i)
    i = nextprime(i)

# print(partials)


max_numbers = 0
cons_prime = 0
for start in range(len(partials)):
    prime_sum = 0
    for end in range(start, len(partials)):
        # print(partials[end], end=" ")
        prime_sum += partials[end]
        if prime_sum > BELOW:
            break # end if too large
        if isprime(prime_sum):

            n = end - start + 1
            # print(f"({n}) ", end="")
            if n > max_numbers:
                max_numbers = n
                cons_prime = prime_sum
    # print()

print(max_numbers, cons_prime)

# 543 not correct


