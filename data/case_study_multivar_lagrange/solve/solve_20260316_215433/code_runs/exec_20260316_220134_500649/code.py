import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Define symbols
    x, y, l = sp.symbols('x y l', real=True)

    # Define function and constraint
    f = x**2 + x*y + y**2
    # Constraint g(x,y) = x^2 + 4y^2 - 4 = 0
    
    # Lagrange Multiplier Equations
    # df/dx = l * dg/dx => 2x + y = l * 2x
    # df/dy = l * dg/dy => x + 2y = l * 8y
    # Constraint: x^2 + 4y^2 = 4
    
    eq1 = 2*x + y - l * 2*x
    eq2 = x + 2*y - l * 8*y
    eq3 = x**2 + 4*y**2 - 4

    # Solve the system
    solutions = sp.solve((eq1, eq2, eq3), (x, y, l))

    # Process solutions
    valid_points = []
    f_values = []
    lambdas = []

    print(f"{'Point (x, y)':<20} | {'Lambda':<10} | {'f(x,y)':<10} | {'Type'}")
    print("-" * 65)

    for sol in solutions:
        xv = sol[0]
        yv = sol[1]
        lv = sol[2]
        
        # Check if solution is real
        if xv.is_real and yv.is_real and lv.is_real:
            xv_val = float(xv)
            yv_val = float(yv)
            lv_val = float(lv)
            f_val = float(f.subs({x: xv, y: yv}))
            
            valid_points.append((xv_val, yv_val))
            f_values.append(f_val)
            lambdas.append(lv_val)
            
            print(f"({xv_val:7.4f}, {yv_val:7.4f})     | {lv_val:7.4f}     | {f_val:7.4f}     | Pending")

    # Identify Maxima and Minima
    if f_values:
        max_val = max(f_values)
        min_val = min(f_values)
        
        print("-" * 65)
        print("Classification Results:")
        for i in range(len(valid_points)):
            pt = valid_points[i]
            val = f_values[i]
            
            status = ""
            if abs(val - max_val) < 1e-6:
                status = "Maximum"
            elif abs(val - min_val) < 1e-6:
                status = "Minimum"
            else:
                status = "Intermediate"
            
            print(f"Point ({pt[0]:.4f}, {pt[1]:.4f}): f = {val:.4f} -> {status}")

        # Plotting
        t = np.linspace(0, 2*np.pi, 400)
        # Ellipse parameterization: x^2/4 + y^2/1 = 1 => x = 2cos(t), y = sin(t)
        xe = 2 * np.cos(t)
        ye = np.sin(t)

        plt.figure(figsize=(8, 6))
        plt.plot(xe, ye, 'k-', label='Constraint: $x^2 + 4y^2 = 4$')
        
        pts_arr = np.array(valid_points)
        
        # Determine colors based on max/min
        colors = []
        for val in f_values:
            if abs(val - max_val) < 1e-6:
                colors.append('red') # Max
            elif abs(val - min_val) < 1e-6:
                colors.append('blue') # Min
            else:
                colors.append('green')
        
        plt.scatter(pts_arr[:, 0], pts_arr[:, 1], c=colors, s=100, edgecolors='black', zorder=5, label='Critical Points')
        
        # Annotate
        for i, txt in enumerate([f"f={f_values[i]:.2f}" for i in range(len(f_values))]):
            plt.annotate(txt, (pts_arr[i, 0]+0.15, pts_arr[i, 1]+0.15), fontsize=9)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Lagrange Multipliers: Critical Points on Constraint')
        plt.axhline(0, color='gray', linewidth=0.5)
        plt.axvline(0, color='gray', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.axis('equal')
        plt.savefig('lagrange_solution.png')
        
    else:
        print("No real solutions found.")

if __name__ == "__main__":
    main()