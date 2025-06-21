from collections import deque

from sympy import nextprime, isprime

primes = deque([])

current_prime = 1

def prime_with_all(current_prime, primes):
    for prime in primes:
        if not isprime(int(str(prime) + str(current_prime))):
            return False

        if not isprime(int(str(current_prime) + str(prime))):
            return False
    return True


MAX_PRIME = 10000

while len(primes) < 5:
    current_prime = nextprime(current_prime)

    if current_prime > MAX_PRIME:
        # backtrack
        current_prime = primes.pop()
        continue

    if len(primes) == 0:
        primes.append(current_prime)
        continue

    if prime_with_all(current_prime, primes):
        primes.append(current_prime)

print(sum(primes))



