import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5))

fig.set_size_inches(8, 5)
fig.suptitle("Overall title for the whole figure")

ax.grid(True, alpha=0.3)

# a = 0
# b = 200
# scale = 0.2
# for i in range(a, b):
#     ax.scatter(i, math.sin(i*scale))

# x = np.arange(0, 5*np.pi, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# ax.fill(x, y)
# ax.fill_between(x, 10, 50)

# categories = ["Farrah", "Fred", "Felicia"]
# levels = [90, 20, 100]
# plt.bar(categories, levels)

# x = np.asarray([[random.uniform(-1, 1) for _ in range(5)] for _ in range(5)], dtype=np.float32)
# ax.imshow(x)

# X = np.arange(random.randint(0, 100), random.randint(100, 200), random.randint(0, 10))
# Y = np.arange(random.randint(0, 100), random.randint(100, 200), random.randint(0, 10))

# Z = X + Y
# Z = np.cos(X) + np.sin(Y)
# Z = np.cos(X / 5) + np.sin(Y / 5)

# X = np.linspace(-5.0, 3.0, 70)
# Y = np.linspace(-5.0, 3.0, 70)
# [X, Y] = np.meshgrid(X, Y)
# Z = X ** 2 + Y ** 2
# ax.contourf(X, Y, Z)

ax.quiver([0, 2, 4], [0, 0, 2], [4, 2, 3], [4, 6, 2])

plt.show()
fig.savefig("img/plot.png")

