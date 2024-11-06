import numpy as np

# Define the pairwise comparison matrices
A1 = np.array([[1, 2, 4, 5],
               [1 / 2, 1, 2, 3],
               [1 / 4, 1 / 2, 1, 4],
               [1 / 5, 1 / 3, 1 / 4, 1]])

A2 = np.array([[1, 1, 2, 5],
               [1, 1, 3, 1],
               [1 / 2, 1 / 3, 1, 3],
               [1 / 5, 1, 1 / 3, 1]])

A3 = np.array([[1, 3, 4, 2],
               [1 / 3, 1, 4, 2],
               [1 / 4, 1 / 4, 1, 2],
               [1 / 2, 1 / 2, 1 / 2, 1]])

A4 = np.array([[1, 1 / 2, 1 / 3, 1 / 2],
               [2, 1, 1 / 2, 1 / 3],
               [3, 2, 1, 1 / 4],
               [2, 3, 4, 1]])

A5 = np.array([[1, 1, 1 / 2, 5],
               [1, 1, 1 / 3, 1],
               [2, 3, 1, 1 / 2],
               [1 / 5, 1, 2, 1]])

A6 = np.array([[1, 1 / 2, 1 / 4, 1 / 2],
               [2, 1, 1 / 3, 1 / 2],
               [4, 3, 1, 1 / 2],
               [2, 2, 2, 1]])

# List of pairwise comparison matrices
matrices = [A1, A2, A3, A4, A5, A6]

# Define the priority vectors
priority_vectors = {
    'A1': [0.49753799, 0.25750579, 0.17243689, 0.07251933],
    'A2': [0.37623462, 0.3062028, 0.19084833, 0.12671425],
    'A3': [0.46867979, 0.2735346, 0.12972916, 0.12805646],
    'A4': [0.11944768, 0.1548946, 0.23550569, 0.49015203],
    'A5': [0.33085846, 0.15764231, 0.30547054, 0.20602869],
    'A6': [0.1105168, 0.16250298, 0.34549423, 0.38148598]
}


def calculate_priority_vector(matrix):
    # Calculate the principal eigenvector (priority vector)
    eigvals, eigvecs = np.linalg.eig(matrix)
    max_index = np.argmax(eigvals)  # index of the maximum eigenvalue
    priority_vector = eigvecs[:, max_index].real  # Get the corresponding eigenvector
    priority_vector /= np.sum(priority_vector)  # Normalize the vector
    return priority_vector


# Check if calculated priority vectors match the given priority vectors
for i, matrix in enumerate(matrices, start=1):
    calculated_vector = calculate_priority_vector(matrix)
    calculated_vector = calculated_vector / np.sum(calculated_vector)  # Normalize
    expected_vector = np.array(priority_vectors[f'A{i}'])

    # Compare the two vectors
    comparison_result = np.allclose(calculated_vector, expected_vector, atol=1e-6)

    print(f"Matrix A{i}:")
    print(f"  Calculated priority vector: {calculated_vector}")
    print(f"  Expected priority vector: {expected_vector}")
    print(f"  Match: {comparison_result}\n")
