import sympy as sp

t = sp.symbols('t')
x = t**3 - 3*t
y = t**2 - 1

dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)

solutions_dx = sp.solve(dx_dt, t)
solutions_dy = sp.solve(dy_dt, t)

print("dx/dt =", dx_dt)
print("dy/dt =", dy_dt)
print("t where dx/dt = 0:", solutions_dx)
print("t where dy/dt = 0:", solutions_dy)