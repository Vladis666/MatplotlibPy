import pandas as pd

# Define the adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 0],  # API НБУ
    [0, 0, 1, 0, 0, 0],  # Збір даних
    [0, 0, 0, 1, 1, 0],  # База даних
    [0, 0, 0, 0, 0, 0],  # Збереження
    [0, 0, 0, 0, 0, 1],  # Аналіз
    [0, 0, 0, 0, 0, 0]   # Візуалізація
]

# Define the labels for the rows and columns
labels = ["API НБУ", "Збір даних", "База даних", "Збереження", "Аналіз", "Візуалізація"]

# Create a DataFrame from the adjacency matrix
df = pd.DataFrame(adj_matrix, index=labels, columns=labels)

# Export the DataFrame to an Excel file
df.to_excel("adjacency_matrix.xlsx")

print("Матриця суміжностей збережена у файлі 'adjacency_matrix.xlsx'")
