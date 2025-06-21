from itertools import permutations

digits = list("0123456789")

pds = []

total = 0
for pd in permutations(digits):
    if pd[0] == "0":
        continue

    is_substring_divisible = True

    for i, divider in enumerate([2, 3, 5, 7, 11, 13, 17]):
        substring = int("".join(pd[i+1:i+4]))
        # print(substring, divider)

        if substring % divider != 0:
            is_substring_divisible = False
            break

    if is_substring_divisible:
        # print(pd)
        total += int("".join(pd))



print(total)