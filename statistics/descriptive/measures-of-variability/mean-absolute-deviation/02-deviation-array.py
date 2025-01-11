import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sec_a = np.array([75, 65, 73, 68, 72, 67])
sec_b = np.array([90, 47, 43, 96, 93, 51])
no = np.array([1, 2, 3, 4, 5, 6])
mean = np.mean(sec_b)
print(np.abs(sec_a - mean))
mad_a = np.sum(np.abs(sec_a - mean)) / len(sec_a)
print(np.abs(sec_b - mean))
mad_b = np.sum(np.abs(sec_b - mean)) / len(sec_b)
