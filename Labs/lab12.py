import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#y = np.array([2.4, 3.65, 4.65, 5.41, 6.11, 6.68, 7.22])**2
y = np.array([1.78, 3.41, 4.47, 5.2, 5.94, 6.58, 7.16])**2
#x = 3662-np.array([1, 2, 3, 4, 5, 6, 7])
x = 3459-np.array([1, 2, 3, 4, 5, 6, 7])
f = np.poly1d(np.polyfit(x, y, 1))

x_array = np.linspace(min(x), max(x) + 1, 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel("Квадрат диаметра колец, $мм^2$")
plt.xlabel("Порядок колец")

plt.scatter(x, y, c="orange", label='Измерянные величины для оранжевого цвета')
plt.plot(x_array, f(x_array), color="red", label='Сглаженные величины для оранжевого цвета')

#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend()
plt.title("Зависисмость диаметра колец от порядка расположения")
plt.show()