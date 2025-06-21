n_to_find = {1, 10, 100, 1000, 10000, 100000, 1000000}

i = 1
n = 0

p = 1
while True:
    i_digits = list(map(int, list(str(i))))
    # print(i_digits)
    for j in range(len(i_digits)):
        n += 1
        if n in n_to_find:
            print(f"{i_digits[j]}", end="")
            p *= i_digits[j]

    if n > 1000000:
        break
    i += 1

print()
print(p)

# 1153721 niet goed?

