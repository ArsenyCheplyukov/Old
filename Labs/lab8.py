import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

y = np.array([1.05, 4.32, 6.24, 8.21])
x = np.array([2, 5, 7, 9])
f = np.poly1d(np.polyfit(x, y, 1))

x_array = np.linspace(min(x), max(x), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.xlabel("Концентрация раствора, %", fontsize=9)
plt.ylabel("Угол поворота плоскости, °", fontsize=10)

plt.scatter(x, y, c="orange", label='Экспериментальные данные')
plt.plot(x_array, f(x_array), color="red", label='Линейная аппроксимация по экспериментальным данным')

plt.axhline(y=7.31, color='black', linestyle='--')
plt.axvline(x=8, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend(fontsize=6)
plt.title("Зависисмость угла поворота плоскости поляризации от концентрации раствора", fontweight='bold', fontstyle='italic', fontsize=9)
plt.show()