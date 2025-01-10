import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sec_a = np.array([75, 65, 73, 68, 72, 67])
sec_b = np.array([90, 47, 43, 96, 93, 51])
no = np.array([1, 2, 3, 4, 5, 6])
mean = np.mean(sec_b)
plt.figure(figsize=(10, 3))
plt.scatter(sec_a, no, color="red", label="sec_a")
plt.scatter(sec_b, no, color="green", label="sec_b")
plt.plot([mean for i in range(1, 7)], no, color="blue", label="Mean")
plt.legend()
plt.show()
