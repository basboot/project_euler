SIZE = 1001 // 2

current_sum = 1

current_value = 1
for i in range(SIZE):
    offset = (i + 1) * 2
    for _ in range(4):
        current_value += offset
        current_sum += current_value

print(current_sum)



