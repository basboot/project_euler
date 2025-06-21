# ab = (a + b)^2, eg: 2025 = (20 + 25)^2
from tqdm import tqdm
import math


# ab must be a square
# split must sum up to the square root

def find_candidates(n):
    above = 10**(n - 1) - 1
    below = 10**n

    square_root_candidate = math.floor(math.sqrt(above) + 1)
    square_candidate =  square_root_candidate*square_root_candidate

    while square_candidate < below:
        yield square_candidate, square_root_candidate
        square_root_candidate += 1
        square_candidate = square_root_candidate * square_root_candidate


def can_split_and_sum(number: int, target: int) -> bool:
    str_num = str(number)
    n = len(str_num)

    for i in range(1, n):
        first_part = int(str_num[:i])

        if first_part > target:
            break  # break if the first part is already too large

        if str_num[i] == '0':
            continue # skip leading zeros

        second_part = int(str_num[i:])

        if first_part + second_part == target:
            return True

    return False

total = 0
for n in tqdm(range(1, 16 + 1)):
    for ab, square_root in find_candidates(n):
        if can_split_and_sum(ab, square_root):
            total += ab
            # print(ab, square_root)

print(total)





print(total)