import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define the input data (inter-industry relationships matrix X)
X = np.array([
    [390, 170, 550, 380],
    [210, 270, 80, 290],
    [350, 370, 340, 400],
    [520, 390, 300, 540]
])

# Final demand vector Y
Y = np.array([110, 60, 50, 100])

# 1. Total output for each sector (sum of rows in X)
total_output = X.sum(axis=1)

# 2. Step 1(A): Calculate the direct cost matrix A (direct costs matrix)
A = X / total_output[:, np.newaxis]

# 3. Step 2(S): Calculate the full cost matrix S = (I - A)^(-1)
I = np.eye(A.shape[0])  # Identity matrix of the same size as A
S = np.linalg.inv(I - A)  # Full cost matrix

# 4. Step 3(C): Full internal cost matrix C
C = S.copy()

# 5. Step 4(C'): Indirect cost matrix C'
epsilon = 1e-5  # Small value to perturb the matrix
S = np.linalg.inv(I - (A + np.eye(A.shape[0]) * epsilon))
C_prime = S - I

# 6. Step 5(X): Gross output X for each industry to meet the final demand Y
X_output = S @ Y

# Print the calculated data
print("Total Output (sum of rows in X):", total_output)
print("Direct Cost Matrix A:\n", A)
print("Full Cost Matrix S:\n", S)
print("Full Internal Cost Matrix C:\n", C)
print("Indirect Cost Matrix C':\n", C_prime)
print("Gross Output X for each industry:\n", X_output)

# Plotting results for each step

# Set up the figure background color and subplots
fig, axs = plt.subplots(2, 3, figsize=(100, 50))  # Increased figure size
fig.patch.set_facecolor('#F8E9F8')  # Set figure background color
plt.subplots_adjust(hspace=0.4, wspace=0.4)

# Plot 1: Matrix A (direct cost matrix)
sns.heatmap(A, ax=axs[0, 0], annot=True, cmap="Blues", cbar=False, square=True, linewidths=0.5, fmt='.2f', annot_kws={"size": 8})
axs[0, 0].set_title('Step 1(A): Direct Cost Matrix A', fontsize=10)
axs[0, 0].set_facecolor('#E6F2FF')  # Set background color for the plot

# Plot 2: Matrix S (full cost matrix)
sns.heatmap(S, ax=axs[0, 1], annot=True, cmap="RdBu", cbar=False, square=True, linewidths=0.5, fmt='.1f', annot_kws={"size": 8})
axs[0, 1].set_title('Step 2(S): Full Cost Matrix S', fontsize=10)
axs[0, 1].set_facecolor('#E6F2FF')

# Plot 3: Matrix C (full internal cost matrix)
cmap_c = sns.color_palette("dark:purple", as_cmap=True)
sns.heatmap(C, ax=axs[0, 2], annot=True, cmap=cmap_c, cbar=False,
             square=True, linewidths=0.5, fmt='.2e',  # Changed to simple scientific notation
             annot_kws={"size": 8})
axs[0, 2].set_title('Step 3(C): Full Internal Cost Matrix C', fontsize=10)
axs[0, 2].set_facecolor('#E6F2FF')


# Plot 4: Matrix C' (indirect cost matrix)
sns.heatmap(C_prime, ax=axs[1, 0], annot=True, cmap="coolwarm", cbar=False, square=True, linewidths=0.5, fmt='.1f', annot_kws={"size": 8})
axs[1, 0].set_title('Step 4(C\'): Indirect Cost Matrix C\'', fontsize=10)
axs[1, 0].set_facecolor('#E6F2FF')

# Plot 5a: Gross Output X (bar chart)
axs[1, 1].bar(range(len(X_output)), X_output, color='salmon')
axs[1, 1].set_title('Step 5(X): Gross Output X (Bar Chart)', fontsize=10)
axs[1, 1].set_facecolor('#E6F2FF')
axs[1, 1].set_xticks(range(len(X_output)))
axs[1, 1].set_xticklabels([f"Sector {i + 1}" for i in range(len(X_output))], fontsize=8)
axs[1, 1].set_ylabel('Output', fontsize=8)

# Plot 5b: Gross Output X (line graph)
axs[1, 2].plot(range(len(X_output)), X_output, marker='o', color='salmon')
axs[1, 2].set_title('Step 5(X): Gross Output X (Line Graph)', fontsize=10)
axs[1, 2].set_facecolor('#E6F2FF')
axs[1, 2].set_xticks(range(len(X_output)))
axs[1, 2].set_xticklabels([f"Sector {i + 1}" for i in range(len(X_output))], fontsize=8)
axs[1, 2].set_ylabel('Output', fontsize=8)

# Set the limits for the bar chart and line graph to avoid scientific notation
axs[1, 1].set_ylim(bottom=0)  # Set the bottom limit to 0
axs[1, 1].ticklabel_format(style='plain', axis='y')  # Disable scientific notation on y-axis
#axs[1, 2].set_ylim(bottom=0)  # Set the bottom limit to 0
#axs[1, 2].ticklabel_format(style='plain', axis='y')  # Disable scientific notation on y-axis

# Show the plots
plt.show()
