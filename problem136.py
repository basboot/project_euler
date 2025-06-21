# -x**2 + 6xp -5p**2 < 50M

# oplossing als 6xp > x^2 + 5p^2

# 13, 10, 7, x = 13, p = 3

# (x^2) - (x-p)^2 - (x-2p)^2 = n

# print(13**2 - (13 - 7)**2 - (13 - 1)**2)

# exit()

x = 1
count = 0
while True:
    x += 1
    p = 0

    solutionFound = False
    while True:
        p += 1
        # print(x, p)

        n = -x**2 + 6*x*p -5*p**2
        if p >  x // 2:
            break

        if n > 0 and n < 50000000:
            count += 1
            solutionFound = True
            print(n)

        if n > 50000000:
            break
    if not solutionFound:
        break
print(count)

# TODO: for which x is no solution possible anymore?


