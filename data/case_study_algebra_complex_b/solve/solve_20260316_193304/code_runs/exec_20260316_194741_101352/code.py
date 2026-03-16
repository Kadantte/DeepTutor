import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Define symbols
t, t1, t2 = sp.symbols('t t1 t2', real=True)

# Define parametric equations
x = t**3 - 3*t
y = t**2 - 1

# 1. Verify t = sqrt(3) and t = -sqrt(3)
t_val1 = sp.sqrt(3)
t_val2 = -sp.sqrt(3)

x1 = x.subs(t, t_val1)
y1 = y.subs(t, t_val1)
x2 = x.subs(t, t_val2)
y2 = y.subs(t, t_val2)

print("Verification for t = sqrt(3) and t = -sqrt(3):")
print(f"Point at t = sqrt(3): ({x1}, {y1})")
print(f"Point at t = -sqrt(3): ({x2}, {y2})")
is_same = sp.simplify(x1 - x2) == 0 and sp.simplify(y1 - y2) == 0
print(f"Are they the same point? {is_same}")
print("-" * 40)

# 2. Search for any other distinct parameter pairs
# Condition: x(t1) = x(t2) and y(t1) = y(t2) with t1 != t2
# From y(t1) = y(t2) => t1^2 = t2^2 => t1 = -t2 (since t1 != t2)
# Substitute into x(t1) = x(t2) => x(t1) = x(-t1)
# t1^3 - 3*t1 = -t1^3 + 3*t1 => 2*t1^3 - 6*t1 = 0 => 2*t1*(t1^2 - 3) = 0

equation = 2 * t1**3 - 6 * t1
solutions = sp.solve(equation, t1)

print("Searching for all distinct parameter pairs (t1, t2) with t1 != t2 producing same (x,y):")
intersection_pairs = []
intersection_points = []

for sol in solutions:
    if sol == 0:
        # t1 = 0 implies t2 = 0, which is not distinct
        continue
    t1_val = sol
    t2_val = -sol
    # Calculate coordinates
    pt_x = x.subs(t, t1_val)
    pt_y = y.subs(t, t1_val)
    intersection_pairs.append((t1_val, t2_val))
    intersection_points.append((pt_x, pt_y))

if not intersection_pairs:
    print("No self-intersection points found.")
else:
    for i, (pair, pt) in enumerate(zip(intersection_pairs, intersection_points)):
        print(f"Pair {i+1}: t1 = {pair[0]}, t2 = {pair[1]} -> Point (x, y) = ({pt[0]}, {pt[1]})")

print("-" * 40)

# 3. Plot the curve to visualize
t_num = np.linspace(-2.5, 2.5, 400)
x_num = t_num**3 - 3*t_num
y_num = t_num**2 - 1

plt.figure(figsize=(8, 6))
plt.plot(x_num, y_num, label=r'$x=t^3-3t, y=t^2-1$')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Mark intersection point
if intersection_points:
    ix = float(intersection_points[0][0])
    iy = float(intersection_points[0][1])
    plt.plot(ix, iy, 'ro', label=f'Intersection ({ix}, {iy})')
    plt.text(ix, iy + 0.2, f'({ix}, {iy})', horizontalalignment='center')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve Self-Intersection Verification')
plt.legend()
plt.savefig('curve_self_intersection.png')
print("Plot saved to 'curve_self_intersection.png'")