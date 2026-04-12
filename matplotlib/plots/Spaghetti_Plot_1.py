#Spaghetti plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(True, alpha=0.3)

np.random.seed(42) 

n_series = 30
n_points = 50

t = np.linspace(0, 10, n_points)

base = np.sin(t)

Ys = base + 0.3 * np.random.randn(n_series, n_points) + np.random.uniform(-0.5, 0.5, (n_series, 1))

for y in Ys:
    ax.plot(t, y, alpha=0.4, linewidth=1)

plt.savefig("img/sphgett_plt_1.png")
plt.show()
