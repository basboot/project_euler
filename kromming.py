import cmath
import math

def find_curvature(k1, k2, k3):
    sum_k = k1 + k2 + k3
    det_k = (2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)) # TODO: why not only ints?

    assert k1 * k2 + k2 * k3 + k3 * k1 > 0, "assume root is always possible"
    return sum_k - det_k, sum_k + det_k

# grote cirkel is -10
print(find_curvature(18,23, 27))


def calculate_triangle_angles(a, b, c):
    # Calculate the angle opposite side a
    A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    # Calculate the angle opposite side b
    B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    # Calculate the angle opposite side c
    C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    return A, B, C

# a, b, c
A, B, C = calculate_triangle_angles(1/18+1/23, 1/23+1/-10, 1/-10+1/18)
x18, y18 = 0, 0
x10, y10 = -1/10 + 1/18, 0
x23, y23 = math.sin(B + 0.5*math.pi) * (1/23+1/18), math.cos(B + 0.5*math.pi) * (1/23+1/18)

a, b, c = 18, 23, -10

curvatures = {18: x18 + y18*1j, 23: x23 + y23*1j, -10: x10 + y10*1j  }

def find_curvatures(k1, k2, k3):
    global curvatures
    k4s = find_curvature(k1, k2, k3)

    print(k1, k2, k3, "=>", k4s)

    for k4 in k4s:
        # if k4 < 0: # ignore outer circles
        #     continue
        if k4 in curvatures: # do not repeat exploration TODO: is this correct?
            continue

        if k4 >= 1000: # ignore small
            continue
        curvatures[k4] = calculate_center(k1, k2, k3, k4)
        # print(k4)

        for c1, c2, c3 in [[k1, k2, k4], [k1, k4, k3], [k4, k2, k3]]:
            find_curvatures(c1, c2, c3)

test = 0
def calculate_center(k1, k2, k3, k4):
    global test
    z1, z2, z3 = curvatures[k1], curvatures[k2], curvatures[k3]

    sum_z = z1 * k1 + z2 * k2 + z3 * k3
    det_z = 2 * cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)


    z4a, z4b = (sum_z + det_z) / k4, (sum_z - det_z) / k4

    error_a = 0
    error_b = 0
    for z, k in [(z1, k1), (z2, k2), (z3, k3)]:
        error_a += abs(abs(z - z4a) - abs(1/k + 1/k4))
        error_b += abs(abs(z - z4b) - abs(1/k + 1/k4))

    return z4a if error_a < error_b else z4b





    # for k, pos in curvatures.items():
    #     print("check", k, pos)
    #     if k == -10:
    #         print("do not check outer")
    #         continue
    #     print("compare", k, pos)
    #     dist = abs(z4a - pos)
    #     print("dist", dist, 1/k + 1/k4)
    #     if abs(dist - (1/k + 1/k4)) < 0.1 or abs(dist - (1/k + 1/k4)) > 0.1:
    #         return z4b
    #
    # return z4a



find_curvatures(a, b, c)

solutions = list(curvatures)
solutions.sort()

print(solutions)
print(len(solutions))

print(curvatures)





###

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def draw_circle(x, y, r, k):
    """
    Draw a circle with center at (x, y) and radius r.

    Parameters:
    x (float): The x-coordinate of the circle's center.
    y (float): The y-coordinate of the circle's center.
    r (float): The radius of the circle.
    """
    circle = plt.Circle((x, y), r, color='black' if k != 135 else 'black', fill=False, linewidth=0.1)

    ax.add_patch(circle)

    plt.text(x, y, str(round(k)), ha='center', va='center', fontsize=700/k)


for k, pos in curvatures.items():
    draw_circle(pos.real, pos.imag, 1/k, k)


ax.set_xlim(-0.17, 0.08)
ax.set_ylim(-0.13, 0.13)

# plt.grid(True)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
plt.axis('off')

ax.set_aspect('equal', 'box')

plt.savefig('plot.pdf', format='pdf')  
plt.show()




