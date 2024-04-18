import math
from functools import cache

import sympy

@cache
def isprime(n):
    return sympy.isprime(n)

@cache
def factorize(n):
    factors = []
    i = 2
    while n > 1:
        # break early if remainder is prime
        if isprime(n):
            return factors + [n]

        # test if prime number is a factor
        if isprime(i):
            if n % i == 0:
                factors.append(i)
                n = n // i
                return factors + factorize(n)
        i += 1
    return factors



def s(n, start=1):
    m = 1
    while True:
        if math.factorial(m) % n == 0:
            return m
        m += 1

def s_smart(n):
    # prime numbers are easy
    if isprime(n):
        return n

    # find factors of n
    factors_n = factorize(n) # are sorted
    last_factor = 1
    m = 1
    last_n = 1
    spare_factors = 0
    for i in range(len(factors_n)):
        factor = factors_n[i]
        if factor > last_factor:
            # new factor, increase m to at least the factor to accomodate
            last_factor = factor
            last_n = factor
            spare_factors = 0 # no factors left, because we have a prime factor
            m = max(m, factor)
        else:
            # use spare factors if there are factors left, otherwise find new
            if spare_factors > 0:
                spare_factors -= 1
            else:
                # find new factors and increase m if needed
                while True:
                    last_n += 1
                    spare_factors = factorize(last_n).count(factor)
                    if spare_factors > 0:
                        m = max(m, last_n)
                        spare_factors -= 1
                        break
    return m


total = 0
for i in range(2, 10**8 + 1):
    if i % 10**6 == 0:
        print(i)
    result = s_smart(i)
    total += result
print(total)

# TODO: optimize by storing (partial) solutions (factors => minimal m, last_n, spare_factors)


# duurde een beetje lang, maar is wel goed :-)
# 476001479068717
