import numpy as np
import matplotlib.pyplot as plt

# Define the function f(q) = 2q^3 - 40q^2 + 90
def f(q):
    return 2*q**3 - 40*q**2 + 90

# Generate q values from -10 to 30 for plotting
q_values = np.linspace(-10, 30, 500)
f_values = f(q_values)

# Generate q values for finding the exact roots
q_roots = np.roots([2, -40, 0, 90])

# Define where the real roots are located
real_q_roots = [root.real for root in q_roots if np.isreal(root)]

# Create the figure
plt.figure(figsize=(8, 6))
plt.gcf().patch.set_facecolor('#F8E9F8')
plt.gca().set_facecolor('#E6F2FF')

# Plot the function in purple
plt.plot(q_values, f_values, label=r'$f(q) = 2q^3 - 40q^2 + 90$', color='purple')
plt.axhline(0, color='black', linewidth=1)  # Horizontal line at f(q) = 0
plt.axvline(0, color='black', linewidth=1)  # Vertical line at q = 0

# Plot the roots where f(q) = 0 with red dots
for root in real_q_roots:
    plt.plot(root, 0, 'ro', label='Root: q={:.2f}'.format(root))

# Labeling the plot
plt.title("Graph of $f(q) = 2q^3 - 40q^2 + 90$ with Roots")
plt.xlabel("q")
plt.ylabel("f(q)")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
