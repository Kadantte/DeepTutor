import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Parameters
a, b, c = 2.0, 3.0, 4.0
A_cyl, B_cyl = np.sqrt(2), 3.0 * np.sqrt(2) / 2.0
z_val = 2.0 * np.sqrt(2)

print("--- Verification Report ---")

# 1. Verify z bounds
within_bounds = abs(z_val) <= c
print(f"1. Z-value check: z = +/- {z_val:.4f}")
print(f"   Ellipsoid z-bounds: [-{c}, {c}]")
print(f"   Is within bounds? {within_bounds}")

# 2. Compute ellipsoid cross-section semi-axes at z = z_val
# Equation: x^2/a^2 + y^2/b^2 = 1 - z^2/c^2
z_term = (z_val ** 2) / (c ** 2)
rhs = 1.0 - z_term
# Effective semi-axes: a_eff = a * sqrt(rhs), b_eff = b * sqrt(rhs)
a_eff = a * np.sqrt(rhs)
b_eff = b * np.sqrt(rhs)

print(f"\n2. Cross-section at z = +/- {z_val:.4f}:")
print(f"   RHS of cross-section equation (1 - z^2/c^2): {rhs:.4f}")
print(f"   Ellipsoid cross-section semi-axes: a_eff = {a_eff:.4f}, b_eff = {b_eff:.4f}")
print(f"   Cylinder semi-axes:                A_cyl = {A_cyl:.4f}, B_cyl = {B_cyl:.4f}")

# Compare
match_a = np.isclose(a_eff, A_cyl)
match_b = np.isclose(b_eff, B_cyl)
print(f"\n3. Comparison:")
print(f"   a_eff matches A_cyl? {match_a}")
print(f"   b_eff matches B_cyl? {match_b}")
if match_a and match_b:
    print("   Conclusion: Cylinder passes through ellipsoid exactly at this cross-section.")
else:
    print("   Conclusion: Mismatch detected.")

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Ellipsoid mesh
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x_el = a * np.outer(np.cos(u), np.sin(v))
y_el = b * np.outer(np.sin(u), np.sin(v))
z_el = c * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_el, y_el, z_el, color='cyan', alpha=0.3, label='Ellipsoid')

# Cylinder mesh (limited height for visualization)
theta = np.linspace(0, 2 * np.pi, 50)
z_cyl = np.linspace(-c, c, 50)
Theta, Z_cyl = np.meshgrid(theta, z_cyl)
X_cyl = A_cyl * np.cos(Theta)
Y_cyl = B_cyl * np.sin(Theta)

ax.plot_surface(X_cyl, Y_cyl, Z_cyl, color='orange', alpha=0.3, label='Cylinder')

# Intersection circles at z = +/- z_val
theta_circle = np.linspace(0, 2 * np.pi, 100)
x_circle = a_eff * np.cos(theta_circle)
y_circle = b_eff * np.sin(theta_circle)
z_circle_pos = np.full_like(theta_circle, z_val)
z_circle_neg = np.full_like(theta_circle, -z_val)

ax.plot(x_circle, y_circle, z_circle_pos, color='red', linewidth=2, label='Intersection z=+2√2')
ax.plot(x_circle, y_circle, z_circle_neg, color='red', linewidth=2, label='Intersection z=-2√2')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ellipsoid and Cylinder Intersection Verification')
try:
    ax.set_box_aspect([a, b, c])
except AttributeError:
    pass

ax.set_xlim(-a, a)
ax.set_ylim(-b, b)
ax.set_zlim(-c, c)

plt.legend(loc='upper left')
plt.savefig('ellipsoid_cylinder_intersection.png')
print("\nPlot saved to 'ellipsoid_cylinder_intersection.png'")