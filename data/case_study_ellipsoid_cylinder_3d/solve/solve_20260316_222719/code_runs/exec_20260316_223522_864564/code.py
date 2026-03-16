import sympy as sp

x, y, z = sp.symbols('x y z')

# Define the common term found in both equations
# Cylinder: 9x^2 + 4y^2 = 18
common_term = 9*x**2 + 4*y**2
cylinder_val = 18

# Ellipsoid: 36x^2 + 16y^2 + 9z^2 = 144
# Rewrite ellipsoid using the common term: 4*(9x^2 + 4y^2) + 9z^2 = 144
ellipsoid_expr = 4 * common_term + 9*z**2 - 144

# Substitute the cylinder constraint into the ellipsoid equation
equation_z = ellipsoid_expr.subs(common_term, cylinder_val)

# Solve for z
z_solutions = sp.solve(equation_z, z)

print("The z-values where intersection occurs are:")
for sol in z_solutions:
    print(sol)