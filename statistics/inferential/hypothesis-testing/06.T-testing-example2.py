# Example1:
# A company wants to test whether there is a difference in productivity between two teams. They randomly
# select 20 employees from each team and record their productivity scores. The mean productivity score
# for Team A is 80 with a standard deviation of 5, while the mean productivity score for Team B is 75
# with a standard deviation of 6. Test at a 5% level of significance whether there is a difference in
# productivity between the two teams.
# x̄ = sample mean
# μ = population mean
# s =  population std
# n = number of sample data
# n<30
import scipy.stats as st
import numpy as np


alpha = 0.05 / 2  # two side
t_a = 80
t_b = 75
t_a_std = 5
t_b_std = 6

n = 20

df = n + n - 2
print(alpha, df)
t_table_left = st.t.ppf(alpha, df)  # (alpha, df) left
t_table_right = st.t.ppf(1 - alpha, df)  # (1-alpha, df) right
print(t_table_left, t_table_right)
t_cal = t_a - t_b
t_data = np.sqrt((np.square(t_a_std) / n) + (np.square(t_b_std) / n))
print(t_cal / t_data)
