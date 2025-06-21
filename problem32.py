from itertools import permutations

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# all needed
# product has same length as sum of multiplicants -1, or same (overflow), 9 total

# 1-4-4
# 2-3-4
# 2-2-5
# 1-3-5

results = set()
for a_len in [1, 2, 3, 4, 5, 6, 7]:
    for a in permutations(digits, a_len):
        digits_left = digits - set(a)
        for b_len in range(1, len(digits_left) - 1):
            for b in permutations(digits_left, b_len):
                digits_left_c = digits_left - set(b)

                # calc
                a_value = 0
                for num in a:
                    a_value = a_value * 10 + num
                b_value = 0
                for num in b:
                    b_value = b_value * 10 + num
                c_value = a_value * b_value

                c = list(map(int, list(str(c_value))))
                c_set = set(c)

                if len(c_set) == len(c) and c_set == digits_left_c:
                    print("Found", a_value, b_value, c_value)
                    results.add(c_value)


print(sum(results))
