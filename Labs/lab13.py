import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

y = np.array([-4.4,0.02, 4.75, 9.25])
x = np.array([-3, -2, -1, 1])
f = np.poly1d(np.polyfit(x, y, 1))

x_array = np.linspace(min(x), max(x), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel(r"Расстояние до диффракционных максимумов, lm", fontsize=9, style='italic') #\dfrac{1}{a₁}$, $см^{-1}
plt.xlabel("Порядок максимума, m", fontsize=9, style='italic')

plt.scatter(x, y, c="peachpuff", label='Измерянные величины')
plt.plot(x_array, f(x_array), color="darkorange", label='Сглаженные величины')

#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend()
plt.title("Зависисмость расстояния до максимумов оранжевого цвета\n диффракционной решётки от порядка максимума", fontsize=12, fontweight='bold', style='italic')
plt.show()