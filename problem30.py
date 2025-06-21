i = 2

answer = 0
while True:
    sum_digits = sum(list(map(lambda x: int(x) ** 5, list(str(i)))))
    if sum_digits == i:
        answer += i
        print(i, answer)

    i += 1