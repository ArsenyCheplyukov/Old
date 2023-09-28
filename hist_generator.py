import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

needed_pulse = 1000000
delta = 104
variance = 20

def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

array = np.array(np.loadtxt('./data/sinfrequency42Mhz.txt', dtype=float))
print(array.mean(), array.min(), array.max(), np.median(array), array.std(), array.size)
plt.title("Распределение данных относительно среднего значения выборки", style='italic')
plt.xlabel('Время, нс')
plt.hist(array, bins=range(int(needed_pulse-(delta/2)-(delta*variance)), int(needed_pulse+(delta/2)+(delta*variance)), delta))
plt.show()
