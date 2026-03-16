import sympy as sp

t, x, y, u = sp.symbols('t x y u')

# Parametric equations
x_expr = t**3 - 3*t
y_expr = t**2 - 1

# Step 1: Solve y = t^2 - 1 for t^2
# We define u = t^2, so u = y + 1
u_sub = y + 1

# Step 2: Express x^2 in terms of u
# x = t(t^2 - 3) => x^2 = t^2 * (t^2 - 3)^2 => x^2 = u * (u - 3)^2
x_sq_u = u * (u - 3)**2

# Step 3: Substitute u with y + 1
rhs = x_sq_u.subs(u, u_sub)

# Construct the implicit equation
implicit_equation = sp.Eq(x**2, sp.expand(rhs))

# Output the results
print("Implicit Cartesian Equation:")
print(implicit_equation)
print("\nStandard Form (f(x,y) = 0):")
print(sp.Eq(x**2 - sp.expand(rhs), 0))