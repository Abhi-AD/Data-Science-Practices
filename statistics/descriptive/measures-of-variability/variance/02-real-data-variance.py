import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../../data/titanic_data_100.csv")
print(dataset.head(3))
print(dataset["age"].var())
sns.histplot(x="age", data=dataset)
plt.show()
