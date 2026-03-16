import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbol
t = sp.symbols('t')

# Define parametric equations
x = t**3 - 3*t
y = t**2 - 1

# Compute derivatives
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)

# Print derivatives
print(f"x(t) = {x}")
print(f"y(t) = {y}")
print(f"dx/dt = {dx_dt}")
print(f"dy/dt = {dy_dt}")

# Find t values where derivatives are zero
t_zero_dx = sp.solve(dx_dt, t)
t_zero_dy = sp.solve(dy_dt, t)

print(f"\nValues of t where dx/dt = 0: {t_zero_dx}")
print(f"Values of t where dy/dt = 0: {t_zero_dy}")

# Evaluate x(t) and y(t) at critical values
critical_points = []

print("\nPoints on the curve at critical parameter values:")

print("\nFor dx/dt = 0:")
for val in t_zero_dx:
    xv = x.subs(t, val)
    yv = y.subs(t, val)
    print(f"t = {val}: (x, y) = ({xv}, {yv})")
    critical_points.append((float(xv), float(yv)))

print("\nFor dy/dt = 0:")
for val in t_zero_dy:
    xv = x.subs(t, val)
    yv = y.subs(t, val)
    print(f"t = {val}: (x, y) = ({xv}, {yv})")
    critical_points.append((float(xv), float(yv)))

# Prepare data for plotting
# Remove duplicate points if any (based on coordinates)
unique_points = list(set(critical_points))
cp_x = [p[0] for p in unique_points]
cp_y = [p[1] for p in unique_points]

# Generate numerical data for the curve
t_vals = np.linspace(-2.5, 2.5, 500)
x_vals = t_vals**3 - 3*t_vals
y_vals = t_vals**2 - 1

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'b-', label='Parametric Curve')
plt.scatter(cp_x, cp_y, c='red', s=100, zorder=5, label='Critical Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve: x=t^3-3t, y=t^2-1')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.savefig('parametric_curve.png')

print("\nPlot saved to parametric_curve.png")