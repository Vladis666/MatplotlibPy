import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = -0.5  # Coefficient of demand curve
b = 60    # Constant term of demand curve
CF = 3    # Fixed costs
CV = 8    # Variable costs per unit
Q_max = 100  # Maximum production capacity

# Functions
def price(Q):
    """ Price as a function of quantity based on the linear demand curve. """
    return a * Q + b

def revenue(Q):
    """ Revenue as a function of quantity. """
    return price(Q) * Q

def cost(Q):
    """ Total cost as a function of quantity. """
    return CF + CV * Q

def profit(Q):
    """ Profit as a function of quantity. """
    return revenue(Q) - cost(Q)

# Generate production quantity values
Q_values = np.linspace(0, Q_max, 100)

# Compute profit for each quantity
profits = profit(Q_values)

# Find the quantity that maximizes profit
Q_optimal = Q_values[np.argmax(profits)]
max_profit = max(profits)

# Print results and formulas
print("Demand curve: P(Q) = aQ + b, where a =", a, "and b =", b)
print("Revenue: R(Q) = P(Q) * Q")
print("Cost function: C(Q) = CF + CV * Q, where CF =", CF, "and CV =", CV)
print("Profit: Π(Q) = R(Q) - C(Q)")
print(f"Optimal production quantity for maximum profit: {Q_optimal:.2f} units")
print(f"Maximum profit: {max_profit:.2f} currency units")

# Plot style adjustments
fig, ax = plt.subplots(figsize=(8, 6))

# Apply the desired color style
fig.patch.set_facecolor('#F8E9F8')  # Background color of the figure
ax.set_facecolor('#E6F2FF')  # Background color of the plot

# Plot the profit curve
ax.plot(Q_values, profits, label="Profit", color='purple', linewidth=2)

# Highlight the optimal production point and maximum profit
ax.axvline(Q_optimal, color='red', linestyle='--', label=f"Optimal Q = {Q_optimal:.2f}", linewidth=1.5)
ax.axhline(max_profit, color='green', linestyle='--', label=f"Max Profit = {max_profit:.2f}", linewidth=1.5)

# Label the plot
ax.set_title("Profit vs Production Quantity", fontsize=14, fontweight='bold')
ax.set_xlabel("Production Quantity (Q)", fontsize=12)
ax.set_ylabel("Profit", fontsize=12)
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Additional text showing key formulas on the plot
textstr = '\n'.join((
    r'$P(Q) = aQ + b$',
    r'$R(Q) = P(Q) \times Q$',
    r'$C(Q) = CF + CV \times Q$',
    r'$\Pi(Q) = R(Q) - C(Q)$',
    f'$a = {a}$, $b = {b}$',
    f'$CF = {CF}$, $CV = {CV}$'
))
props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

# Legend
ax.legend(loc="upper right", fontsize=10)

# Show the plot
plt.show()
