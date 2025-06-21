from sympy import isprime


def squares():
    n = 1
    while True:
        yield n * n
        n += 1

odd_number = 1

while True:
    odd_number += 2
    if isprime(odd_number): # must be composite
        continue

    found = True
    for square in squares():
        if square > odd_number:
            break
        if isprime(odd_number - 2 * square):
            found = False
            break
    if found:
        print(f"{odd_number} cannot be written as sum of prime and twice a square")
        break
