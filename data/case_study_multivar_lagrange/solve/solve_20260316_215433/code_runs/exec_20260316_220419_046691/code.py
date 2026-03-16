import numpy as np
import matplotlib.pyplot as plt

# 1. Symmetric Matrix Representation
# The quadratic form is f(x,y) = x^2 + xy + y^2
# This corresponds to the matrix equation v^T A v where v = [x, y]^T
# A = [[1, 0.5], [0.5, 1]]
A = np.array([[1.0, 0.5], [0.5, 1.0]])

print("1. Symmetric Matrix Representation:")
print(A)

# 2. Compute Eigenvalues and Eigenvectors
# Using eigh for symmetric matrices to ensure real eigenvalues
eigenvalues, eigenvectors = np.linalg.eigh(A)

# Sort eigenvalues in descending order for standard interpretation
# numpy.linalg.eigh returns eigenvalues in ascending order
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

lambda_1 = eigenvalues[0] # Larger eigenvalue
lambda_2 = eigenvalues[1] # Smaller eigenvalue
vec_1 = eigenvectors[:, 0]
vec_2 = eigenvectors[:, 1]

print("\n2. Eigenvalues and Eigenvectors (Principal Axes):")
print(f"Eigenvalues (sorted descending): {eigenvalues}")
print(f"Eigenvector for lambda={lambda_1:.4f}: {vec_1}")
print(f"Eigenvector for lambda={lambda_2:.4f}: {vec_2}")

# 3. Verify Positive Definite
# A matrix is positive definite if all eigenvalues are positive
is_positive_definite = np.all(eigenvalues > 0)
print(f"\n3. Positive Definite Verification: {is_positive_definite}")
if is_positive_definite:
    print("   Result: All eigenvalues are positive. Contours are ellipses.")
else:
    print("   Result: Not positive definite.")

# 4. Determine Aspect Ratio
# The contour equation in principal coordinates is lambda_1 * u^2 + lambda_2 * v^2 = C
# The semi-axis lengths are proportional to 1/sqrt(lambda)
# Major axis corresponds to the smaller eigenvalue (lambda_2)
# Minor axis corresponds to the larger eigenvalue (lambda_1)
# Aspect Ratio = Major Axis / Minor Axis = sqrt(lambda_1 / lambda_2)
aspect_ratio = np.sqrt(lambda_1 / lambda_2)
print(f"\n4. Aspect Ratio of Contour Ellipses (Major/Minor): {aspect_ratio:.4f}")

# Visualization
plt.figure(figsize=(8, 8))
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X**2 + X*Y + Y**2

# Plot contours
contours = plt.contour(X, Y, Z, levels=[0.5, 1.0, 1.5, 2.0], colors='blue', linewidths=1.5)
plt.clabel(contours, inline=True, fontsize=8)

# Plot Principal Axes
# Scale vectors to be visible on the plot
scale = 1.2 
origin = [0, 0]

# Major Axis (associated with smaller eigenvalue lambda_2)
plt.quiver(origin[0], origin[1], vec_2[0]*scale, vec_2[1]*scale, 
           angles='xy', scale_units='xy', scale=1, color='red', width=0.005, label=f'Major Axis (lambda={lambda_2:.2f})')

# Minor Axis (associated with larger eigenvalue lambda_1)
plt.quiver(origin[0], origin[1], vec_1[0]*scale, vec_1[1]*scale, 
           angles='xy', scale_units='xy', scale=1, color='green', width=0.005, label=f'Minor Axis (lambda={lambda_1:.2f})')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Quadratic Form $x^2 + xy + y^2$\nAspect Ratio: {aspect_ratio:.4f}')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.3)
plt.axis('equal')
plt.savefig('quadratic_form_analysis.png')
print("\nPlot saved to 'quadratic_form_analysis.png'")