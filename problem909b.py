import sys
sys.setrecursionlimit(20000)

# l_expression = ["S", ["Z"], ["A"], [0]] # 1
# l_expression = ["S", ["S"], ["S", ["S"]], ["S", ["Z"]], ["A"], [0]] # 6
l_expression = ["S", ["S"], ["S", ["S"]], ["S", ["S"]], ["S", ["Z"]], ["A"], [0]] # ?

def process_expression_iteratively(expression, rule):
    stack = [expression]  # Initialize a stack with the original expression
    restart = True

    while stack and restart:
        current_expression = stack.pop()  # Process the last expression from the stack

        # Iterate from the end to the beginning (same logic as your original code)
        for i in range(len(current_expression) - 1, -1, -1):
            if isinstance(current_expression[i], list):
                stack.append(current_expression[i])  # Add sublist to the stack for processing later
            else:
                match (rule, current_expression[i], len(current_expression) - i - 1):
                    case ("A", "A", x) if x > 0:
                        # print("AAAAA")
                        if isinstance(current_expression[i + 1], list) and isinstance(current_expression[i + 1][0], int):
                            current_expression[i] = current_expression[i + 1][0] + 1
                            del current_expression[i + 1]
                            restart = False
                            break
                    case ("Z", "Z", x) if x > 1:
                        # print("ZZZZZ")
                        if isinstance(current_expression[i + 1], list) and isinstance(current_expression[i + 2], list):
                            u, v = current_expression[i + 1: i + 3]
                            del current_expression[i + 2]  # Delete in reverse order
                            del current_expression[i + 1]
                            del current_expression[i + 0]
                            current_expression[i:i] = v  # Replace Z with v
                            restart = False
                            break
                    case ("S", "S", x) if x > 2:
                        # print("SSSSS")
                        if isinstance(current_expression[i + 1], list) and isinstance(current_expression[i + 2], list) and isinstance(current_expression[i + 3], list):
                            u, v, w = current_expression[i + 1: i + 4]
                            del current_expression[i + 3]  # Delete in reverse order
                            del current_expression[i + 2]
                            del current_expression[i + 1]
                            del current_expression[i + 0]

                            if False and len(u) == 1 and u[0] == "Z":
                                # print("Quick win?")
                                current_expression[i:i] = v + [w]
                            else:
                                current_expression[i:i] = v + [u + [v] + [w]]  # Replace S with v(u(v)(w))
                            restart = False
                            break

    return expression, not restart # True if something changed

count = 0
print("0 - INIT")
print(l_expression)
while len(l_expression) > 1:
    count += 1
    # print(count)
    for rule in ["A", "Z", "S"]:
        l_expression, has_changed = process_expression_iteratively(l_expression, rule)
        if has_changed: # start over after each change, to avoid doing too much S'es
            print(f"{count} - {rule} ***********")
            # if rule == "A" or rule == "Z":
            #     print(l_expression)
            #     # exit()
            break
    print(l_expression)
    # print(f"{count} *****************")

    if count == 100:
        break
print(l_expression)


# TODO: vind momenten dat er een A bij komt, en vergelijk begin naar laatste A