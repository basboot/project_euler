p = 120

def solutions(p):
    s = 0
    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = p - a - b
            if c < 1:
                continue
            if c*c == a*a + b*b:
                s += 1
    return s

best = 0
best_p = 0
for p in range(1000):
    b = solutions(p)
    print(p, b)
    if b > best:
        best = b
        best_p = p


print(best, best_p)