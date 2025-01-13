# Example 2:
# Scenario: Imagine you work for an e-commerce company, and your team is responsible for
# analyzing customer purchase data. You want to determine whether a new website design has
# led to a significant increase in the average purchase amount compared to the old design.

# Data: You have collected data from a random sample of 30 customers who made purchases on
# the old website design and 30 customers who made purchases on the new website design.
# You have the sample means, sample standard deviations, and sample sizes for both groups.

# Old design data = [45.2, 42.8, 38.9, 43.5, 41.0, 44.6, 40.5, 42.7, 39.8, 41.4, 44.3, 39.7,
# 42.1,43.0, 42.2, 41.5, 39.6, 44.0, 43.1, 38.7, 43.9, 42.0, 41.9, 42.8, 43.7, 41.3, 40.9,
# 42.5, 41.6]

# New design data = [48.5, 49.1, 50.2, 47.8, 48.7, 49.9, 48.0, 50.5, 49.8, 49.6,
# 48.2,48.9,50.3,49.4,50.1,48.6, 48.3, 49.0, 50.0, 48.4, 49.3, 49.5, 48.8, 50.6, 50.4,
# 48.1, 49.2, 50.7]

# Population std= 2.5


import scipy.stats as st
import numpy as np

O_data = np.array(
    [
        45.2,
        42.8,
        38.9,
        43.5,
        41.0,
        44.6,
        40.5,
        42.7,
        39.8,
        41.4,
        44.3,
        39.7,
        42.1,
        43.0,
        42.2,
        41.5,
        39.6,
        44.0,
        43.1,
        38.7,
        43.9,
        42.0,
        41.9,
        42.8,
        43.7,
        41.3,
        40.9,
        42.5,
        41.6,
        29.2,
    ]
)
N_data = np.array(
    [
        48.5,
        49.1,
        50.2,
        47.8,
        48.7,
        49.9,
        48.0,
        50.5,
        49.8,
        49.6,
        48.2,
        48.9,
        50.3,
        49.4,
        50.1,
        48.6,
        48.3,
        49.0,
        50.0,
        48.4,
        49.3,
        49.5,
        48.8,
        50.6,
        50.4,
        48.1,
        49.2,
        50.7,
        50.7,
        40.7,
    ]
)
pop_std = 2.5
n_sp = len(N_data)
alp = 0.05
mean_new = np.mean(N_data)
mean_old = np.mean(O_data)

z_cal = (mean_new - mean_old) / (pop_std / np.sqrt(n_sp))
z_table = st.norm.ppf(1 - alp)

print(z_cal)
print(z_table)
if z_table < z_cal:
    print(" Ha is right")
else:
    print("H0 is right")
