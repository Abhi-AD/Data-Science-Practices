import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = np.random.randint(10, 100)
pop_data = [np.random.randint(10, 100) for i in range(10000)]
pop_table = pd.DataFrame({"Pop_data": pop_data})

plt.figure(figsize=(3, 2))
sns.kdeplot(x="Pop_data", data=pop_table)
# plt.show()

sam_mean = []
for num_sample in range(50):
    sample_data = []

    for data in range(500):
        sample_data.append(np.random.choice(pop_data))
    sam_mean.append(np.mean(sample_data))

# print(np.random.choice(pop_data))

# check a distribution
sample_M = pd.DataFrame({"Sample_Mean": sample_data})
plt.figure(figsize=(3, 2))
sns.kdeplot(x="Sample_Mean", data=sample_M)
# plt.show()

# check a mean
print(np.mean(pop_data))
print(np.mean(sam_mean))
