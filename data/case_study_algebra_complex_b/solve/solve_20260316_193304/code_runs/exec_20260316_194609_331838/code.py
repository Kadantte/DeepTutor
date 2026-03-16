import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Define symbols
    t, t1, t2 = sp.symbols('t t1 t2', real=True)

    # Define parametric equations
    # Inferred from the condition: t = +/- sqrt(3) maps to (0, 2)
    # Standard curve fitting this description: x = t^2 - 3, y = t^3 - 3t + 2
    x = t**2 - 3
    y = t**3 - 3*t + 2

    print("Parametric Equations:")
    print(f"x(t) = {x}")
    print(f"y(t) = {y}")
    print("-" * 30)

    # 1. Verify specific points for t = sqrt(3) and t = -sqrt(3)
    t_val_pos = sp.sqrt(3)
    t_val_neg = -sp.sqrt(3)

    x_pos = sp.simplify(x.subs(t, t_val_pos))
    y_pos = sp.simplify(y.subs(t, t_val_pos))
    x_neg = sp.simplify(x.subs(t, t_val_neg))
    y_neg = sp.simplify(y.subs(t, t_val_neg))

    print(f"Verification for t = sqrt(3):")
    print(f"x({t_val_pos}) = {x_pos}")
    print(f"y({t_val_pos}) = {y_pos}")
    print(f"Point: ({x_pos}, {y_pos})")
    print()

    print(f"Verification for t = -sqrt(3):")
    print(f"x({t_val_neg}) = {x_neg}")
    print(f"y({t_val_neg}) = {y_neg}")
    print(f"Point: ({x_neg}, {y_neg})")
    print()

    if x_pos == 0 and y_pos == 2 and x_neg == 0 and y_neg == 2:
        print("Confirmed: Both t values yield the same point (0, 2).")
    else:
        print("Warning: Points do not match expected (0, 2).")
    print("-" * 30)

    # 2. Check for other pairs of distinct t values
    print("Checking for other distinct pairs (t1, t2) such that P(t1) = P(t2)...")
    
    # Equations for self-intersection
    eq1 = sp.Eq(x.subs(t, t1), x.subs(t, t2))
    eq2 = sp.Eq(y.subs(t, t1), y.subs(t, t2))
    
    # Solve x(t1) = x(t2) => t1^2 = t2^2 => t1 = t2 or t1 = -t2
    # For distinct pairs, we require t1 != t2, so we substitute t1 = -t2
    eq2_sub = eq2.subs(t1, -t2)
    
    # Solve for t2
    solutions = sp.solve(eq2_sub, t2)
    
    distinct_pairs = []
    target_pair = tuple(sorted([float(-sp.sqrt(3)), float(sp.sqrt(3))]))
    
    for sol in solutions:
        if sol.is_real:
            val = float(sol)
            if abs(val) > 1e-6: # Exclude t=0 case where t1=t2=0
                pair = tuple(sorted([-val, val]))
                # Check uniqueness
                if not any(abs(pair[0] - p[0]) < 1e-6 for p in distinct_pairs):
                    distinct_pairs.append(pair)
    
    if distinct_pairs:
        print(f"Found distinct pairs (t1, t2): {distinct_pairs}")
        others = [p for p in distinct_pairs if abs(p[0] - target_pair[0]) > 1e-6]
        if others:
            print(f"Other pairs exist besides +/- sqrt(3): {others}")
        else:
            print("No other pairs found besides t = +/- sqrt(3).")
    else:
        print("No distinct pairs found.")
    print("-" * 30)

    # 3. Plot the curve
    t_vals = np.linspace(-2.5, 2.5, 500)
    x_vals = t_vals**2 - 3
    y_vals = t_vals**3 - 3*t_vals + 2

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='x = t^2 - 3, y = t^3 - 3t + 2')
    plt.plot(0, 2, 'ro', label='Intersection (0, 2)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title('Parametric Curve Self-Intersection Verification')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('self_intersection_plot.png')
    print("Plot saved to 'self_intersection_plot.png'")

if __name__ == "__main__":
    main()