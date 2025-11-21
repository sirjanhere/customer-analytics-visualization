import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn styling
sns.set_style('whitegrid')
sns.set_context('talk')

# Synthetic data generation
np.random.seed(42)
categories = ['Electronics', 'Home Appliances', 'Furniture', 'Clothing', 'Sports']
scores = np.random.uniform(3.5, 4.8, size=len(categories))

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction Score': scores
})

# Chart
plt.figure(figsize=(8, 8))  # exactly 512x512 when dpi=64
sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction Score',
    palette='Blues_d'
)

plt.title('Average Customer Satisfaction by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Avg Satisfaction Score')

plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
