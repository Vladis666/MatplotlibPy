import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set print options for NumPy arrays to show full precision and suppress scientific notation
np.set_printoptions(precision=10, suppress=True)

# 1. Define the input data
# Original Gross Output X for each industry
X = np.array([-8276470.32195478, -8276513.38925999, -8276528.46492746, -8276473.69173201])

# Final demand vector Y (from your data)
Y = np.array([390, 210, 350, 520])

# Percentage changes for output (gamma) based on your provided data:
gamma = np.array([5, -3, 0, 2])  # Example percentage changes for each industry

# 2. Calculate the new final demand vector Y' based on percentage changes
Y_new = Y * (1 + gamma / 100)

# 3. Total output for each sector (sum of rows in X)
total_output = np.sum(X)

# 4. Direct Cost Matrix A (assumed to be the same for simplicity)
A = np.array([
    [0.26174497, 0.11409396, 0.36912752, 0.25503356],
    [0.24705882, 0.31764706, 0.09411765, 0.34117647],
    [0.23972603, 0.25342466, 0.23287671, 0.2739726],
    [0.29714286, 0.22285714, 0.17142857, 0.30857143]
])

# 5. Calculate the Full Cost Matrix S
I = np.eye(A.shape[0])  # Identity matrix of the same size as A
S = np.linalg.inv(I - A)  # Full cost matrix

# 6. Calculate the new output vector X' based on the changes in Y
X_new = S @ Y_new

# Print the calculated data without scientific notation
print("New Output Vector X':", np.array2string(X_new, formatter={'float_kind': lambda x: f'{x:.10f}'}))
print("Total Output:", total_output)
print("Direct Cost Matrix A:\n", np.array2string(A, formatter={'float_kind': lambda x: f'{x:.10f}'}))
print("Full Cost Matrix S:\n", np.array2string(S, formatter={'float_kind': lambda x: f'{x:.10f}'}))
print("New Final Demand Vector Y':\n", np.array2string(Y_new, formatter={'float_kind': lambda x: f'{x:.10f}'}))

# Plotting results
fig, axs = plt.subplots(2, 3, figsize=(18, 10))

# Plot 1: New Output Vector X'
axs[0, 0].bar(range(len(X_new)), X_new, color='skyblue')
axs[0, 0].set_title('New Output Vector X\'', fontsize=14)
axs[0, 0].set_ylabel('Output', fontsize=12)
axs[0, 0].set_xticks(range(len(X_new)))
axs[0, 0].set_xticklabels([f"Sector {i + 1}" for i in range(len(X_new))], fontsize=10)

# Plot 2: New Final Demand Vector Y'
axs[0, 1].bar(range(len(Y_new)), Y_new, color='lightgreen')
axs[0, 1].set_title('New Final Demand Vector Y\'', fontsize=14)
axs[0, 1].set_ylabel('Final Demand', fontsize=12)
axs[0, 1].set_xticks(range(len(Y_new)))
axs[0, 1].set_xticklabels([f"Sector {i + 1}" for i in range(len(Y_new))], fontsize=10)

# Plot 3: Direct Cost Matrix A
sns.heatmap(A, ax=axs[0, 2], annot=True, cmap="Blues", cbar=False, square=True, linewidths=0.5, fmt='.2f', annot_kws={"size": 8})
axs[0, 2].set_title('Direct Cost Matrix A', fontsize=14)
axs[0, 2].set_facecolor('#E6F2FF')

# Plot 4: Full Cost Matrix S
sns.heatmap(S, ax=axs[1, 0], annot=True, cmap="RdBu", cbar=False, square=True, linewidths=0.5, fmt='.1f', annot_kws={"size": 8})
axs[1, 0].set_title('Full Cost Matrix S', fontsize=14)
axs[1, 0].set_facecolor('#E6F2FF')

# Optional Plot 5: Y' values as a heatmap
sns.heatmap(Y_new.reshape(1, -1), ax=axs[1, 1], annot=True, cmap="Spectral", cbar=False, square=True, linewidths=0.5, fmt='.1f', annot_kws={"size": 6})
axs[1, 1].set_title('New Final Demand Vector Y\' as Heatmap', fontsize=14)
axs[1, 1].set_xticks(range(len(Y_new)))
axs[1, 1].set_xticklabels([f"Sector {i + 1}" for i in range(len(Y_new))], fontsize=10)

# Hide the last subplot
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()
