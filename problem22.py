import functools

file1 = open('problem22.txt', 'r')
lines = file1.readlines()

names = sorted(lines[0].rstrip().replace("\"", "").split(","))

name_values = [functools.reduce(lambda a, b: a + ord(b) - ord('A') + 1, list(x), 0) for x in names]

name_values2 = [(i + 1) * name_values[i] for i in range(len(name_values))]

print(sum(name_values2))