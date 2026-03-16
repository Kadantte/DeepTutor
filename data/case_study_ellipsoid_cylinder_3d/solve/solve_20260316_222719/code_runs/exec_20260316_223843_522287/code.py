import numpy as np
import matplotlib.pyplot as plt

# Ellipsoid parameters: x^2/a^2 + y^2/b^2 + z^2/c^2 = 1
# Given z-range [-4, 4], so c = 4.
# Assuming a = 5.0, b = 5.0 for concrete calculation.
a = 5.0
b = 5.0
c = 4.0

# Cylinder parameters: x^2/rx^2 + y^2/ry^2 = 1
# Assuming rx = 2.0, ry = 2.0 to verify containment condition.
rx_cyl = 2.0
ry_cyl = 2.0

# Target z values
z_mag = 2 * np.sqrt(2)
z_values = [-z_mag, z_mag]

# 1. Ellipsoid z-bounds
z_min = -c
z_max = c
z_bounds = (z_min, z_max)

# 2. Verify z values lie within z-bounds
within_bounds = all(z_min <= z <= z_max for z in z_values)

# 3. Compute ellipsoid cross-section semi-axes at z = +/- 2*sqrt(2)
# Cross-section equation: x^2/A^2 + y^2/B^2 = 1 - z^2/c^2
# Semi-axes: A = a * sqrt(1 - z^2/c^2), B = b * sqrt(1 - z^2/c^2)
z_sq = z_mag ** 2
c_sq = c ** 2
scale_factor = np.sqrt(1 - z_sq / c_sq)

a_eff = a * scale_factor
b_eff = b * scale_factor

# 4. Check cylinder containment
# Cylinder lies inside if its semi-axes <= ellipsoid cross-section semi-axes
cylinder_inside = (rx_cyl <= a_eff) and (ry_cyl <= b_eff)

# Print Results
print(f"Ellipsoid Parameters: a={a}, b={b}, c={c}")
print(f"Ellipsoid z-bounds: [{z_min}, {z_max}]")
print(f"Target z values: +/- {z_mag:.4f} (approx +/- {z_mag:.2f})")
print(f"Verification 1: z values within z-bounds? {within_bounds}")
print(f"Calculation: scale_factor = sqrt(1 - {z_sq}/{c_sq}) = {scale_factor:.4f}")
print(f"Ellipsoid cross-section semi-axes at z=+/-{z_mag:.2f}:")
print(f"  a_eff (x-axis) = {a_eff:.4f}")
print(f"  b_eff (y-axis) = {b_eff:.4f}")
print(f"Cylinder semi-axes: rx={rx_cyl}, ry={ry_cyl}")
print(f"Verification 2: Cylinder inside ellipsoid cross-section? {cylinder_inside}")

# Plotting
theta = np.linspace(0, 2 * np.pi, 200)
x_ell = a_eff * np.cos(theta)
y_ell = b_eff * np.sin(theta)
x_cyl = rx_cyl * np.cos(theta)
y_cyl = ry_cyl * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x_ell, y_ell, 'b-', linewidth=2, label=f'Ellipsoid Cross-Section')
plt.plot(x_cyl, y_cyl, 'r--', linewidth=2, label=f'Cylinder Cross-Section')
plt.fill(x_cyl, y_cyl, color='red', alpha=0.1)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.legend()
plt.title(f'Cross-Section at z = {z_mag:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig('cross_section_verification.png')
plt.close()