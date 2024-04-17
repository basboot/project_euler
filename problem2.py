def fibonacci():
    a, b = 0, 1
    while True:
        if a == 0:
            c = a + 1
        else:
            c = a + b
        a, b = b, c
        yield c


total = 0
for fib in fibonacci():
    if fib > 4000000:
        break

    if fib % 2 == 0:
        total += fib

print(total)