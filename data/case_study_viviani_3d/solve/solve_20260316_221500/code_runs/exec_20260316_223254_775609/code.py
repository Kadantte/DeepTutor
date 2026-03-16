import numpy as np
import matplotlib.pyplot as plt

def compute_intersection():
    # Parameter t in [0, 2*pi]
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # Cylinder parameterization
    x = 1 + np.cos(t)
    y = np.sin(t)
    
    # Compute z from sphere x^2 + y^2 + z^2 = 4
    # z^2 = 4 - (x^2 + y^2)
    z_sq = 4 - (x**2 + y**2)
    
    # Handle numerical precision issues
    z_sq = np.maximum(z_sq, 0)
    
    # Two branches for z
    z_pos = np.sqrt(z_sq)
    z_neg = -np.sqrt(z_sq)
    
    # Calculate Max and Min values
    x_max, x_min = np.max(x), np.min(x)
    y_max, y_min = np.max(y), np.min(y)
    
    # Consider both branches for z bounds
    z_all = np.concatenate([z_pos, z_neg])
    z_max, z_min = np.max(z_all), np.min(z_all)
    
    # Verification of closed loop
    # Check continuity (max difference between adjacent points)
    dx = np.max(np.abs(np.diff(x)))
    dy = np.max(np.abs(np.diff(y)))
    dz_pos = np.max(np.abs(np.diff(z_pos)))
    
    is_continuous = (dx < 0.1) and (dy < 0.1) and (dz_pos < 0.1)
    
    # Check periodicity (start point vs end point)
    # For the curve to be closed, P(0) must equal P(2*pi)
    # Note: At t=0 and t=2*pi, z=0 for both branches, so they meet.
    start_point = np.array([x[0], y[0], 0.0])
    end_point = np.array([x[-1], y[-1], 0.0])
    
    is_periodic = np.allclose(start_point, end_point)
    
    # Print Results
    print("Parametric Form:")
    print("x(t) = 1 + cos(t)")
    print("y(t) = sin(t)")
    print("z(t) = +/- sqrt(2 - 2*cos(t))")
    print("-" * 30)
    print("Maximum values:")
    print(f"x_max: {x_max:.4f}")
    print(f"y_max: {y_max:.4f}")
    print(f"z_max: {z_max:.4f}")
    print("-" * 30)
    print("Minimum values:")
    print(f"x_min: {x_min:.4f}")
    print(f"y_min: {y_min:.4f}")
    print(f"z_min: {z_min:.4f}")
    print("-" * 30)
    print("Verification:")
    print(f"Continuous: {is_continuous}")
    print(f"Periodic (Closed): {is_periodic}")
    print("Note: The full single closed loop (Viviani's curve) requires t in [0, 4*pi] with z = 2*sin(t/2).")
    print("The range [0, 2*pi] covers the projection once, resulting in two symmetric branches meeting at z=0.")
    
    # Plotting
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot upper branch
    ax.plot(x, y, z_pos, 'b', label='z > 0', linewidth=2)
    # Plot lower branch
    ax.plot(x, y, z_neg, 'r', label='z < 0', linewidth=2)
    
    # Plot sphere wireframe for context
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    xs = 2 * np.outer(np.cos(u), np.sin(v))
    ys = 2 * np.outer(np.sin(u), np.sin(v))
    zs = 2 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(xs, ys, zs, color='gray', alpha=0.1)
    
    # Plot cylinder wireframe for context
    theta = np.linspace(0, 2 * np.pi, 50)
    h = np.linspace(-2, 2, 50)
    theta_grid, h_grid = np.meshgrid(theta, h)
    xc = 1 + np.cos(theta_grid)
    yc = np.sin(theta_grid)
    zc = h_grid
    ax.plot_wireframe(xc, yc, zc, color='green', alpha=0.1)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Intersection Curve: Cylinder and Sphere')
    ax.legend()
    ax.set_box_aspect([1, 1, 1])
    
    plt.savefig('intersection_curve.png')
    print("-" * 30)
    print("Plot saved to 'intersection_curve.png'")

if __name__ == "__main__":
    compute_intersection()