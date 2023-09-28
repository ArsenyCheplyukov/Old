import numpy as np
import matplotlib.pyplot as plt

r = np.array([80, 90, 105, 115, 115, 115, 100, 92, 70, 47, 29, 12, 3.25, 1, 6.25, 18.25, 37, 60])
r = np.concatenate((r, r, np.array(r[0])), axis=None)
theata = np.pi*np.arange(10, 371, 10)/180
print(r.size, theata.size)
ax = plt.subplot(111,projection='polar')

plt.scatter(theata, r, c="darkblue")
ax.plot(theata,r,color='b',linewidth=2)
ax.grid(True)
plt.title(" Зависимость силы фототока (I, мА) от\n положения пластинки (φ, градусы)", fontsize=14, fontweight='bold', style='italic')
plt.show()