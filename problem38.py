def is_pandigital(n):
    if len(str(n)) != 9:
        return False
    return len (set(list(str(n))) - {'0'}) == 9

print(is_pandigital(123456780))

def create_candidate(n):
    result = ""
    i = 0
    while len(result) < 9:
        i += 1
        result += str(i * n)


    if i < 2:
        return None

    if not is_pandigital(int(result)):
        return None

    return int(result)

best = 0
for i in range(1, 50000000):
    candidate = create_candidate(i)

    if candidate is not None:
        if candidate > best:
            print(candidate)
            best = candidate

print(best)

