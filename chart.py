import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style('whitegrid')
sns.set_context('talk')

np.random.seed(42)
categories = ['Electronics', 'Home Appliances', 'Furniture', 'Clothing', 'Sports']
scores = np.random.uniform(3.5, 4.8, size=len(categories))

df = pd.DataFrame({
    'Product Category': categories,
    'Average Satisfaction Score': scores
})

# Create chart normally
plt.figure(figsize=(8, 8), dpi=64)
sns.barplot(
    data=df,
    x='Product Category',
    y='Average Satisfaction Score',
    palette='Blues_d'
)

plt.title('Average Customer Satisfaction by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Avg Satisfaction Score')

plt.savefig("chart_raw.png")  # save temporary raw file
plt.show()

# ---- FORCE RESIZE ----
from PIL import Image

img = Image.open("chart_raw.png")
img = img.resize((512, 512), Image.LANCZOS)
img.save("chart.png")   # final output

print("Final size:", Image.open("chart.png").size)


# from google.colab import files
# files.download('chart.png')
