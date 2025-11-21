import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# No theme, no style, no overrides
# Ensures white background and default seaborn barplot
# DO NOT change anything here

np.random.seed(42)
categories = ['Electronics', 'Home Appliances', 'Furniture', 'Clothing', 'Sports']
scores = np.random.uniform(3.5, 4.8, size=len(categories))

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction Score': scores
})

plt.figure(figsize=(8, 8), dpi=64)   # EXACT 512x512 output

sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction Score',
    color='#4C72B0'  # seaborn default bar color
)

plt.title('Average Customer Satisfaction by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Avg Satisfaction Score')

plt.savefig("chart.png", dpi=64)  # EXACT 512x512
plt.show()
