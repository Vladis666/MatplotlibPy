import pulp
import numpy as np
import matplotlib.pyplot as plt

# Supply (number of units available at each supplier)
supply = [140, 180, 160]

# Demand (number of units required by each consumer)
demand = [60, 70, 120, 130, 100]

# Transportation time matrix (in hours)
times = np.array([
    [2, 3, 4, 2, 4],  # Times from A1 to B1, B2, B3, B4, B5
    [8, 4, 1, 4, 1],  # Times from A2 to B1, B2, B3, B4, B5
    [9, 7, 3, 7, 2]   # Times from A3 to B1, B2, B3, B4, B5
])

# Number of suppliers and consumers
num_suppliers = len(supply)
num_consumers = len(demand)

# Create a linear programming problem
prob = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Create decision variables (how much to transport from each supplier to each consumer)
decision_vars = [[pulp.LpVariable(f'x_{i + 1}_{j + 1}', lowBound=0, cat='Continuous')
                  for j in range(num_consumers)] for i in range(num_suppliers)]

# Objective function: Minimize total transportation time
prob += pulp.lpSum(times[i][j] * decision_vars[i][j] for i in range(num_suppliers) for j in range(num_consumers))

# Constraints: Supply constraints (sum of shipments from each supplier must not exceed its supply)
for i in range(num_suppliers):
    prob += pulp.lpSum(decision_vars[i][j] for j in range(num_consumers)) <= supply[i], f"Supply_Constraint_A{i + 1}"

# Constraints: Demand constraints (sum of shipments to each consumer must meet its demand)
for j in range(num_consumers):
    prob += pulp.lpSum(decision_vars[i][j] for i in range(num_suppliers)) == demand[j], f"Demand_Constraint_B{j + 1}"

# Solve the problem
prob.solve()

# Extract the results
solution = np.zeros((num_suppliers, num_consumers))
for i in range(num_suppliers):
    for j in range(num_consumers):
        solution[i][j] = pulp.value(decision_vars[i][j])

# Display the optimal solution and the total weighted transportation time
total_weighted_time = pulp.value(prob.objective)
print("Optimal Transportation Plan:")
print(solution)
print(f"\nTotal Weighted Transportation Time (units transported * time): {total_weighted_time:.2f} hours")

# Minimize the maximum transportation time
# Add a variable to represent the maximum transportation time across all routes
max_time_var = pulp.LpVariable('max_time', lowBound=0, cat='Continuous')

# Create a new problem for minimizing the maximum transportation time
prob_max_time = pulp.LpProblem("Minimize_Max_Transportation_Time", pulp.LpMinimize)

# Add constraints to ensure no route's time exceeds the maximum transportation time variable
for i in range(num_suppliers):
    for j in range(num_consumers):
        prob_max_time += decision_vars[i][j] * times[i][j] <= max_time_var

# Add supply and demand constraints
for i in range(num_suppliers):
    prob_max_time += pulp.lpSum(decision_vars[i][j] for j in range(num_consumers)) <= supply[i], f"Supply_Constraint_A{i + 1}"

for j in range(num_consumers):
    prob_max_time += pulp.lpSum(decision_vars[i][j] for i in range(num_suppliers)) == demand[j], f"Demand_Constraint_B{j + 1}"

# Set the objective to minimize the maximum transportation time
prob_max_time += max_time_var

# Solve the new problem to minimize the maximum time
prob_max_time.solve()

# Get the value of the minimized maximum transportation time
minimized_max_time = pulp.value(max_time_var)
print(f"Minimized Maximum Transportation Time: {minimized_max_time:.2f} hours")
#Total Weighted Transportation Time 1200 E Sum  A1*B1+A2*B2 ... etc optional
print(f"\nTotal Weighted Transportation Time (units transported * time): {total_weighted_time:.2f} hours")


# Plot the supply and demand data, transportation times, and solution
fig, axs = plt.subplots(2, 2, figsize=(9, 9))

# Apply background color to the figure and the individual axes
fig.patch.set_facecolor('#F8E9F8')  # Set figure background color
for ax in axs.flat:
    ax.set_facecolor('#E6F2FF')  # Set background color for the plots

# Plot supply data
axs[0, 0].bar([f'A{i + 1}' for i in range(num_suppliers)], supply, color='skyblue')
axs[0, 0].set_title('Supply (Units Available)', fontweight='bold')
axs[0, 0].set_ylabel('Units', fontweight='bold')
axs[0, 0].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Plot demand data
axs[0, 1].bar([f'B{i + 1}' for i in range(num_consumers)], demand, color='salmon')
axs[0, 1].set_title('Demand (Units Required)', fontweight='bold')
axs[0, 1].set_ylabel('Units', fontweight='bold')
axs[0, 1].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Plot transportation time matrix
im = axs[1, 0].imshow(times, cmap='Blues')
axs[1, 0].set_title('Transportation Times (hours)', fontweight='bold')
axs[1, 0].set_xticks(np.arange(num_consumers))
axs[1, 0].set_xticklabels([f'B{i + 1}' for i in range(num_consumers)])
axs[1, 0].set_yticks(np.arange(num_suppliers))
axs[1, 0].set_yticklabels([f'A{i + 1}' for i in range(num_suppliers)])
fig.colorbar(im, ax=axs[1, 0])

# Plot the optimal transportation plan
im2 = axs[1, 1].imshow(solution, cmap='Greens')
axs[1, 1].set_title('Optimal Transportation Plan (Units)', fontweight='bold')
axs[1, 1].set_xticks(np.arange(num_consumers))
axs[1, 1].set_xticklabels([f'B{i + 1}' for i in range(num_consumers)])
axs[1, 1].set_yticks(np.arange(num_suppliers))
axs[1, 1].set_yticklabels([f'A{i + 1}' for i in range(num_suppliers)])
fig.colorbar(im2, ax=axs[1, 1])

# Adjust spacing between subplots to avoid overlap
plt.subplots_adjust(wspace=0.3, hspace=0.3)  # Increase horizontal and vertical space

plt.tight_layout()
plt.show()
