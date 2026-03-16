import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbolic variable
t = sp.symbols('t')

# Define the parametric equations
x = t**2 - 1
y = t**3 - t

# Compute the derivatives
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)

# Find critical values where derivatives are zero
critical_t_dx = sp.solve(dx_dt, t)
critical_t_dy = sp.solve(dy_dt, t)

# Print derivatives and critical values
print(f"x(t) = {x}")
print(f"y(t) = {y}")
print(f"dx/dt = {dx_dt}")
print(f"dy/dt = {dy_dt}")
print(f"\nValues of t where dx/dt = 0: {critical_t_dx}")
print(f"Values of t where dy/dt = 0: {critical_t_dy}")

# Function to analyze sign changes
def analyze_sign_changes(derivative, critical_points, name):
    print(f"\nSign analysis for {name}:")
    if not critical_points:
        print("  No critical points found.")
        return
    
    # Convert to floats and sort
    pts = sorted([float(p) for p in critical_points])
    f = sp.lambdify(t, derivative, 'numpy')
    
    # Define test intervals
    intervals = []
    if len(pts) == 1:
        intervals.append((pts[0] - 1.0, f"t < {pts[0]:.4f}"))
        intervals.append((pts[0] + 1.0, f"t > {pts[0]:.4f}"))
    else:
        intervals.append((pts[0] - 1.0, f"t < {pts[0]:.4f}"))
        for i in range(len(pts) - 1):
            mid = (pts[i] + pts[i+1]) / 2.0
            intervals.append((mid, f"{pts[i]:.4f} < t < {pts[i+1]:.4f}"))
        intervals.append((pts[-1] + 1.0, f"t > {pts[-1]:.4f}"))
    
    # Print signs in intervals
    for val, label in intervals:
        res = f(val)
        sign = "+" if res > 0 else "-" if res < 0 else "0"
        print(f"  Interval {label}: derivative is {sign}")
    
    # Print sign changes at critical points
    print("  Sign changes at critical points:")
    for pt in pts:
        val_left = f(pt - 1e-5)
        val_right = f(pt + 1e-5)
        sign_left = "+" if val_left > 0 else "-" if val_left < 0 else "0"
        sign_right = "+" if val_right > 0 else "-" if val_right < 0 else "0"
        changes = "Yes" if sign_left != sign_right else "No"
        print(f"    At t = {pt:.4f}: {sign_left} -> {sign_right} (Change: {changes})")

# Perform sign analysis
analyze_sign_changes(dx_dt, critical_t_dx, "dx/dt")
analyze_sign_changes(dy_dt, critical_t_dy, "dy/dt")

# Generate and save plot
t_vals = np.linspace(-2, 2, 500)
dx_vals = sp.lambdify(t, dx_dt, 'numpy')(t_vals)
dy_vals = sp.lambdify(t, dy_dt, 'numpy')(t_vals)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, dx_vals, label='dx/dt = 2t', linewidth=2)
plt.plot(t_vals, dy_vals, label='dy/dt = 3t^2 - 1', linewidth=2)
plt.axhline(0, color='black', linewidth=1, linestyle='--')

# Mark zeros
for i, pt in enumerate(critical_t_dx):
    plt.plot(float(pt), 0, 'ro', markersize=10, markeredgecolor='black', 
             label='dx/dt=0' if i==0 else "")
for i, pt in enumerate(critical_t_dy):
    plt.plot(float(pt), 0, 'gs', markersize=10, markeredgecolor='black', 
             label='dy/dt=0' if i==0 else "")

plt.xlabel('t')
plt.ylabel('Derivative Value')
plt.title('Derivatives dx/dt and dy/dt with Critical Points')
plt.legend()
plt.grid(True)
plt.savefig('derivatives_plot.png')
print("\nPlot saved to derivatives_plot.png")