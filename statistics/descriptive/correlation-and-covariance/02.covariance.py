import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../data/trips.csv")
print(dataset.head(3))

# this file check a null value
print(dataset.isnull().sum())

# correaltions
print(dataset.info())
cov = dataset.select_dtypes(["float64", "int64"]).corr()
print(cov)

plt.figure(figsize=(4, 3))
sns.heatmap(cov, annot=True)
plt.show()
