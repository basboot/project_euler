from sympy import divisors

def sum_proper_divisors(n):
    return sum(divisors(n)[0:-1])

def is_amicable_number(n):
    sum1 = sum_proper_divisors(n)
    return n != sum1 and sum_proper_divisors(sum1) == n

result = 0

for i in range(1, 10001):
    if is_amicable_number(i):
        print(i)
        result += i

print(result)