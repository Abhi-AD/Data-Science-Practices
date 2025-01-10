import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../../../../data/titanic_data_100.csv")
print(dataset.head(3))
min_age = dataset["age"].min()
max_age = dataset["age"].max()
range = max_age - min_age
print(min_age, max_age, range)
