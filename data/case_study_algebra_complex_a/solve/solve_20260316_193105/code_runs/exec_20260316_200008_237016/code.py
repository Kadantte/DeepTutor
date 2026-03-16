import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return t**2 - 1

def y(t):
    return t**3 - t

# Specific t values requested
t_vals = [0, 1/np.sqrt(3), -1/np.sqrt(3), 1, -1]

print("Coordinates for Critical Points:")
print(f"{'t':<12} {'x(t)':<12} {'y(t)':<12}")
print("-" * 36)

computed_points = []
for t in t_vals:
    xt = x(t)
    yt = y(t)
    computed_points.append((xt, yt))
    print(f"{t:<12.6f} {xt:<12.6f} {yt:<12.6f}")

print("\nSymmetry Analysis:")
print("Comparing (x(t), y(t)) with (x(-t), y(-t))")

# Analytical check using numpy arrays for verification
t_range = np.linspace(-2, 2, 1000)
x_t = x(t_range)
y_t = y(t_range)
x_neg_t = x(-t_range)
y_neg_t = y(-t_range)

# Check for x-axis symmetry: (x, y) -> (x, -y)
# This requires x(-t) == x(t) and y(-t) == -y(t)
cond_x_axis = np.allclose(x_t, x_neg_t) and np.allclose(y_neg_t, -y_t)

# Check for y-axis symmetry: (x, y) -> (-x, y)
# This requires x(-t) == -x(t) and y(-t) == y(t)
cond_y_axis = np.allclose(x_neg_t, -x_t) and np.allclose(y_t, y_neg_t)

if cond_x_axis:
    print("Conclusion: The curve has x-axis symmetry.")
    print("Verification: (x(-t), y(-t)) equals (x(t), -y(t)).")
elif cond_y_axis:
    print("Conclusion: The curve has y-axis symmetry.")
    print("Verification: (x(-t), y(-t)) equals (-x(t), y(t)).")
else:
    print("Conclusion: No x-axis or y-axis symmetry detected via this method.")

# Plotting the curve and points
plt.figure(figsize=(8, 6))
t_plot = np.linspace(-1.5, 1.5, 400)
plt.plot(x(t_plot), y(t_plot), label='Curve: x=t^2-1, y=t^3-t')
plt.scatter([p[0] for p in computed_points], [p[1] for p in computed_points], 
            color='red', zorder=5, label='Critical Points')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve Analysis')
plt.legend()
plt.savefig('parametric_curve.png')
plt.close()

print("\nPlot saved to 'parametric_curve.png'")