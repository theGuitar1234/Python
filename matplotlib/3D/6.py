from matplotlib.tri import Triangulation
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

tri = Triangulation(X.ravel(), Y.ravel())

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)

plt.savefig("img/6.png")
plt.show()