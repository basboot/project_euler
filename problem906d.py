# 3, 34 / 36
# 4, 512 / 576
# 5, 12096 / 14400
# 6, 413568 / 518400
# 7, 19335744 / 25401600
import math

n = 3
n_agreements = 34
n_possibilities = 36


n += 1

n_possibilities *= (n ** 2)

print(f"diff = {512 - n_agreements}")

print((n - 2) + math.factorial(n - 2))

# 512

print(f"n = {n}, {n_agreements} / {n_possibilities} = {n_agreements / n_possibilities}")


print(f"tweede = {12096 - 512}")


