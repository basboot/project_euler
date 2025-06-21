from functools import cache


pentagonal_numbers = set()

# greedy approach
for n in range(1, 10000):
    p = n * (3 * n - 1) / 2
    pentagonal_numbers.add(p)

for p1 in pentagonal_numbers:
    for p2 in pentagonal_numbers:
        if p1 == p2:
            continue
        if p1 + p2 in pentagonal_numbers and abs(p1 - p2) in pentagonal_numbers:
            print(f"Found candidates {p1} {p2} D = {abs(p1 - p2)}")


