import numpy as np
import matplotlib.pyplot as plt
#tau = np.array([0.033, 0.33, 1, 3.3]) * 19.2e-5
#x = np.append(0, np.logspace(-4, -2.5, num=7))
#y = np.array([])
#print(x*1000000)
#for tau_ in tau:
#    print(np.exp(-x/tau_))
#    print(1-np.exp(-x/tau_))

time_2 = np.array([])
channel2_data = np.array([])
with open("C:/Users/Arseny/Desktop/Programs/code/Python/graphs/data/Tranzistor/wien_lissagou.txt") as f:
    contents = f.readlines()
    for row in contents:
        data = row.split()
        time_2 = np.append(time_2, (float(data[0])))
        channel2_data = np.append(channel2_data, float(data[1]))
        #plt.plot(time_2, 8*np.sin(2*np.pi*time_2), color="blue")
        plt.plot(time_2, channel2_data, color="lightgreen")
#plt.xscale('log')
plt.ylabel("Напряжение генератора, В")
plt.xlabel("Напряжение автогенератора с мостом Вина, В")

#plt.legend()
plt.title("Зависимость напряжение генератора и автогенератора с мостом Вина")
plt.grid()
plt.show()

