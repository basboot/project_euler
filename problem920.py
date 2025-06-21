from sympy import divisors


def is_tau(n):
    return n % len(divisors(n)) == 0

print(is_tau(2**26 * 3**15))