import sympy
from sympy import isprime

NUMBER = 600851475143

factors = []
for i in range(2, 13195):
    if isprime(i) and NUMBER % i == 0:
        print("prime factor", i)
        factors.append(i)

print(f"Largest prime factor {factors[-1]}")



