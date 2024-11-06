import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function f(q) = 2q^3 - 40q^2 + 90
def f(q):
    return 2*q**3 - 40*q**2 + 90

# Generate q values from -10 to 30 for plotting
q_values = np.linspace(-10, 30, 500)
f_values = f(q_values)

# Use fsolve to find the roots by providing initial guesses
initial_guesses = [-10, 5, 20]  # Provide different guesses for different roots
roots = fsolve(f, initial_guesses)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8,6))

fig.patch.set_facecolor('#F8E9F8')
ax.set_facecolor('#E6F2FF')


ax.plot(q_values, f_values, label=r'$f(q) = 2q^3 - 40q^2 + 90$', color='purple')
ax.axhline(0, color='black', linewidth=1)  # Horizontal line at f(q) = 0
ax.axvline(0, color='black', linewidth=1)  # Vertical line at q = 0

# Plot the roots where f(q) = 0 with red dots
for root in roots:
    ax.plot(root, 0, 'ro', label='Root: q={:.2f}'.format(root))

# Labeling the plot
ax.set_title("Graph of $f(q) = 2q^3 - 40q^2 + 90$ with Roots")
ax.set_xlabel("q")
ax.set_ylabel("f(q)")
ax.grid(True)
ax.legend()

# Show the plot
plt.show()

# Print the roots
print("Roots of the equation:", roots)
