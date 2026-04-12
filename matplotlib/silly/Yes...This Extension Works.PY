import matplotlib.pyplot as plt
import pandas as pd
import math

fig, ax = plt.subplots(figsize=(10, 5))

fig.set_size_inches(8, 5)
fig.suptitle("Overall title for the whole figure")

ax.grid(True, alpha=0.3)

a = 0
b = 200
scale = 0.2
for i in range(a, b):
    ax.scatter(i, math.sin(i*scale))

plt.show()
fig.savefig("img/plot.png")

