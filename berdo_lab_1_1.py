import numpy as np
import pandas as pd
from numpy.linalg import eig


# Function to calculate priorities (weights) from the eigenvector of the pairwise comparison matrix
def calculate_priorities(matrix):
    eigvals, eigvecs = eig(matrix)
    max_index = np.argmax(eigvals)  # Identify the largest eigenvalue
    max_eigvec = np.real(eigvecs[:, max_index])  # Get the corresponding eigenvector
    normalized_vector = max_eigvec / np.sum(max_eigvec)  # Normalize to sum to 1
    return normalized_vector


# Function to check consistency (CI and CR) of the comparison matrix
def check_consistency(matrix, priorities):
    n = matrix.shape[0]
    # Calculate lambda_max (principal eigenvalue)
    weighted_sum = matrix @ priorities
    lambda_max = np.sum(weighted_sum / priorities) / n

    # Consistency Index (CI)
    CI = (lambda_max - n) / (n - 1)

    # Random Index (RI) for matrices of size 3 to 10
    random_index = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    RI = random_index[n - 1]

    # Consistency Ratio (CR)
    CR = CI / RI if RI != 0 else 0

    return CI, CR


# Function to ensure sheet names are <= 31 characters
def truncate_sheet_name(sheet_name):
    return sheet_name[:31]


# Function to perform AHP for multiple criteria
def ahp_process():
    # Define criteria and alternatives in Ukrainian
    criteria = ["Економічність", "Вартість", "Надійність", "Вплив на здоров'я", "Вартість утилізації"]
    alternatives = ["Лампа розжарювання", "Електролюмінесцентна лампа", "Світлодіодна лампа"]

    # Pairwise comparison matrices for each criterion (3x3 matrices filled with pairwise comparison values)
    matrices = {
        "Економічність": np.array([[1, 5, 7],
                                   [1 / 5, 1, 3],
                                   [1 / 7, 1 / 3, 1]]),
        "Вартість": np.array([[1, 1 / 7, 1 / 5],
                              [7, 1, 3],
                              [5, 1 / 3, 1]]),
        "Надійність": np.array([[1, 1 / 3, 1 / 5],
                                [3, 1, 1 / 3],
                                [5, 3, 1]]),
        "Вплив на здоров'я": np.array([[1, 7, 5],
                                       [1 / 7, 1, 3],
                                       [1 / 5, 1 / 3, 1]]),
        "Вартість утилізації": np.array([[1, 1 / 5, 1 / 7],
                                         [5, 1, 3],
                                         [7, 1 / 3, 1]])
    }

    # Store results
    priorities_dict = {}
    consistency_results = {}

    # Perform AHP for each criterion
    for criterion, matrix in matrices.items():
        priorities = calculate_priorities(matrix)
        priorities_dict[criterion] = priorities

        # Check consistency
        CI, CR = check_consistency(matrix, priorities)
        consistency_results[criterion] = (CI, CR)

    # Save matrices, priorities, and consistency checks to Excel
    with pd.ExcelWriter("ahp_results_combined.xlsx", engine="openpyxl") as writer:
        for criterion, matrix in matrices.items():
            # Ensure sheet name is <= 31 characters
            short_criterion = truncate_sheet_name(f"{criterion}")

            # Create a DataFrame combining the matrix, priorities, and consistency results
            df_matrix = pd.DataFrame(matrix, index=alternatives, columns=alternatives)
            df_priorities = pd.DataFrame(priorities_dict[criterion], index=alternatives, columns=["Пріоритет"])
            df_consistency = pd.DataFrame([consistency_results[criterion]], columns=["CI", "CR"])

            # Combine all three sections into one DataFrame
            combined_df = pd.concat([df_matrix, df_priorities, df_consistency], axis=1)

            # Write the combined DataFrame to a single sheet for this criterion
            combined_df.to_excel(writer, sheet_name=short_criterion)

    # Aggregate global priorities
    global_priorities = np.zeros(3)  # For 3 alternatives
    # Assign equal weight to each criterion for simplicity (can be customized)
    criterion_weights = np.ones(len(criteria)) / len(criteria)

    # Multiply each criterion priority by its weight and sum for global priorities
    for i, criterion in enumerate(criteria):
        global_priorities += criterion_weights[i] * priorities_dict[criterion]

    # Reopen the file in append mode to add global priorities
    with pd.ExcelWriter("ahp_results_combined.xlsx", engine="openpyxl", mode="a", if_sheet_exists="new") as writer:
        df_global_priorities = pd.DataFrame(global_priorities, index=alternatives, columns=["Глобальний Пріоритет"])
        df_global_priorities.to_excel(writer, sheet_name="Глобальні Пріоритети")

    print("AHP таблиці збережені у файлі 'ahp_results_combined.xlsx'")


# Run the AHP process
ahp_process()
