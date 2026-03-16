import sympy as sp

# Ellipsoid: 36x^2 + 16y^2 + 9z^2 = 144
# Standard form: x^2/a^2 + y^2/b^2 + z^2/c^2 = 1
# Divide by 144
a_sq = sp.Rational(144, 36)
b_sq = sp.Rational(144, 16)
c_sq = sp.Rational(144, 9)
a = sp.sqrt(a_sq)
b = sp.sqrt(b_sq)
c = sp.sqrt(c_sq)

# Elliptic Cylinder: 9x^2 + 4y^2 = 18
# Standard form: x^2/A^2 + y^2/B^2 = 1
# Divide by 18
A_sq = sp.Rational(18, 9)
B_sq = sp.Rational(18, 4)
A = sp.sqrt(A_sq)
B = sp.sqrt(B_sq)

print("Ellipsoid:")
print(f"Standard Form: x^2/{a_sq} + y^2/{b_sq} + z^2/{c_sq} = 1")
print(f"Semi-axes: a = {a}, b = {b}, c = {c}")
print()
print("Elliptic Cylinder:")
print(f"Standard Form: x^2/{A_sq} + y^2/{B_sq} = 1")
print(f"Semi-axes: A = {A}, B = {B}")