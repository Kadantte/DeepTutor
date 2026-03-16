import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbolic variable
t = sp.symbols('t')

# Define parametric equations
x_t = t**3 - 3*t
y_t = t**2 - 1

# Compute expressions to verify Cartesian equation
# Target: x^2 = (y + 1)(y - 2)^2
lhs = x_t**2
rhs = (y_t + 1)*(y_t - 2)**2

# Simplify the difference to verify equality
difference = sp.simplify(lhs - rhs)
is_equal = difference == 0

# Print verification results
print("Parametric Equations:")
print(f"x = {x_t}")
print(f"y = {y_t}")
print("\nVerification of Cartesian Equation x^2 = (y + 1)(y - 2)^2:")
print(f"Computed x^2: {lhs}")
print(f"Computed (y + 1)(y - 2)^2: {rhs}")
print(f"Are they equal? {is_equal}")
print(f"Difference (simplified): {difference}")

# Identify curve type
print("\nCurve Identification:")
print("Type: Cubic Curve (specifically a Tschirnhausen Cubic or Nodal Cubic)")
print("Feature: Contains a loop formed between t = -sqrt(3) and t = sqrt(3)")

# Generate plot to visualize the curve
t_vals = np.linspace(-2.5, 2.5, 1000)
x_vals = t_vals**3 - 3*t_vals
y_vals = t_vals**2 - 1

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Parametric Curve', color='blue')
plt.title('Cartesian Curve Verification: x^2 = (y + 1)(y - 2)^2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axis('equal')
plt.savefig('curve_plot.png')
print("\nPlot saved as 'curve_plot.png'")