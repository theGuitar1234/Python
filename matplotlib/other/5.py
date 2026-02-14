import matplotlib.pyplot as plt
import pandas as pd
import random

fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(True, alpha=0.3)

n = 1

#Scatter plot
for i in range(0, 100):
    ax.scatter(random.randint(i-10 - n, i+10 - n), random.randint(i-10 - n, i+10 - n))
    n -= 1

plt.show()

#Spaghetti plot
import numpy as np

np.random.seed(42) 

n_series = 30     # number of lines (subjects)
n_points = 50     # time points

t = np.linspace(0, 10, n_points)   # time axis

# Base signal (shared trend)
base = np.sin(t)

# Each series = base signal + noise + small offset
Ys = base + 0.3 * np.random.randn(n_series, n_points) + np.random.uniform(-0.5, 0.5, (n_series, 1))

for y in Ys:
    ax.plot(t, y, alpha=0.4, linewidth=1)

plt.show()

#Dot plot
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)

x = np.random.normal(loc=70, scale=8, size=40)

fig, ax = plt.subplots(figsize=(8, 2))

ax.scatter(x, np.zeros_like(x), alpha=0.6)

ax.set_yticks([])             # hide meaningless y-axis
ax.set_xlabel("Value")
ax.set_title("1D dot plot")

plt.show()


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 2))

ax.scatter(x, np.zeros_like(x), alpha=0.6)

ax.set_yticks([])             # hide meaningless y-axis
ax.set_xlabel("Value")
ax.set_title("1D dot plot")

plt.show()
