file1 = open('problem13.txt', 'r')
lines = file1.readlines()

total = 0
for line in lines:
    total += int(line.rstrip())

print(total)

# 5537376230390876637302048746832985971773659831892672