import numpy as np
import matplotlib.pyplot as plt

time_1 = np.array([])
time_2 = np.array([])
channel1_data = np.array([])
channel2_data = np.array([])

with open("./data/int_4_1.txt") as f:
    contents = f.readlines()
    for row in contents:
        data = row.split()
        time_1 = np.append(time_1, float(data[0])*1000000)
        channel1_data = np.append(channel1_data, float(data[1]))

with open("./data/int_4_2.txt") as f:
    contents = f.readlines()
    for row in contents:
        data = row.split()
        time_2 = np.append(time_2, float(data[0])*1000000)
        channel2_data = np.append(channel2_data, float(data[1]))

#time = np.linspace(0, len(channel1_data), len(channel1_data))

#($10^6$)
#plt.xscale("log")
plt.grid(color='black', linestyle='-', linewidth=0.25, which='both')
plt.ylabel("Напряжение, В")
plt.xlabel("Время, мкс")
plt.plot(time_1, channel1_data, color="red", label="Входной сигнал")
plt.plot(time_2, channel2_data, color="blue", label="Сигнал после преобразования интегрирующей цепи")



plt.legend()
plt.title("Зависимость напряжения от времени")
plt.show()