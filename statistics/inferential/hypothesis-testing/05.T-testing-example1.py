# Example1:
# A manufactor claims that the average weight of a bag of potato chips is 150 grams. A sample of 25
# bags is taken, and the average weight is found to be 148 grams, with a standard deviation of 5 grams.
# Test the manufactor's claim using a one-tailed-test with a  significance  level of 0.05.
# Z-testing is possible reasion:
# x̄ = sample mean
# μ = population mean
# s =  population std
# n = number of sample data
# n<30
import scipy.stats as st
import numpy as np

alpha = 0.05
s_x = 148
p_u = 150
s_std = 5
n = 25
df = n - 1
t_table = st.t.ppf(alpha, df)  # (alpha, df)
print(t_table)
t_cal = (s_x - p_u) / (s_std / np.sqrt(n))

if t_cal < t_table:
    print(" Ha is right")
else:
    print("H0 is right")
