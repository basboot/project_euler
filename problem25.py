import sys

sys.setrecursionlimit(10000)

# Python3 program to find the Nth Fibonacci
# number using Fast Doubling Method
#MOD = 1000000007


# Function calculate the N-th fibonacci
# number using fast doubling method
def FastDoubling(n, res):
    # Base Condition
    if (n == 0):
        res[0] = 0
        res[1] = 1
        return

    FastDoubling((n // 2), res)

    # Here a = F(n)
    a = res[0]

    # Here b = F(n+1)
    b = res[1]

    c = 2 * b - a

    # if (c < 0):
    #     c += MOD

        # As F(2n) = F(n)[2F(n+1) – F(n)]
    # Here c = F(2n)
    c = (a * c) #% MOD

    # As F(2n + 1) = F(n)^2 + F(n+1)^2
    # Here d = F(2n + 1)
    d = (a * a + b * b) #% MOD

    # Check if N is odd
    # or even
    if (n % 2 == 0):
        res[0] = c
        res[1] = d
    else:
        res[0] = d
        res[1] = c + d

    # Driver code


N = 1
offset = 2
growing = True

while True:
    # print(N, offset)
    res = [0] * 2
    FastDoubling(N, res)
    fib = res[0]
    print(fib)

    if fib < 10**999:
        offset *= 2
    else:
        print(N)
        break

    N = N + offset

# 8189 large enough
for N in range(8189, 0, -1):
    res = [0] * 2
    FastDoubling(N, res)
    fib = res[0]
    print(fib)
    if fib < 10**999:
        print(N, "too small")
        break

