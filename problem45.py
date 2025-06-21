# n * (n + 1) / 2
# n * (3n - 1) / 2
# n * (2n -1
from collections import defaultdict

# greedy approach...

n = 1
results = defaultdict(int)
while True:
    t = n * (n + 1) / 2
    p = n * (3*n - 1) / 2
    h = n * (2*n - 1)

    for i in [t, p, h]:
        results[i] += 1
        if results[i] == 3:
            print(f"{i} is in three solutions")
    n += 1



