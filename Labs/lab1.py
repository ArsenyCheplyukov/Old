import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

y = 1/(np.array([40.5, 25, 20.5, 17.8, 16.75, 15.75]) / 100)
x = 1/(np.array([15, 20, 25, 30, 35, 40])/100)
f = np.poly1d(np.polyfit(x, y, 1))

x_array = np.linspace(min(x), max(x), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel(r"$\dfrac{1}{a_2}$, $м^{-1}$", fontsize=9, style='italic') #\dfrac{1}{a₁}$, $см^{-1}
plt.xlabel(r"$\dfrac{1}{a_1}$, $м^{-1}$", fontsize=9, style='italic')

plt.scatter(x, y, c="peachpuff", label='Измерянные величины')
plt.plot(x_array, f(x_array), color="darkorange", label='Сглаженные величины')

#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend()
plt.title("Зависисмость обратного расстояния от линзы до изображения \n от обратного расстояния от предмета до линзы", fontsize=12, fontweight='bold', style='italic')
plt.show()