import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def main():
    # Define symbolic variable
    t = sp.symbols('t')

    # Define parametric equations
    x_t = t**2 - 1
    y_t = t**3 - t

    # 1. Verify Symmetry
    x_neg_t = x_t.subs(t, -t)
    y_neg_t = y_t.subs(t, -t)

    sym_x = sp.simplify(x_neg_t - x_t) == 0
    sym_y = sp.simplify(y_neg_t + y_t) == 0

    print("Symmetry Verification:")
    print(f"x(-t) = x(t): {sym_x}")
    print(f"y(-t) = -y(t): {sym_y}")
    if sym_x and sym_y:
        print("Conclusion: The curve is symmetric with respect to the x-axis.")
    else:
        print("Conclusion: Symmetry conditions not met.")

    # 2. Compute Key Geometric Points
    
    # Crossing Point (Self-intersection)
    # Solve for t1 != t2 such that x(t1)=x(t2) and y(t1)=y(t2)
    t1, t2 = sp.symbols('t1 t2')
    eq1 = (t1**2 - 1) - (t2**2 - 1)
    eq2 = (t1**3 - t1) - (t2**3 - t2)
    # From eq1: t1^2 = t2^2. Since t1 != t2, t1 = -t2.
    # Substitute t2 = -t1 into eq2
    sol_crossing = sp.solve(eq2.subs(t2, -t1), t1)
    crossing_coords = set()
    
    print("\nCrossing Point(s):")
    for val in sol_crossing:
        if val != 0 and val.is_real: 
            t_val = float(val)
            x_val = float(x_t.subs(t, val))
            y_val = float(y_t.subs(t, val))
            crossing_coords.add((round(x_val, 4), round(y_val, 4)))
    
    for cx, cy in crossing_coords:
        print(f"Point: ({cx}, {cy})")

    # Local Extrema and Vertices
    # dx/dt = 0 (Vertical tangent / Vertex in x)
    dx_dt = sp.diff(x_t, t)
    crit_x = sp.solve(dx_dt, t)

    # dy/dt = 0 (Horizontal tangent / Local extrema in y)
    dy_dt = sp.diff(y_t, t)
    crit_y = sp.solve(dy_dt, t)

    print("\nCritical Points (Vertical Tangent / Vertex):")
    vertex_points = []
    for val in crit_x:
        if val.is_real:
            t_val = float(val)
            x_val = float(x_t.subs(t, val))
            y_val = float(y_t.subs(t, val))
            vertex_points.append((t_val, x_val, y_val))
            print(f"t = {t_val:.4f} -> Point: ({x_val:.4f}, {y_val:.4f})")

    print("\nCritical Points (Horizontal Tangent / Local Extrema):")
    extrema_points = []
    for val in crit_y:
        if val.is_real:
            t_val = float(val)
            x_val = float(x_t.subs(t, val))
            y_val = float(y_t.subs(t, val))
            extrema_points.append((t_val, x_val, y_val))
            print(f"t = {t_val:.4f} -> Point: ({x_val:.4f}, {y_val:.4f})")

    # 3. Generate Parametric Plot
    t_vals = np.linspace(-2, 2, 1000)
    x_vals = t_vals**2 - 1
    y_vals = t_vals**3 - t_vals

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, 'b-', label='x=t^2-1, y=t^3-t', linewidth=2)

    # Add Direction Arrows
    # Place arrows at specific t intervals to show flow
    arrow_t_vals = [-1.5, -0.5, 0.5, 1.5]
    for at in arrow_t_vals:
        # Calculate position
        ax = at**2 - 1
        ay = at**3 - at
        # Calculate next position for direction
        dt = 0.1
        at_next = at + dt
        ax_next = at_next**2 - 1
        ay_next = at_next**3 - at_next
        
        plt.annotate('', xy=(ax_next, ay_next), xytext=(ax, ay),
                     arrowprops=dict(arrowstyle='->', color='red', lw=2))

    # Label Critical Points
    # Crossing Point (0,0)
    plt.plot(0, 0, 'ko', markersize=8)
    plt.text(0.1, 0.15, 'Crossing (0,0)', fontsize=9, color='black', bbox=dict(facecolor='white', alpha=0.7))

    # Vertex (-1, 0)
    plt.plot(-1, 0, 'go', markersize=8)
    plt.text(-1.1, 0.15, 'Vertex (-1,0)', fontsize=9, color='green', bbox=dict(facecolor='white', alpha=0.7))

    # Extrema
    for t_val, x_val, y_val in extrema_points:
        plt.plot(x_val, y_val, 'ro', markersize=8)
        label = f'Extrema\n({x_val:.2f},{y_val:.2f})'
        # Adjust text position slightly to avoid overlap
        offset_x = 0.05 if x_val > -1 else -0.15
        plt.text(x_val + offset_x, y_val, label, fontsize=8, color='red', bbox=dict(facecolor='white', alpha=0.7))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Parametric Curve: x=t^2-1, y=t^3-t')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.tight_layout()
    plt.savefig('parametric_curve.png')
    plt.close()

    print("\nPlot saved as 'parametric_curve.png'")

if __name__ == "__main__":
    main()