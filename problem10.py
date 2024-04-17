import sympy

n = 2
max_prime = 2000000

total = 0
while n < max_prime:
    if sympy.isprime(n):
        total += n
    n += 1

print(total)