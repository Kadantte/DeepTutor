import numpy as np
from sympy import symbols, solve, Eq, sqrt, simplify

# Define the parametric curve (common curve with self-intersection at t = ±√3)
def x(t):
    return t**3 - 3*t

def y(t):
    return t**2 - 1

# Verify t = ±√3 give the same point
t1_val = np.sqrt(3)
t2_val = -np.sqrt(3)

print("=" * 60)
print("SELF-INTERSECTION POINT ANALYSIS")
print("=" * 60)

print(f"\n1. Verifying t = ±√3:")
print(f"   t1 = √3 ≈ {t1_val:.6f}")
print(f"   t2 = -√3 ≈ {t2_val:.6f}")
print(f"   x(t1) = {x(t1_val):.6f}, y(t1) = {y(t1_val):.6f}")
print(f"   x(t2) = {x(t2_val):.6f}, y(t2) = {y(t2_val):.6f}")
print(f"   Same point: {np.isclose(x(t1_val), x(t2_val)) and np.isclose(y(t1_val), y(t2_val))}")

# Symbolic solution for self-intersection points
print(f"\n2. Finding all self-intersection points symbolically:")
t1, t2 = symbols('t1 t2', real=True)

# System of equations: x(t1) = x(t2) and y(t1) = y(t2)
eq1 = Eq(t1**3 - 3*t1, t2**3 - 3*t2)
eq2 = Eq(t1**2 - 1, t2**2 - 1)

# From eq2: t1^2 = t2^2, so t1 = t2 or t1 = -t2
# We want t1 ≠ t2, so t1 = -t2
# Substitute into eq1:

# When t1 = -t2:
# (-t2)^3 - 3(-t2) = t2^3 - 3*t2
# -t2^3 + 3*t2 = t2^3 - 3*t2
# -2*t2^3 + 6*t2 = 0
# -2*t2(t2^2 - 3) = 0
# t2 = 0 or t2 = ±√3

print("\n   Solving the system analytically:")
print("   From y(t1) = y(t2): t1² = t2² → t1 = t2 or t1 = -t2")
print("   For distinct parameters: t1 = -t2")
print("   Substituting into x(t1) = x(t2):")
print("   (-t2)³ - 3(-t2) = t2³ - 3t2")
print("   -t2³ + 3t2 = t2³ - 3t2")
print("   2t2³ - 6t2 = 0")
print("   2t2(t2² - 3) = 0")
print("   t2 = 0 or t2 = ±√3")

print("\n   Self-intersection parameter pairs (t1, t2) with t1 ≠ t2:")
pairs = [
    (sqrt(3), -sqrt(3)),
    (-sqrt(3), sqrt(3)),
]

for t1_sym, t2_sym in pairs:
    point_x = simplify(t1_sym**3 - 3*t1_sym)
    point_y = simplify(t1_sym**2 - 1)
    print(f"   t1 = {t1_sym}, t2 = {t2_sym} → Point: ({point_x}, {point_y})")

# Note: t = 0 gives t1 = t2 = 0, which is not a self-intersection
print("\n   Note: t = 0 gives t1 = t2 = 0 (same parameter, not a self-intersection)")

# Numerical search for any other self-intersections
print(f"\n3. Numerical search for other self-intersection points:")
print("   Searching parameter range [-10, 10]...")

t_values = np.linspace(-10, 10, 10001)
x_values = x(t_values)
y_values = y(t_values)

# Find pairs where points are close (within tolerance)
tolerance = 1e-4
found_pairs = []

for i in range(len(t_values)):
    for j in range(i+1, len(t_values)):
        if abs(t_values[i] - t_values[j]) > 0.1:  # Ensure distinct parameters
            if np.abs(x_values[i] - x_values[j]) < tolerance and \
               np.abs(y_values[i] - y_values[j]) < tolerance:
                found_pairs.append((t_values[i], t_values[j], x_values[i], y_values[i]))

# Remove duplicates (pairs that are too close to each other)
unique_pairs = []
for pair in found_pairs:
    is_duplicate = False
    for existing in unique_pairs:
        if np.abs(pair[0] - existing[0]) < 0.5 and np.abs(pair[1] - existing[1]) < 0.5:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_pairs.append(pair)

print(f"\n   Found {len(unique_pairs)} self-intersection parameter pair(s):")
for t1_num, t2_num, x_val, y_val in unique_pairs:
    print(f"   t1 ≈ {t1_num:.4f}, t2 ≈ {t2_num:.4f} → Point ≈ ({x_val:.4f}, {y_val:.4f})")

# Create plot
import matplotlib.pyplot as plt

t_plot = np.linspace(-3, 3, 1000)
x_plot = x(t_plot)
y_plot = y(t_plot)

plt.figure(figsize=(8, 8))
plt.plot(x_plot, y_plot, 'b-', linewidth=2, label='Parametric curve')
plt.plot(0, 2, 'ro', markersize=10, label='Self-intersection (0, 2)')
plt.plot(x(np.sqrt(3)), y(np.sqrt(3)), 'g*', markersize=15, label='t = √3')
plt.plot(x(-np.sqrt(3)), y(-np.sqrt(3)), 'm*', markersize=15, label='t = -√3')

plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Parametric Curve: x(t) = t³ - 3t, y(t) = t² - 1')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.savefig('self_intersection_plot.png', dpi=150, bbox_inches='tight')
print("\n4. Plot saved to 'self_intersection_plot.png'")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("The curve has ONE self-intersection point at (0, 2)")
print("This occurs when t = √3 and t = -√3")
print("No other self-intersection points exist for this curve.")
print("=" * 60)