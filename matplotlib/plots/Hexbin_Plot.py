import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000000)
y = 2 * x + np.random.normal(size=1000000)

plt.hexbin(x, y, gridsize=100, cmap='Blues')
plt.colorbar()
plt.savefig("img/hxbn_plt.png")
plt.show()