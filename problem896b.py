import cvxpy as cp
import numpy as np

print(cp.installed_solvers())

# size of the divisible range
N = 13

# create vars to represent the factor for each divider
# x[0] * 1, x[1] * 2, etc...
x = cp.Variable(N, integer=True)
y = cp.Variable((N, N), boolean=True)

M = 100000

minimum_value = 300

# create constraints
constraints = []
for i in range(N):
    for j in range(N):
        if i == j: # TODO: avoid double constraints
            continue

        # constrains.append(x[i] != x[j])
        # https://stackoverflow.com/questions/50428510/how-to-express-the-not-equals-relation-in-linear-programming
        constraints.append(x[i] * (i+1) <= x[j] * (j + 1) - 1 + M * y[i, j])
        constraints.append(x[i] * (i+1) >= x[j] * (j + 1) + 1 - M * (1 - y[i, j]))

        # each value must be within range of all other values
        constraints.append(x[i] * (i+1) <= x[j] * (j + 1) + N - 1)
        constraints.append(x[i] * (i+1) >= x[j] * (j + 1) - N + 1)



print(constraints)

# minimum
constraints.append(x[0] >= minimum_value)

objective = cp.Minimize(x[0])

prob = cp.Problem(objective, constraints)

# result = prob.solve(verbose=True)
result = prob.solve(solver='SCIPY', scipy_options={'method': 'revised simplex'})

print(prob.status)
print(prob.solver_stats)

# objective = cp.Minimize(cp.sum_squares(A @ x - b))
# constraints = [0 <= x, x <= 1]
# prob = cp.Problem(objective, constraints)
#
# # The optimal objective value is returned by `prob.solve()`.
# result = prob.solve()
# # The optimal value for x is stored in `x.value`.
print(x.value)

values = []
for i in range(N):
    values.append(x.value[i] * (i + 1))

values.sort()
print(values)


