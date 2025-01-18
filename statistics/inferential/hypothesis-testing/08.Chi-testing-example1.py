# Example1:
#           A fair die is rolled 120 times and the following results are obtained:
#           Face1: 22 times
#           Face2: 17 times
#           Face3: 20 times
#           Face4: 26 times
#           Face5: 22 times
#           Face6: 13 times
#           Test at a 5% level of significance wheather the die of fair.

import scipy.stats as st
import numpy as np

Ob = np.array([22, 17, 20, 26, 22, 13])  # Observed value
Ex = np.array([20, 20, 20, 20, 20, 20])  # Expected value

# calculate chi-square Custom formula
print(np.sum(np.square(Ob - Ex) / Ex))

# calculate chi-square
chi_square_cal = st.chisquare(Ob, Ex)
print(chi_square_cal)
alpha = 0.05
critical_value = st.chi2.ppf(1 - alpha, 5)
print(critical_value)

if chi_square_cal.statistic > critical_value:
    print("Ha is right")
else:
    print("H0 is right")
