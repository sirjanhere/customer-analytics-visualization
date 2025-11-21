import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate synthetic data for product categories
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

# Set Seaborn style and context
sns.set_style('whitegrid')
sns.set_context('talk')
palette = sns.color_palette('Set2')

plt.figure(figsize=(8, 8))  # 8*64=512px

ax = sns.barplot(
    x='Average Satisfaction Score', 
    y='Product Category', 
    data=df,
    palette=palette
)
plt.title('Average Customer Satisfaction by Product Category', weight='bold')
plt.xlabel('Average Satisfaction Score')
plt.ylabel('Product Category')

for i, v in enumerate(df['Average Satisfaction Score']):
    ax.text(v + 0.05, i, f'{v:.1f}', va='center')

plt.tight_layout()

# Exactly 512x512 pixels!
plt.savefig('chart.png', dpi=64)
plt.close()
