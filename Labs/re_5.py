import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.interpolate import interp1d

y = np.array([3.2, 3.2, 3.2, 3.2 , 3.2 ,3.16, 2.67])
x = np.array([1, 10, 100, 500, 1000, 1250, 1500])
f = interp1d(x, y, 'cubic')

x_array = np.linspace(min(x), max(x), num=100000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel("Коэффициент усиления")
plt.xlabel("Входное напряжение, В")

plt.scatter(x, y, c="blue",)
plt.plot(x_array, f(x_array), color="red")
#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
#plt.legend()
plt.title("Зависисмость коэффициента усиления от входного напряжения")
plt.show()