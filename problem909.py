import sys
sys.setrecursionlimit(2000)
from cvxpy.expressions.cvxtypes import expression

# S(Z)(A)(0)

# A(x) => x + 1
# Z(u)(v) => v
# S(u)(v)(w) => v(u(v)(w))

# l_expression = ["S", ["Z"], ["A"], [0]] # 1
l_expression = ["S", ["S"], ["S", ["S"]], ["S", ["Z"]], ["A"], [0]] # 6
# l_expression = ["S", ["S"], ["S", ["S"]], ["S", ["S"]], ["S", ["Z"]], ["A"], [0]] # ?

def process_single_expression(original_expression):

    restart = True
    expression = original_expression


    for i in range(len(expression) - 1, -1, -1):
        if isinstance(expression[i], list):
            expression[i] = process_single_expression(expression[i])

        match (expression[i], len(expression) - i - 1):
            case ("A", x) if x > 0:
                if isinstance(expression[i + 1], list) and isinstance(expression[i + 1][0], int):
                    expression[i] = expression[i + 1][0] + 1
                    del expression[i + 1]
            case ("Z", x) if x > 1:
                if isinstance(expression[i + 1], list) and isinstance(expression[i + 2], list):
                    u, v = expression[i + 1: i + 3]
                    del expression[i + 2]  # delete in reverse order
                    del expression[i + 1]
                    expression[i:i] = v


            case ("S", x) if x > 2:
                if isinstance(expression[i + 1], list) and isinstance(expression[i + 2], list) and isinstance(expression[i + 3], list):
                    u, v, w = expression[i + 1: i + 4]
                    # v(u(v)(w))
                    del expression[i + 3]  # delete in reverse order
                    del expression[i + 2]
                    del expression[i + 1]
                    del expression[i + 0]

                    expression[i:i] = v + [u + [v] + [w]]


    return original_expression

print(l_expression)
while len(l_expression) > 1:
    l_expression = process_single_expression(l_expression)
    print(l_expression)
    # exit()