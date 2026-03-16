import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variable
t = sp.symbols('t')
x_t = t**3 - 3*t
y_t = t**2 - 1

# Derivatives
dx_dt = sp.diff(x_t, t)
dy_dt = sp.diff(y_t, t)

# 1. Self-intersection points
# Solve x(t1) = x(t2) and y(t1) = y(t2) for t1 != t2
t1, t2 = sp.symbols('t1 t2')
eq1 = sp.Eq(t1**3 - 3*t1, t2**3 - 3*t2)
eq2 = sp.Eq(t1**2 - 1, t2**2 - 1)
# From eq2: t1^2 = t2^2 => t1 = -t2 (since t1 != t2)
# Substitute t2 = -t1 into eq1
eq_sub = eq1.subs(t2, -t1)
sol_t1 = sp.solve(eq_sub, t1)
# Filter real non-zero solutions
self_intersect_t = []
for sol in sol_t1:
    if sol != 0 and sol.is_real:
        self_intersect_t.append(sol)

# Calculate coordinates for self-intersections
self_intersect_points = []
for val in self_intersect_t:
    self_intersect_points.append((val, (sp.simplify(x_t.subs(t, val)), sp.simplify(y_t.subs(t, val)))))

# 2. Critical points dx/dt = 0
crit_dx = sp.solve(dx_dt, t)
# 3. Critical points dy/dt = 0
crit_dy = sp.solve(dy_dt, t)

# 4. Intercepts
# x-axis (y=0)
intercept_x_t = sp.solve(y_t, t)
# y-axis (x=0)
intercept_y_t = sp.solve(x_t, t)

# Collect all key t values for the table
key_t_values = set()
for val in self_intersect_t:
    if val.is_real: key_t_values.add(val)
for val in crit_dx:
    if val.is_real: key_t_values.add(val)
for val in crit_dy:
    if val.is_real: key_t_values.add(val)
for val in intercept_x_t:
    if val.is_real: key_t_values.add(val)
for val in intercept_y_t:
    if val.is_real: key_t_values.add(val)

# Sort key t values numerically
sorted_t = sorted(list(key_t_values), key=lambda k: float(k))

# Print Results
print("="*70)
print("PARAMETRIC CURVE ANALYSIS: x = t^3 - 3t, y = t^2 - 1")
print("="*70)

print("\n1. SELF-INTERSECTION POINTS:")
for val, pt in self_intersect_points:
    print(f"   t = {val}, Point: ({pt[0]}, {pt[1]})")
# Verify t = +/- sqrt(3)
verified = True
for val, _ in self_intersect_points:
    if sp.simplify(val**2 - 3) != 0:
        verified = False
print(f"   Verification (t = +/- sqrt(3)): {'Confirmed' if verified else 'Failed'}")

print("\n2. CRITICAL POINTS (dx/dt = 0):")
for val in crit_dx:
    pt = (sp.simplify(x_t.subs(t, val)), sp.simplify(y_t.subs(t, val)))
    print(f"   t = {val}, Point: {pt}, Tangent: Vertical")

print("\n3. CRITICAL POINTS (dy/dt = 0):")
for val in crit_dy:
    pt = (sp.simplify(x_t.subs(t, val)), sp.simplify(y_t.subs(t, val)))
    print(f"   t = {val}, Point: {pt}, Tangent: Horizontal")

print("\n4. INTERCEPTS:")
print("   x-axis (y=0):")
for val in intercept_x_t:
    pt = (sp.simplify(x_t.subs(t, val)), sp.simplify(y_t.subs(t, val)))
    print(f"   t = {val}, Point: {pt}")
print("   y-axis (x=0):")
for val in intercept_y_t:
    pt = (sp.simplify(x_t.subs(t, val)), sp.simplify(y_t.subs(t, val)))
    print(f"   t = {val}, Point: {pt}")

print("\n5. MOTION DIRECTION BY REGION:")
regions = [(-np.inf, -1), (-1, 0), (0, 1), (1, np.inf)]
for i, (start, end) in enumerate(regions):
    if start == -np.inf:
        mid = -2.0
    elif end == np.inf:
        mid = 2.0
    else:
        mid = (start + end) / 2.0
    
    dx_val = 3*mid**2 - 3
    dy_val = 2*mid
    dir_x = "Right" if dx_val > 0 else "Left"
    dir_y = "Up" if dy_val > 0 else "Down"
    print(f"   Region {i+1} ({start}, {end}): dx/dt {dir_x}, dy/dt {dir_y}")

print("\n" + "="*70)
print("COMPREHENSIVE TABLE OF KEY POINTS")
print("="*70)
print(f"{'t value':<12} | {'(x, y)':<22} | {'Tangent':<12} | {'Significance':<30}")
print("-"*80)

for val in sorted_t:
    x_val = sp.simplify(x_t.subs(t, val))
    y_val = sp.simplify(y_t.subs(t, val))
    coord_str = f"({x_val}, {y_val})"
    
    tangent = "Slanted"
    significance = []
    
    # Check Critical
    is_crit_dx = any(sp.simplify(val - c) == 0 for c in crit_dx)
    is_crit_dy = any(sp.simplify(val - c) == 0 for c in crit_dy)
    
    if is_crit_dx:
        tangent = "Vertical"
    if is_crit_dy:
        tangent = "Horizontal"
        
    # Check Intersections
    is_self_intersect = any(sp.simplify(val - si[0]) == 0 for si in self_intersect_points)
    if is_self_intersect:
        significance.append("Self-Intersection")
        
    # Check Intercepts
    is_int_x = any(sp.simplify(val - i) == 0 for i in intercept_x_t)
    is_int_y = any(sp.simplify(val - i) == 0 for i in intercept_y_t)
    
    if is_int_x:
        significance.append("x-intercept")
    if is_int_y:
        significance.append("y-intercept")
        
    # Check Critical significance
    if is_crit_dx:
        significance.append("Vert. Tangent")
    if is_crit_dy:
        significance.append("Horiz. Tangent")
        
    sig_str = ", ".join(significance)
    print(f"{str(val):<12} | {coord_str:<22} | {tangent:<12} | {sig_str:<30}")

print("="*70)

# Plotting
t_num = np.linspace(-2.5, 2.5, 1000)
x_num = t_num**3 - 3*t_num
y_num = t_num**2 - 1

plt.figure(figsize=(8, 8))
plt.plot(x_num, y_num, label='x=t^3-3t, y=t^2-1', color='blue', linewidth=2)

# Plot key points
for val in sorted_t:
    xv = float(x_t.subs(t, val))
    yv = float(y_t.subs(t, val))
    plt.plot(xv, yv, 'ro', markersize=8, zorder=5)
    plt.text(xv, yv, f" t={float(val):.2f}", fontsize=9, verticalalignment='bottom', horizontalalignment='left')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')
plt.title('Parametric Curve: x=t^3-3t, y=t^2-1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('parametric_curve.png')
print("\nPlot saved to 'parametric_curve.png'")