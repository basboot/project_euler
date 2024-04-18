from num2words import num2words

count_letters = 0

for i in range(1, 1000 + 1):
    word = num2words(i)
    print(word)
    word = word.replace(" ", "").replace("-", "")
    count_letters += len(word)

print(count_letters)