import numpy as np

A = np.array([[1, 0.5], [0.5, -1]])
eigenvalues = np.linalg.eigvals(A)

a = 1
b = 1
c = -1
discriminant = b**2 - 4*a*c

print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print(f"\nCoefficients: a={a}, b={b}, c={c}")
print(f"Discriminant (b^2 - 4ac): {discriminant}")

if discriminant > 0:
    print("Classification: Saddle Point")
else:
    print("Classification: Not a Saddle Point")

if np.prod(eigenvalues) < 0:
    print("Verification: Eigenvalues have opposite signs.")