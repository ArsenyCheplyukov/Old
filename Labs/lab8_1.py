import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

x = (360-np.array([356.225, 355.975, 355.4, 355, 354.65, 354.25, 353.9, 353.475]))-5
y = np.array([-2.64, -2, -1, 0, 1, 2, 2.5, 2.64])
f = np.poly1d(np.polyfit(x, y, 1))

x_array = np.linspace(min(x), max(x), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel("Ток соленоида, А", fontsize=10)
plt.xlabel("Угол вращения, °", fontsize=10)

plt.scatter(x, y, c="orange", label='Экспериментальные данные')
plt.plot(x_array, f(x_array), color="red", label='Линейная аппроксимация по экспериментальным данным')

#plt.axhline(y=7.31, color='black', linestyle='--')
#plt.axvline(x=8, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend(fontsize=8)
plt.title("Зависисмость тока соленоида от угла вращения", fontweight='bold', fontstyle='italic', fontsize=14)
print(x)
plt.show()