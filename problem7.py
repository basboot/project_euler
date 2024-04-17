import sympy

n_primes = 0

found = 0
find = 10001

n = 2

while True:
    if sympy.isprime(n):
        found += 1
    if find == found:
        print(n)
        break
    n += 1
