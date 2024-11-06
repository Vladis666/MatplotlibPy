import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function f(q) = 2q^3 - 40q^2 + 90
def f(q):
    return 2*q**3 - 40*q**2 + 90

# Generate q values from -10 to 30 for plotting
q_values = np.linspace(-10, 30, 500)
f_values = f(q_values)

# Use np.roots to find all roots, including complex roots if they exist
coefficients = [2, -40, 0, 90]  # Coefficients of the polynomial 2q^3 - 40q^2 + 0q + 90
all_roots = np.roots(coefficients)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))


fig.patch.set_facecolor('#F8E9F8')
ax.set_facecolor('#E6F2FF')

# Plot the function
ax.plot(q_values, f_values, label=r'$f(q) = 2q^3 - 40q^2 + 90$', color='purple')  # Line color changed to purple
ax.axhline(0, color='black', linewidth=1)  # Horizontal line at f(q) = 0
ax.axvline(0, color='black', linewidth=1)  # Vertical line at q = 0

# Plot the roots where f(q) = 0 with red dots
for root in all_roots:
    ax.plot(root.real, 0, 'ro', label='Root: q={:.2f}'.format(root))  # Plot real part of roots
    if np.iscomplex(root):  # Check if the root is complex
        print(f"Complex root: {root}")

# Labeling the plot
ax.set_title("Graph of $f(q) = 2q^3 - 40q^2 + 90$ with Roots")
ax.set_xlabel("q")
ax.set_ylabel("f(q)")
ax.grid(True)
ax.legend()

# Show the plot
plt.show()

# Print all roots
print("Roots of the equation (including complex roots):", all_roots)
