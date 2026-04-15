import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

fig = plt.figure()
fig.add_subplot(111, projection='3d')
ax = plt.axes(projection='3d')

x = np.arange(0, 100)
y = np.arange(0, 100)
z = np.sin(x) + np.cos(y)

ax.plot3D(x, y, z, color='green')
plt.savefig("img/2.png")
plt.show()