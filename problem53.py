import math

count = 0
for n in range(1, 101):
    for k in range(1, n + 1):
        if math.comb(n, k) > 1000000:
            count += 1

print(count)

