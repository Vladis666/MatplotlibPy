from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coefficients of the objective function (negatives because linprog minimizes)
c = [-15, -5, -40, -10, -5, -30]

# Coefficients for the inequality constraints (Ax <= b)
A = [
    [9, 6, 6, 8, 5, 5],   # Material 1
    [11, 11, 6, 7, 9, 8], # Material 2
    [9, 10, 9, 8, 6, 8],  # Material 3
    [6, 9, 9, 8, 10, 9],  # Material 4
    [8, 6, 8, 6, 6, 4]    # Time constraints
]

# Right-hand side of the inequality constraints
b = [6500, 9350, 8550, 9050, 6500]

# Bounds for each variable (non-negative constraint)
x_bounds = [(0, None)] * 6

# Solving the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Check if the problem was solved successfully
if res.success:
    quantities = res.x
    print("Number of units for each product:")
    for i, x in enumerate(quantities, 1):
        print(f"X{i}: {x:.2f}")
    max_profit = -res.fun
    print(f"Maximum profit: {max_profit:.2f} currency units")
else:
    print("The problem does not have a solution")

# Graphs

# 1. Bar chart for the quantities of each product
products = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']
plt.figure(figsize=(10, 6))
plt.bar(products, quantities, color='lightblue')
plt.xlabel('Product Type')
plt.ylabel('Number of Units Produced')
plt.title('Optimal Number of Units to Produce for Each Product Type')
plt.show()

# 2. Pie chart for resource usage of Material 1
resource_usage = [9*quantities[0], 6*quantities[1], 6*quantities[2], 8*quantities[3], 5*quantities[4], 5*quantities[5]]
total_available_material_1 = 6500
plt.figure(figsize=(8, 8))
plt.pie(resource_usage, labels=products, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
plt.title('Material 1 Usage by Product Type')
plt.show()

# 3. Bar chart for profit contribution
profits = [15*quantities[0], 5*quantities[1], 40*quantities[2], 10*quantities[3], 5*quantities[4], 30*quantities[5]]
plt.figure(figsize=(10, 6))
plt.bar(products, profits, color='green')
plt.xlabel('Product Type')
plt.ylabel('Profit Contribution (currency units)')
plt.title('Profit Contribution by Product Type')
plt.show()

# 4. Bar chart for Material 1 usage and remaining capacity
material_1_usage = sum(resource_usage)
material_1_left = total_available_material_1 - material_1_usage
plt.figure(figsize=(8, 6))
plt.bar(['Used Material 1', 'Remaining Material 1'], [material_1_usage, material_1_left], color=['red', 'lightgreen'])
plt.ylabel('Material 1 (kg)')
plt.title('Material 1 Usage and Remaining Capacity')
plt.show()

# 5. Analysis of results (summary)
# Create a summary bar chart showing all constraints and how much is used
plt.figure(figsize=(10, 6))

# Total resource usage for each material and time
materials_usage = [
    sum([9*quantities[0], 6*quantities[1], 6*quantities[2], 8*quantities[3], 5*quantities[4], 5*quantities[5]]),  # Material 1
    sum([11*quantities[0], 11*quantities[1], 6*quantities[2], 7*quantities[3], 9*quantities[4], 8*quantities[5]]),  # Material 2
    sum([9*quantities[0], 10*quantities[1], 9*quantities[2], 8*quantities[3], 6*quantities[4], 8*quantities[5]]),  # Material 3
    sum([6*quantities[0], 9*quantities[1], 9*quantities[2], 8*quantities[3], 10*quantities[4], 9*quantities[5]]),  # Material 4
    sum([8*quantities[0], 6*quantities[1], 8*quantities[2], 6*quantities[3], 6*quantities[4], 4*quantities[5]])    # Time
]

# Plot usage and total available
total_available = [6500, 9350, 8550, 9050, 6500]
constraints = ['Material 1', 'Material 2', 'Material 3', 'Material 4', 'Time']

plt.bar(constraints, materials_usage, color='orange', label='Used')
plt.bar(constraints, [total - used for total, used in zip(total_available, materials_usage)], bottom=materials_usage, color='lightgray', label='Remaining')

plt.xlabel('Constraints')
plt.ylabel('Units')
plt.title('Resource Usage vs Available')
plt.legend()
plt.show()
