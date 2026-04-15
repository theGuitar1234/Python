import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
y = np.sin(25 * z)
x = np.cos(25 * z)

ax.plot3D(x, y, z, color='green')
plt.savefig("img/2.png")
plt.show()