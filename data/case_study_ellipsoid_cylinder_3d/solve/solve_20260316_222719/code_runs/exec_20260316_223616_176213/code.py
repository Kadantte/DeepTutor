import sympy as sp

def solve_intersection():
    # Define symbols
    x, y, z = sp.symbols('x y z')
    
    # Given relationship: 36x^2 + 16y^2 = 4 * (9x^2 + 4y^2)
    # Cylinder equation: 9x^2 + 4y^2 = 18
    cylinder_expr_value = 18
    
    # Calculate the value of the term 36x^2 + 16y^2 based on the relationship
    # 36x^2 + 16y^2 = 4 * (18)
    xy_term_value = 4 * cylinder_expr_value
    
    # Ellipsoid equation: 36x^2 + 16y^2 + 9z^2 = 144
    # Substitute the calculated xy_term_value into the ellipsoid equation
    # xy_term_value + 9z^2 = 144
    z_equation = sp.Eq(xy_term_value + 9 * z**2, 144)
    
    # Solve for z
    z_solutions = sp.solve(z_equation, z)
    
    # Print results
    print(f"Given: 9x^2 + 4y^2 = {cylinder_expr_value}")
    print(f"Derived: 36x^2 + 16y^2 = 4 * {cylinder_expr_value} = {xy_term_value}")
    print(f"Substituted into ellipsoid: {xy_term_value} + 9z^2 = 144")
    print(f"Simplified: 9z^2 = {144 - xy_term_value}")
    print(f"Solutions for z: {z_solutions}")
    
    # Print numerical approximations
    print(f"Numerical values: {[sol.evalf() for sol in z_solutions]}")

if __name__ == "__main__":
    solve_intersection()