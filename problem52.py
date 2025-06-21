from collections import Counter

x = 0

while True:
    x += 1
    digits = Counter(list(str(x)))
    for n in range(2, 7):
        other_digits = Counter(list(str(x * n)))

        if other_digits != digits:
            break

        if n == 6:
            print(x)


