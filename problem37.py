from sympy import nextprime, isprime

i = 11

def is_truncatable_prime(p):
    assert isprime(p), "Only works for primes"
    p_str = str(p)
    for i in range(len(p_str) - 1):
        if not isprime(int(p_str[i + 1:])):
            return False
    for i in range(len(p_str) - 1):
        if not isprime(int(p_str[:i + 1])):
            return False
    return True

result = 0
while True:
    if is_truncatable_prime(i):
        result += i
        print(i, result)
    i = nextprime(i)

