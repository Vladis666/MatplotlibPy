import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Supply (number of units available at each supplier)
supply = [140, 180, 160]

# Demand (number of units required by each consumer)
demand = [60, 70, 120, 130, 100]

# Transportation cost matrix
costs = np.array([
    [2, 3, 4, 2, 4],  # Costs from A1 to B1, B2, B3, B4, B5
    [8, 4, 1, 4, 1],  # Costs from A2 to B1, B2, B3, B4, B5
    [9, 7, 3, 7, 2]   # Costs from A3 to B1, B2, B3, B4, B5
])

# Flatten the cost matrix to a 1D vector (since linprog works with 1D arrays)
cost_vector = costs.flatten()

# Number of suppliers and consumers
num_suppliers = len(supply)
num_consumers = len(demand)

# Create inequality constraints (Ax <= b)
# First, supply constraints (sum of shipments from each supplier <= supply[i])
A_supply = np.zeros((num_suppliers, num_suppliers * num_consumers))
for i in range(num_suppliers):
    A_supply[i, i * num_consumers:(i + 1) * num_consumers] = 1

b_supply = supply

# Second, demand constraints (sum of shipments to each consumer == demand[j])
A_demand = np.zeros((num_consumers, num_suppliers * num_consumers))
for j in range(num_consumers):
    A_demand[j, j::num_consumers] = 1

b_demand = demand

# Combine A_supply and A_demand into A_eq, and b_supply and b_demand into b_eq
A_eq = np.vstack([A_supply, A_demand])
b_eq = np.hstack([b_supply, b_demand])

# Bounds: all variables should be non-negative (x >= 0)
bounds = [(0, None) for _ in range(num_suppliers * num_consumers)]

# Solve the linear programming problem using linprog (minimize cost_vector * x)
result = linprog(cost_vector, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Reshape the result to the original supplier-consumer matrix form
solution_scipy = result.x.reshape((num_suppliers, num_consumers))

# Extract the total cost from the result
total_cost_scipy = result.fun

# Display the optimal solution and the total cost
print("Optimal Transportation Plan (scipy):")
print(solution_scipy)
print(f"\nTotal Transportation Cost (scipy): {total_cost_scipy:.2f} UAH")

# Plotting similar to the Pulp solution for comparison
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Apply background color to the figure and the individual axes
fig.patch.set_facecolor('#F8E9F8')  # Set figure background color
for ax in axs.flat:
    ax.set_facecolor('#E6F2FF')  # Set background color for the plots

# Plot supply data
axs[0, 0].bar([f'A{i+1}' for i in range(num_suppliers)], supply, color='skyblue')
axs[0, 0].set_title('Supply (Units Available)', fontweight='bold')
axs[0, 0].set_ylabel('Units', fontweight='bold')
axs[0, 0].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Plot demand data
axs[0, 1].bar([f'B{i+1}' for i in range(num_consumers)], demand, color='salmon')
axs[0, 1].set_title('Demand (Units Required)', fontweight='bold')
axs[0, 1].set_ylabel('Units', fontweight='bold')
axs[0, 1].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Plot transportation cost matrix
im = axs[1, 0].imshow(costs, cmap='Blues')
axs[1, 0].set_title('Transportation Costs (UAH per unit)', fontweight='bold')
axs[1, 0].set_xticks(np.arange(num_consumers))
axs[1, 0].set_xticklabels([f'B{i+1}' for i in range(num_consumers)])
axs[1, 0].set_yticks(np.arange(num_suppliers))
axs[1, 0].set_yticklabels([f'A{i+1}' for i in range(num_suppliers)])
fig.colorbar(im, ax=axs[1, 0])

# Plot the optimal transportation plan
im2 = axs[1, 1].imshow(solution_scipy, cmap='Greens')
axs[1, 1].set_title('Optimal Transportation Plan (Units)', fontweight='bold')
axs[1, 1].set_xticks(np.arange(num_consumers))
axs[1, 1].set_xticklabels([f'B{i+1}' for i in range(num_consumers)])
axs[1, 1].set_yticks(np.arange(num_suppliers))
axs[1, 1].set_yticklabels([f'A{i+1}' for i in range(num_suppliers)])
fig.colorbar(im2, ax=axs[1, 1])

plt.tight_layout()
plt.show()
