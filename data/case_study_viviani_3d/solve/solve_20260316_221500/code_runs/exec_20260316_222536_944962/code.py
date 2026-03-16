import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define symbolic variable
t = sp.symbols('t', real=True)

# Cylinder parameterization
x_t = 1 + sp.cos(t)
y_t = sp.sin(t)

# Assume Sphere Equation: x^2 + y^2 + z^2 = 4 (Viviani's Curve context)
# This is the standard sphere that intersects cleanly with cylinder (x-1)^2 + y^2 = 1
R_sphere = 2
x_sym, y_sym, z_sym = sp.symbols('x y z')
sphere_eq = x_sym**2 + y_sym**2 + z_sym**2 - R_sphere**2

# Substitute cylinder parameterization into sphere equation to find z(t)
# x^2 + y^2 = (1+cos(t))^2 + sin(t)^2 = 1 + 2cos(t) + cos^2(t) + sin^2(t) = 2 + 2cos(t)
# z^2 = 4 - (2 + 2cos(t)) = 2 - 2cos(t)
z_squared = R_sphere**2 - (x_t**2 + y_t**2)
z_t_pos = sp.sqrt(z_squared)
z_t_neg = -sp.sqrt(z_squared)

# Simplify z(t)
# 2 - 2cos(t) = 4sin^2(t/2)
z_t_simplified = sp.simplify(z_t_pos)

# Find extrema of y(t)
# y = sin(t), range [-1, 1]
y_max = 1
y_min = -1

# Find extrema of z(t)
# z^2 = 2(1 - cos(t)). Max when cos(t) = -1 => z^2 = 4 => z = +/- 2
# Min when cos(t) = 1 => z^2 = 0 => z = 0
# However, the curve exists in 3D space, so z ranges from -2 to 2 across the full intersection
z_max = 2
z_min = -2

# Identify where z reaches extrema
# z_max occurs when cos(t) = -1 => t = pi
# z_min (magnitude max negative) occurs when cos(t) = -1 => t = pi (for negative branch)
# z = 0 occurs when cos(t) = 1 => t = 0, 2pi

# Numerical evaluation for plotting
t_vals = np.linspace(0, 2 * np.pi, 500)
x_vals = 1 + np.cos(t_vals)
y_vals = np.sin(t_vals)
z_vals_pos = np.sqrt(2 - 2 * np.cos(t_vals))
z_vals_neg = -np.sqrt(2 - 2 * np.cos(t_vals))

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot upper branch
ax.plot(x_vals, y_vals, z_vals_pos, 'b', label='z > 0')
# Plot lower branch
ax.plot(x_vals, y_vals, z_vals_neg, 'r', label='z < 0')

# Plot cylinder surface for context (optional but helpful)
# Not plotting surface to keep code concise and focused on curve

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection Curve: Cylinder (x-1)^2+y^2=1 and Sphere x^2+y^2+z^2=4')
ax.legend()
ax.grid(True)

# Set equal aspect ratio
max_range = np.array([x_vals.max()-x_vals.min(), y_vals.max()-y_vals.min(), z_vals_pos.max()-z_vals_pos.min()]).max() / 2.0
mid_x = (x_vals.max()+x_vals.min()) * 0.5
mid_y = (y_vals.max()+y_vals.min()) * 0.5
mid_z = (z_vals_pos.max()+z_vals_neg.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.savefig('intersection_curve.png')

# Print results
print(f"Parametric Representation:")
print(f"x(t) = 1 + cos(t)")
print(f"y(t) = sin(t)")
print(f"z(t) = +/- sqrt(2 - 2*cos(t))  (derived from sphere x^2 + y^2 + z^2 = 4)")
print(f"\nExtrema Values:")
print(f"Maximum y: {y_max}")
print(f"Minimum y: {y_min}")
print(f"Maximum z: {z_max}")
print(f"Minimum z: {z_min}")
print(f"\nExtrema Locations (t in [0, 2pi]):")
print(f"y max at t = pi/2")
print(f"y min at t = 3*pi/2")
print(f"z max magnitude at t = pi (z = +/- 2)")
print(f"z = 0 at t = 0, 2*pi")

plt.close()