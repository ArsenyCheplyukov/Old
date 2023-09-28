import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.interpolate import interp1d

y = np.array([500e-12, 650e-12, 950e-12, 1.4e-9, 14e-9,   140e-9, 1.4e-6, 14e-6,  140e-6, 1.4e-3, 14e-3,  140e-3, 1.4,   2.5]) / 2
x = np.array([1e-12,   2.5e-12, 5e-12,   10e-12, 100e-12, 1e-9,   10e-9,  100e-9, 1e-6,  10e-6,   100e-6, 1e-3,   10e-3, 100e-3])
f2 = np.poly1d(np.polyfit(x[4:-4], y[4:-4], 1))
f1 = interp1d(x[:4], y[:4], 'cubic')
f3 = interp1d(x[-3:], y[-3:], 'quadratic')

plt.xscale('log')
plt.yscale('log')
x_array2 = np.linspace(x[3], x[-3], num=100000)
x_array1 = np.linspace(np.min(x[:4]), np.max(x[:4]), 10000)
x_array3 = np.linspace(np.min(x[-3:]), np.max(x[-3:]), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel("Выходное напряжение, В")
plt.xlabel("Входное напряжение, В")

plt.scatter(x, y, c="blue",)
plt.plot(x_array1, f1(x_array1), color="red")
plt.plot(x_array2, f2(x_array2), color="red")
plt.plot(x_array3, f3(x_array3), color="red")
#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
#plt.legend()
plt.title("Зависисмость выходного напряжения от входного")
plt.show()