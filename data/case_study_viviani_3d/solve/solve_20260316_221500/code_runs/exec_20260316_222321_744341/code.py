import sympy as sp

x, y, z = sp.symbols('x y z', real=True)

# Define the equations for the curve
# 1. Cylinder: (x-1)^2 + y^2 = 1
eq_cylinder = (x - 1)**2 + y**2 - 1
# 2. Sphere: x^2 + y^2 + z^2 = 4
eq_sphere = x**2 + y**2 + z**2 - 4

print("Intersection points of the curve with coordinate planes:\n")

# (1) Intersection with z=0 plane
sols_z0 = sp.solve([eq_cylinder, eq_sphere, z], (x, y, z), dict=True)
print("(1) z=0 plane:")
if sols_z0:
    for s in sols_z0:
        print(f"    ({s[x]}, {s[y]}, {s[z]})")
else:
    print("    No intersection points found.")

# (2) Intersection with y=0 plane
sols_y0 = sp.solve([eq_cylinder, eq_sphere, y], (x, y, z), dict=True)
print("\n(2) y=0 plane:")
if sols_y0:
    for s in sols_y0:
        print(f"    ({s[x]}, {s[y]}, {s[z]})")
else:
    print("    No intersection points found.")

# (3) Intersection with x=0 plane
sols_x0 = sp.solve([eq_cylinder, eq_sphere, x], (x, y, z), dict=True)
print("\n(3) x=0 plane:")
if sols_x0:
    for s in sols_x0:
        print(f"    ({s[x]}, {s[y]}, {s[z]})")
else:
    print("    No intersection points found.")