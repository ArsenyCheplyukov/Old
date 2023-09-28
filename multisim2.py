import numpy as np
import matplotlib.pyplot as plt

tau_ = np.array([0.033, 0.33, 1, 3.3]) * 19.2e-5
sub_numbers = ['₁', '₂', '₃', '₄']
multiplier = [1000000, 100000, 10000, 10000]
powers = ['10⁻⁶', '10⁻⁵', '10⁻⁴', '10⁻⁴']

plt.grid(color='black', linestyle='-', linewidth=0.1, which='both')
plt.ylabel("Напряжение, В")
plt.xlabel("Время, $10^{-4}$ с")
for counter, tau in enumerate(tau_):
    x = np.linspace(0, tau_[1]*10, 1000)
    y = 1 - np.exp(-x/tau)
    in_ = np.array([0, 1, 2, 3, 4, 5, 6]) * (1.0/1000000)
    out = 1 - np.exp(-in_/tau)
    print(f"{sub_numbers[counter]} = {out}")
    #plt.xscale("log")
    plt.plot(x*10000, y, label="τ{} = {:.2f}*{}".format(sub_numbers[counter], tau*multiplier[counter], powers[counter]))

plt.legend()
plt.title("Зависисмость напряжения от времени")
plt.show()