from sympy import factorint

def n_divisors(n):
    result = 1
    for power in factorint(n).values():
        result *= (power + 1)
    return result - 1

triangular_number = 1

i = 2

# while True:
#     print(triangular_number)
#     if n_divisors(triangular_number) > 500:
#         break
#
#     triangular_number += i
#     i += 1



# print(triangular_number - i + 1) # rollback

print(n_divisors(76576500))

# 76564125 not correct

