result = 0

for i in range(1000000):

    binary_repres = bin(i)[2:]
    if str(i) == str(i)[::-1] and binary_repres == binary_repres[::-1]:
        print("dbp", i, binary_repres)
        result += i

print(result)
