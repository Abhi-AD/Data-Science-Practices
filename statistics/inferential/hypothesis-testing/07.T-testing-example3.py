# Example3:
#      A company wants to test whether a new training program improves the typing speed of its employees. The
#      typing speed of 20 employees was recorded before and after the training program. The data is given
#      below. Test at a 5% level of significance whether the training program has an effect on the typing
#      speed of the employees.
#      Before: 50,60,45,65,55,70,40,75,80,65,70,60,50,55,45,75,60,50,65,70
#      After: 60,70,55,75,65,80,50,85,90,70,75,65,55,60,50,80,65,55,70,75

import scipy.stats as st
import numpy as np

alpha = 0.05 / 2  # two side

before = np.array(
    [50, 60, 45, 65, 55, 70, 40, 75, 80, 65, 70, 60, 50, 55, 45, 75, 60, 50, 65, 70]
)
after = np.array(
    [60, 70, 55, 75, 65, 80, 50, 85, 90, 70, 75, 65, 55, 60, 50, 80, 65, 55, 70, 75]
)
n = 20
df = n - 1  # number of value same show n-1
t_table_left = st.t.ppf(alpha, df)  # (alpha, df) left
t_table_right = st.t.ppf(1 - alpha, df)  # (1-alpha, df) right
print(t_table_left, t_table_right)

# after and before mean
before_mean = np.mean(before)
after_mean = np.mean(after)
print(before_mean, after_mean)

# calculate the standard deviation
before_std = np.std(before)
after_std = np.std(after)
print(before_std, after_std)


# calcuate the table calculation
t_cal = (after_mean - before_mean) / np.sqrt(
    (np.square(before_std) / n) + (np.square(after_std) / n)
)
print(t_cal)

if t_cal > t_table_right or t_cal < t_table_left:
    print("Ha is right")
else:
    print("H0 is right")
