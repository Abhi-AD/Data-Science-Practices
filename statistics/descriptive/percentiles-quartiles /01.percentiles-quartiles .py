import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../data/titanic_data_100.csv")
print(dataset.head(3))
# # value missing to add the data
# print(dataset.isnull().sum())
# dataset["age"].fillna(dataset["age"].mean(), inplace=True)

percentile_0 = np.percentile(dataset["age"], 0)  # min value of age
percentile_25 = np.percentile(dataset["age"], 25)  # first quarter of age
percentile_50 = np.percentile(dataset["age"], 50)  # second (median) value of age
percentile_75 = np.percentile(dataset["age"], 75)  # third quarter of age
percentile_100 = np.percentile(dataset["age"], 100)  # max value of age
print(percentile_0, percentile_25, percentile_50, percentile_75, percentile_100)
print(dataset["age"].median())
print(dataset.describe())

# box boxplot
sns.boxplot(x="age", data=dataset)
plt.show()
