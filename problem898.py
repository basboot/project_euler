import numpy as np

# ChatGPT
def create_binary_array(n):
    # Calculate the number of rows in the output matrix
    num_rows = 2 ** n # use symmetry of the problem

    # Generate all numbers from 0 to 2^n - 1
    numbers = np.arange(num_rows)

    # Convert each number to its binary representation and store as a string
    binary_strings = [np.binary_repr(num, width=n) for num in numbers]

    # Create the binary matrix by converting each character in the string to an integer
    binary_matrix = np.array([[int(bit) for bit in binary_string] for binary_string in binary_strings])

    return binary_matrix#[0:1,:] # TODO: remove when it works


ps = [20, 40, 80] #
# ps = list(range(25, 76))
# size = 25
# ps = list(range(50 - size, 50 + size + 1))


N = len(ps)

lying_probabilities = np.array([ps]) / 100
print(len(lying_probabilities))





not_lying_probabilities = 1 - lying_probabilities



answers = create_binary_array(N)
print(answers)
#
# # given 1, what are the probabilities for each answer
#
chance_one = np.multiply(answers, not_lying_probabilities) + np.multiply(1 - answers, lying_probabilities)
print(chance_one)
#
# # given 0, what are the probabilities for each answer
#
chance_not_one = np.multiply(1 - answers, not_lying_probabilities) + np.multiply(answers, lying_probabilities)
#
# print(chance_not_one)
#
p_one = np.prod(chance_one, 1)
print(p_one)
p_not_one = np.prod(chance_not_one, 1)
print(p_not_one)

p = np.array([p_one, p_not_one])

p_norm = p / np.sum(p) #

print(p_norm)

print(np.sum(np.max(p_norm, 0)))

total = 0
correct = 0
for _ in range(10000):
    # sim
    # always 1, so not lying is 1
    answer = np.random.random((not_lying_probabilities.shape)) < not_lying_probabilities
    chance_one = np.multiply(answer, not_lying_probabilities) + np.multiply(1 - answer, lying_probabilities)
    chance_not_one = np.multiply(1 - answer, not_lying_probabilities) + np.multiply(answer, lying_probabilities)
    p_one = np.prod(chance_one, 1)
    # print(p_one)
    p_not_one = np.prod(chance_not_one, 1)
    # print(p_not_one)
    total += 1
    if p_one > p_not_one:
        correct += 1
    else:
        if p_one == p_not_one:
            correct += 0.5

print("sim", correct / total)

