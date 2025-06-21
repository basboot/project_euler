# O = (0,0)
# C0 = (R, 0) = (x_0, y_0)
# k = schaling (< 1)
# phi = draaiing
import math

from sympy import symbols, solve, nsolve
import sympy


# chat gpt helper function
def calculate_triangle_angles(a, b, c):
    # Calculate the angle opposite side a
    A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    # Calculate the angle opposite side b
    B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    # Calculate the angle opposite side c
    C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    # convert radians to 0-1
    A /= (math.pi * 2)
    B /= (math.pi * 2)
    C /= (math.pi * 2)

    return A, B, C


def calculate_triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

x0, x1, x8 = symbols("x0,x1,x8")
y0, y1, y8 = symbols("y0,y1,y8")
R, k, phi = symbols("R,k,phi")

expr = []
expr.append(x0 - R)
expr.append(y0)

def rotate_and_scale_xy(x, y, phi, n, k):
    x_rot = sympy.cos(phi * n) * x * k ** n - sympy.sin(phi * n) * y * k ** n
    y_rot = sympy.sin(phi * n) * x * k ** n + sympy.cos(phi * n) * y * k ** n

    return x_rot, y_rot

def distance(p1, q1, p2, q2):
    return sympy.sqrt((p1 - p2) ** 2 + (q1 - q2) ** 2)

x1_expr, y1_expr = rotate_and_scale_xy(x0, y0, phi, 1, k)
x8_expr, y8_expr = rotate_and_scale_xy(x0, y0, phi, 8, k)

expr.append(x1 - x1_expr)
expr.append(y1 - y1_expr)

expr.append(x8 - x8_expr)
expr.append(y8 - y8_expr)

expr.append(1 + k - distance(x0, y0, x1, y1))
expr.append(k + k ** 8 - distance(x1, y1, x8, y8))
expr.append(1 + k ** 8 - distance(x0, y0, x8, y8))

for exp in expr:
    print(exp)


solution = nsolve(tuple(expr), (k, phi, R, x0, y0, x1, y1, x8, y8), (0.9170040432046712, 0.8377580409572781, 2.5, 2.5, 0, 1.75, 1.75, 1.25, 0.25))
k, phi, R, x0, y0, x1, y1, x8, y8 = solution


r0 = 1
r1 = r0 * k
r8 = r0 * k ** 8

x7, y7 = rotate_and_scale_xy(x0, y0, phi, 7, k)
r7 = r0 * k ** 7

print(k, phi, R, x0, y0, x1, y1, x8, y8, r0, r1, r8)
print(x7, y7, r7)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def draw_circle(x, y, r):
    """
    Draw a circle with center at (x, y) and radius r.

    Parameters:
    x (float): The x-coordinate of the circle's center.
    y (float): The y-coordinate of the circle's center.
    r (float): The radius of the circle.
    """
    circle = plt.Circle((x, y), r, color='blue', fill=False)

    ax.add_patch(circle)






x, y, r = x0, y0, r0

for n in range(50):
    draw_circle(x, y, r)
    x, y = rotate_and_scale_xy(x, y, phi, 1, k)
    r = r * k

plt.grid(True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")

ax.set_aspect('equal', 'box')

# Set the limits of the plot to make sure the circle is fully visible
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)

plt.show()

# sides
a0, b0, c0 = distance(x0, y0, x1, y1), distance(x1, y1, x8, y8), distance(x8, y8, x0, y0)
a1, b1, c1 = distance(x0, y0, x8, y8), distance(x8, y8, x7, y7), distance(x7, y7, x0, y0)

# angles in 0-1
A0, B0, C0 = calculate_triangle_angles(a0, b0, c0)
A1, B1, C1 = calculate_triangle_angles(a1, b1, c1)

# triangle areas
area018 = calculate_triangle_area(a0, b0, c0)
area087 = calculate_triangle_area(a1, b1, c1)

# circle areas
circle0 = math.pi * r0 ** 2
circle1 = math.pi * r1 ** 2
circle7 = math.pi * r7 ** 2
circle8 = math.pi * r8 ** 2

# circle parts
circle_part018 = circle0 * B0 + circle1 * C0 + circle8 * A0
circle_part087 = circle0 * B1 + circle7 * A1 + circle8 * C1

# remainder
remainder018 = area018 - circle_part018
remainder087 = area087 - circle_part087

tworemainders = remainder018 + remainder087


# 10 decimals needed
print(tworemainders)

total = 0

while tworemainders > 1e-12:
    total += tworemainders
    tworemainders *= (k*k)
print("Total", total)



