import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t1 = sp.symbols('t1')
equation = 2 * t1**3 - 2 * t1
roots = sp.solve(equation, t1)

valid_t1 = [r for r in roots if r != 0]
points = []

print("Valid t1 values:", valid_t1)
for t_val in valid_t1:
    t2_val = -t_val
    x_val = t_val**2 - 1
    y_val = t_val**3 - t_val
    points.append((float(x_val), float(y_val)))
    print(f"t1={t_val}, t2={t2_val} -> Intersection Point: ({x_val}, {y_val})")

t = np.linspace(-2, 2, 400)
x = t**2 - 1
y = t**3 - t

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Curve')
for px, py in points:
    plt.plot(px, py, 'ro', label='Intersection')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.savefig('intersection.png')