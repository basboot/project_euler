file = open('./0042_words.txt','r')

def word_value(w):
    return sum([ord(c) - ord('A') + 1 for c in list(w)])

triangular_numbers = set()

for n in range(1, 1000): # way to much
    t = n * (n + 1) / 2
    triangular_numbers.add(t)


total = 0

for word in file.readline().replace("\"", "").split(","):
    if word_value(word) in triangular_numbers:
        total += 1

print(total)