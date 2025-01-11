import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Normal Skew
normal = [
    2,
    3,
    3,
    4,
    4,
    4,
    5,
    5,
    5,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
    7,
    7,
    7,
    7,
    7,
    8,
    8,
    8,
    8,
    8,
    9,
    9,
    9,
    9,
    10,
    10,
    10,
    11,
    11,
    12,
]
dfn = pd.DataFrame({"n": normal})
print(dfn["n"].skew())
print(dfn["n"].mean())
print(dfn["n"].median())
print(dfn["n"].mode()[0])
sns.histplot(x="n", data=dfn, bins=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
plt.show()
