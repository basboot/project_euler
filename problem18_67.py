file1 = open('problem67.txt', 'r')
lines = file1.readlines()

triangle = []

triangle_size = len(lines)

for line in lines:
    triangle += map(int, line.rstrip().split(" "))

# zero indexed!!!
def update(row, col):
    position = ((row * (row + 1)) // 2) + col
    triangle[position] += max(triangle[position + row + 1], triangle[position + row + 2])

for row in range(triangle_size - 2, -1, -1):
    for col in range(row + 1):
        update(row, col)

print(triangle[0])