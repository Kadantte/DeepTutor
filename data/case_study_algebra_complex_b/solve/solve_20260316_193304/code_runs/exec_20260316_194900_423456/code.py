import sympy as sp

t, x, y = sp.symbols('t x y')

# Define the parametric equations as polynomials equal to zero
# x = t^3 - 3t  =>  t^3 - 3t - x = 0
# y = t^2 - 1   =>  t^2 - 1 - y = 0
poly1 = t**3 - 3*t - x
poly2 = t**2 - 1 - y

# Eliminate parameter t using the resultant method
implicit_equation = sp.resultant(poly1, poly2, t)

# Simplify the resulting equation
implicit_equation = sp.simplify(implicit_equation)

# Print the result to stdout
print(implicit_equation)