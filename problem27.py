from sympy import isprime, nextprime


def number_of_primes(a, b):
    n = 0
    while True:
        if not isprime(n**2 + a*n + b):
            break
        n += 1
    return n

# b must be prime
# a + b + 1 must also be prime
# check negative primes? => negative numbers excluded, so b cannot be negative

b = 1
max_primes = 0
max_factors = None

while b < 1000: # 1000, not prime, so safe to exclude
    for a in range(-999, 1000):
        if not isprime(a + b + 1):
            continue
        n = number_of_primes(a, b)
        if n > max_primes:
            max_primes = n
            max_factors = (a, b)

    b = nextprime(b)

print(max_factors, max_primes)
print(max_factors[0] * max_factors[1])