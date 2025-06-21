import math

i = 3

total = 0

while True:
    sum_fact = sum(list(map(lambda x: math.factorial(int(x)), list(str(i)))))

    if sum_fact == i:
        total += i
        print(i, total)
    i += 1