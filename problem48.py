
result = 0

MOD = 10 ** 10

for i in range(1, 1000 + 1):
    result = (result + pow(i, i, MOD)) % MOD

print(result)