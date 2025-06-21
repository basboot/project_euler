results = set()
for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        results.add(a ** b)

print(len(results))
