import matplotlib.pyplot as plt

# Data for Windows 10 prices
versions = ['Windows 10 Home', 'Windows 10 Pro', 'Windows 10 Enterprise']
prices = [139.99, 199.99, 309.00]  # Prices in USD

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(versions, prices, color=['blue', 'green', 'orange'])

# Add title and labels
plt.title('Prices of Windows 10 Versions', fontsize=16)
plt.xlabel('Windows 10 Versions', fontsize=14)
plt.ylabel('Price in USD', fontsize=14)
plt.ylim(0, 350)  # Set the y-axis limit for better visibility

# Add price labels on top of the bars
for i, price in enumerate(prices):
    plt.text(i, price + 5, f'${price}', ha='center', fontsize=12)

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
