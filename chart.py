import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate realistic synthetic data
data = {
    'Product Category': [
        'Electronics', 'Apparel', 'Home Goods', 
        'Toys', 'Food & Beverage', 'Beauty', 'Sporting Goods'
    ],
    'Average Satisfaction Score': [
        8.3, 7.4, 8.9, 7.1, 8.7, 7.8, 8.0
    ]
}

df = pd.DataFrame(data)

# Set Seaborn style and context for professional look
sns.set_style('whitegrid')
sns.set_context('talk')

# Set color palette
palette = sns.color_palette('Set2')

# Create figure with required size for 512x512 pixels
plt.figure(figsize=(8, 8))

# Seaborn barplot
ax = sns.barplot(
    x='Average Satisfaction Score', 
    y='Product Category', 
    data=df,
    palette=palette
)

# Add titles and labels
plt.title('Average Customer Satisfaction by Product Category', fontsize=18, weight='bold')
plt.xlabel('Average Satisfaction Score', fontsize=14)
plt.ylabel('Product Category', fontsize=14)

# Optional: Show values on bars for clarity
for index, value in enumerate(df['Average Satisfaction Score']):
    ax.text(value + 0.05, index, f'{value:.1f}', va='center', fontsize=13)

plt.tight_layout()

# Save chart as PNG (512x512 pixels)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
