import pandas as pd

# Define the alternatives for each system component
functionality_options = ['Автоматизоване', 'Напівавтоматизоване']
data_type_options = ['Часові ряди', 'Точкові дані']
data_collection_method_options = ['API', 'Вручну', 'Комбіноване']

# Define system variants as sets
B1 = {functionality_options[0], data_type_options[0], data_collection_method_options[0]}
B2 = {functionality_options[0], data_type_options[0], data_collection_method_options[1]}
B3 = {functionality_options[1], data_type_options[1], data_collection_method_options[2]}

# Function to calculate various measures
def calculate_measures(Bj, Bk):
    count_A = len(Bj & Bk)  # Intersection count
    count_Bj = len(Bj)      # Count of Bj
    count_Bk = len(Bk)      # Count of Bk

    # Calculate similarity measures
    czekanowski = (2 * count_A) / (count_Bj + count_Bk) if (count_Bj + count_Bk) > 0 else 0
    jaccard = count_A / (count_Bj + count_Bk - count_A) if (count_Bj + count_Bk - count_A) > 0 else 0
    sokal_sneath = (2 * count_A) / (2 * count_Bj + 2 * count_Bk - count_A ** 2) if (2 * count_Bj + 2 * count_Bk - count_A ** 2) > 0 else 0
    andreev = (4 * count_A) / (count_Bj + count_Bk + 2 * count_A) if (count_Bj + count_Bk + 2 * count_A) > 0 else 0
    mullczynski = count_A / (count_Bj + count_Bk - count_A) if (count_Bj + count_Bk - count_A) > 0 else 0
    difference_measure = (count_Bj + count_Bk) - (2 * count_A)

    return {
        'Czekanowski-Sørensen': czekanowski,
        'Jaccard': jaccard,
        'Sokal-Sneath': sokal_sneath,
        'Andreev': andreev,
        'Mullczynski': mullczynski,
        'Difference Measure': difference_measure
    }

# Calculate measures against a prototype (using B1 as an example)
prototype = B1
variants = [B1, B2, B3]
variant_names = ['B1', 'B2', 'B3']
similarity_scores = []

for variant in variants:
    measures = calculate_measures(prototype, variant)
    similarity_scores.append(measures['Czekanowski-Sørensen'])  # Or any measure you prefer

# Create a DataFrame for ranking
ranking_df = pd.DataFrame({
    'Variant': variant_names,
    'Czekanowski-Sørensen Score': similarity_scores
})

# Sort the DataFrame by similarity score
ranking_df = ranking_df.sort_values(by='Czekanowski-Sørensen Score', ascending=False).reset_index(drop=True)

# Display ranking
print("Ranking of Variants by Proximity to Prototype:")
print(ranking_df)

# Prepare data for Excel
data_for_excel = {
    'Варіант': variant_names,
    'Оцінка близькості (Чекановського-Серенсена)': similarity_scores
}

# Create a DataFrame and save to Excel
ranking_df.to_excel('ranking_variants.xlsx', index=False)
print(f"\nРейтинг варіантів збережено у 'ranking_variants.xlsx'")
