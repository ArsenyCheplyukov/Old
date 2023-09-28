import matplotlib.pyplot as plt
import numpy as np

data_1 = np.array([])
data_2 = np.array([])
data_3 = np.array([])

with open("./data42.txt", "r") as file:
    contents = file.readlines()
    for line in contents:
        data_1 = np.append(data_1, float(line))
with open("./data84.txt", "r") as file:
    contents = file.readlines()
    for line in contents:
        data_2 = np.append(data_2, float(line))
with open("./data21.txt", "r") as file:
    contents = file.readlines()
    for line in contents:
        data_3 = np.append(data_3, float(line))

minimal = min(np.min(data_1), np.min(data_2), np.min(data_3))
data_1 -= minimal
data_2 -= minimal
data_3 -= minimal

#bins = np.linspace(min(np.min(data_1), np.min(data_2)), max(np.max(data_1), np.max(data_2)), 20)

len = min(np.size(data_1), np.size(data_2), np.size(data_3))

print(data_1.mean()+minimal, data_2.mean()+minimal, data_3.mean()+minimal)

plt.hist(data_3[:len], alpha=0.15, label='21MHz')
plt.hist(data_1[:len], alpha=0.3, label='42MHz')
plt.hist(data_2[:len], alpha=0.6, label='84MHz')
plt.legend(loc='upper right')
plt.show()