# A teacher claims that the mean score of students in his class is greater than 82 with a
# standard deviation of 20. If a sampleof 81 students was selected with mean score of 90.
# Z-testing is possible reasion:
# x̄ = sample mean
# μ = population mean
# σ =  population std
# n = number of sample data
import scipy.stats as st
import numpy as np

s_x = 90
p_u = 82
p_std = 20
n = 81
ap = 0.05

z_cal = (s_x - p_u) / (p_std / np.sqrt(n))
z_table = st.norm.ppf(1 - ap)

if z_table < z_cal:
    print(" Ha is right")
else:
    print("H0 is right")
