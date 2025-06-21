from sympy import nextprime

def is_pandigital(n):
    n_digits = len(str(n))
    return len (set(list(str(n))).intersection(set(list(map(str, range(1, n_digits + 1)))))) == n_digits

i = 1

while True:
    i = nextprime(i)

    if is_pandigital(i):
        print(i)

    if len(str(i)) > 9:
        break

