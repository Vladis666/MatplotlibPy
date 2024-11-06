import pulp
import numpy as np
import matplotlib.pyplot as plt

# Supply (number of units available at each supplier)
supply = [140, 180, 160, 200, 190]  # Adding supply for A5 (190)

# Demand (number of units required by each consumer)
demand = [60, 70, 120, 130, 100]

# Transportation cost matrix including A5-B5
costs = np.array([
    [2, 3, 4, 2, 4],  # Costs from A1 to B1, B2, B3, B4, B5
    [8, 4, 1, 4, 1],  # Costs from A2 to B1, B2, B3, B4, B5
    [9, 7, 3, 7, 2],  # Costs from A3 to B1, B2, B3, B4, B5
    [5, 6, 7, 3, 4],  # Costs from A4 to B1, B2, B3, B4, B5
    [4, 3, 5, 6, 3]   # Costs from A5 to B1, B2, B3, B4, B5
])

# Number of suppliers and consumers
num_suppliers = len(supply)
num_consumers = len(demand)

# Create a linear programming problem
prob = pulp.LpProblem("Transportation_Problem_with_Constraints", pulp.LpMinimize)

# Create decision variables (how much to transport from each supplier to each consumer)
decision_vars = [[pulp.LpVariable(f'x_{i}_{j}', lowBound=0, cat='Continuous')
                  for j in range(num_consumers)] for i in range(num_suppliers)]

# Objective function: Minimize total transportation cost
prob += pulp.lpSum(costs[i][j] * decision_vars[i][j] for i in range(num_suppliers) for j in range(num_consumers))

# Constraints: Supply constraints (sum of shipments from each supplier must not exceed its supply)
for i in range(num_suppliers):
    prob += pulp.lpSum(decision_vars[i][j] for j in range(num_consumers)) <= supply[i]

# Constraints: Demand constraints (sum of shipments to each consumer must meet its demand)
for j in range(num_consumers):
    prob += pulp.lpSum(decision_vars[i][j] for i in range(num_suppliers)) == demand[j]

# Apply the exact volume constraint for A5-B5 (index A5 is 4, B5 is 4)
prob += decision_vars[4][4] == 50, "Exact_Volume_A5_B5"

# Solve the problem
prob.solve()

# Extract the results
solution = np.zeros((num_suppliers, num_consumers))
for i in range(num_suppliers):
    for j in range(num_consumers):
        solution[i][j] = pulp.value(decision_vars[i][j])

# Display the optimal solution and the total cost
total_cost = pulp.value(prob.objective)
print("Optimal Transportation Plan with Constraints:")
print(solution)
print(f"\nTotal Transportation Cost: {total_cost:.2f} UAH")

# Plot the supply and demand data, transportation costs, and solution
fig, axs = plt.subplots(2, 2, figsize=(7, 7))  # Slightly reduced figure size

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
im2 = axs[1, 1].imshow(solution, cmap='Greens')
axs[1, 1].set_title('Optimal Transportation Plan (Units)', fontweight='bold')
axs[1, 1].set_xticks(np.arange(num_consumers))
axs[1, 1].set_xticklabels([f'B{i+1}' for i in range(num_consumers)])
axs[1, 1].set_yticks(np.arange(num_suppliers))
axs[1, 1].set_yticklabels([f'A{i+1}' for i in range(num_suppliers)])
fig.colorbar(im2, ax=axs[1, 1])

# Adjust spacing between subplots to avoid overlap
plt.subplots_adjust(wspace=0.3, hspace=0.3)  # Increase horizontal and vertical space

plt.tight_layout()
plt.show()
