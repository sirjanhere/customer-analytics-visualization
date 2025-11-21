import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['figure.figsize'] = (8, 8)
plt.rcParams['figure.dpi'] = 64
plt.rcParams['savefig.dpi'] = 64

sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.0)

np.random.seed(42)
categories = ['Electronics', 'Home Appliances', 'Furniture', 'Clothing', 'Sports']
scores = np.random.uniform(3.5, 4.8, size=len(categories))

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction Score': scores
})

plt.figure()
sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction Score',
    palette='Blues_d'
)

plt.title("Average Customer Satisfaction by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Avg Satisfaction Score")

plt.savefig("chart.png")
