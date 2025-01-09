import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../../data/titanic_data_100.csv")
print(dataset.head(3))

print(dataset["age"].mean())
mean = np.mean(dataset["age"])

sns.histplot(x="age", data=dataset, bins=[i for i in range(0, 81, 10)])
plt.plot([mean for i in range(0, 20)], [i for i in range(0, 20)], c="red")
print(plt.show())
