import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.arange(0, 100, 2)
x = z ** 2
y = z ** 2
c = x + y
ax.scatter(x, y, z, c=c)
plt.savefig("img/3.png")
plt.show()