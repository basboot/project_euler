import cmath
import math

def calculate_triangle_angles(a, b, c):
    # Calculate the angle opposite side a
    A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    # Calculate the angle opposite side b
    B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    # Calculate the angle opposite side c
    C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    return A, B, C

def find_curvature(k1, k2, k3):
    sum_k = k1 + k2 + k3
    det_k = (2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)) # TODO: why not only ints?

    assert k1 * k2 + k2 * k3 + k3 * k1 > 0, "assume root is always possible"
    return sum_k - det_k, sum_k + det_k

# calculate start values
# a, b, c
a, b, c = 18, 23, -10
A, B, C = calculate_triangle_angles(1/a+1/b, 1/b+1/c, 1/c+1/a)
xa, ya = 0, 0
xc, yc = 1/c + 1/a, 0
xb, yb = math.sin(B + 0.5*math.pi) * (1/b+1/a), math.cos(B + 0.5*math.pi) * (1/b+1/a)


curvatures = [(a, xa + ya*1j), (b, xb + yb*1j), (c, xc + yc*1j)]
circle_ids = {(a, round(1000 * xa), round(1000 * ya)), (b, round(1000 * xb), round(1000 * yb)), (c, round(1000 * xc), round(1000 * yc))}


def find_curvatures(p1, p2, p3):
    global curvatures

    k4s = find_curvature(p1[0], p2[0], p3[0])

    for k4 in k4s:
        if k4 < 0:
            continue
        if k4 >= 1000: # ignore small
            continue
        z4 = calculate_center(p1, p2, p3, k4)
        print(p1[0], p2[0], p3[0], "->", k4)
        p4 = (k4, z4)

        if (k4, round(1000 * z4.real), round(1000 * z4.imag)) in circle_ids:
            continue
        else:
            circle_ids.add((k4, round(1000 * z4.real), round(1000 * z4.imag)))

        curvatures.append(p4)

        for c1, c2, c3 in [[p1, p2, p4], [p1, p4, p3], [p4, p2, p3]]:
            find_curvatures(c1, c2, c3)

test = 0
def calculate_center(p1, p2, p3, k4):
    k1, z1 = p1
    k2, z2 = p2
    k3, z3 = p3

    sum_z = z1 * k1 + z2 * k2 + z3 * k3
    det_z = 2 * cmath.sqrt(k1*k2*z1*z2 + k2*k3*z2*z3 + k3*k1*z3*z1)

    z4a, z4b = (sum_z + det_z) / k4, (sum_z - det_z) / k4

    error_a = 0
    error_b = 0
    for z, k in [(z1, k1), (z2, k2), (z3, k3)]:
        error_a += abs(abs(z - z4a) - abs(1/k + 1/k4))
        error_b += abs(abs(z - z4b) - abs(1/k + 1/k4))

    return z4a if error_a < error_b else z4b



find_curvatures(curvatures[0], curvatures[1], curvatures[2])

# solutions = list(curvatures)
# solutions.sort()

# print(solutions)
# print(len(solutions))

print(len(curvatures))

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


for k, pos in curvatures:
    draw_circle(pos.real, pos.imag, 1/k, k)


ax.set_xlim(-0.16, 0.08)
ax.set_ylim(-0.13, 0.13)

# plt.grid(True)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
plt.axis('off')

ax.set_aspect('equal', 'box')

plt.savefig('plot.pdf', format='pdf')  
plt.show()


print(len(circle_ids))


