import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# --- THE ALGORITHM (Math Logic) ---
print("Step 1: Defining the System Matrix")
A = np.array([[1, -2, -1, 6],
              [2, 2, -1, 1],
              [-1, -1, 2, 1]], dtype=float)
print(A)

print("\nStep 2: Forward Elimination (R2 - 2*R1) and (R3 + R1)")
A[1] = A[1] - 2*A[0]
A[2] = A[2] + A[0]
print(A)

print("\nStep 3: Final Elimination (2*R3 + R2)")
A[2] = 2*A[2] + A[1]
print(A)

# Solving for specific points
x3 = A[2,3] / A[2,2]
x2 = (A[1,3] - A[1,2]*x3) / A[1,1]
x1 = (A[0,3] - A[0,1]*x2 - A[0,2]*x3) / A[0,0]
print(f"\nFinal Result: x1={x1}, x2={x2}, x3={x3}")

# --- THE 3D CHART (Visualization) ---
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the planes
x = np.linspace(-2, 8, 20)
y = np.linspace(-7, 3, 20)
X, Y = np.meshgrid(x, y)

# Equations rearranged for Z (x3)
Z1 = X - 2*Y - 6          # x1 - 2x2 - x3 = 6
Z2 = 2*X + 2*Y - 1        # 2x1 + 2x2 - x3 = 1
Z3 = (X + Y + 1) / 2      # -x1 - x2 + 2x3 = 1

# Plotting the planes
ax.plot_surface(X, Y, Z1, alpha=0.4, color='cyan')
ax.plot_surface(X, Y, Z2, alpha=0.4, color='magenta')
ax.plot_surface(X, Y, Z3, alpha=0.4, color='yellow')

# Plot the specific solution point
ax.scatter(x1, x2, x3, color='black', s=200, label=f'Solution ({x1}, {x2}, {x3})')

ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('X3 Axis')
ax.set_title('3D Gaussian Elimination Result')
ax.legend()

print("\nDisplaying 3D Chart...")
plt.show()
