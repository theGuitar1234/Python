import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111, projection="3d")
# x = np.linspace(-2, 2, 100)
# y = np.linspace(-2, 2, 100)
# Z = np.sin(X)**2 + np.cos(Y)**2

fig = plt.figure(figsize=(14,9))
x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T
z = np.sin(x**2) + np.cos(y**2)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='hot', antialiased=True)

cset = ax.contourf(x, y, z,
                   zdir ='z',
                   offset = np.min(z),
                   cmap = 'hot')
cset = ax.contourf(x, y, z,
                   zdir ='x',
                   offset =-5,
                   cmap = 'hot')
cset = ax.contourf(x, y, z, 
                   zdir ='y',
                   offset = 5,
                   cmap = 'hot')

plt.savefig("img/srfc_plt.png")
plt.show()