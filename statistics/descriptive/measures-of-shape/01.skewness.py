import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../data/titanic_data_100.csv")
print(dataset.head(3))
# Positively
print(dataset["age"].mean())
print(dataset["age"].median())
print(dataset["age"].mode()[0])
print(dataset["age"].skew())
sns.histplot(x="age", data=dataset)
plt.show()


# Random
data = np.random.normal(0, 100, 100)
df = pd.DataFrame({"x": data})
# print(df["x"].skew())
# sns.histplot(x="x", data=df)
# plt.show()
