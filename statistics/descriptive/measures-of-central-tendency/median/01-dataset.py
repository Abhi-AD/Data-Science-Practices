import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../../data/titanic_data_100.csv")
print(dataset.head(3))
# dataset["age"].fillna(dataset["age"].mean(), inplace=True) #clean up the dataset
median = np.median(dataset["fare"])
print(dataset["fare"].median())

sns.histplot(x="fare", data=dataset, bins=[i for i in range(0, 81, 10)])
plt.plot([median for i in range(0, 20)], [i for i in range(0, 20)], c="green")
print(plt.show())
