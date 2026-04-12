import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

x = [1, 2, 3, 4, 5]
y = [6, 2, 5, 1, 3]

fig, ax = plt.subplots(figsize=(8, 4))

ax.scatter(x, y, s=80, color="seagreen", label="frequency")
ax.set_xlim(0, 6)
ax.set_ylim(0, 7)
ax.set_xticks(range(0, 7))
ax.set_yticks(range(0, 8))
ax.grid(True)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.4), frameon=False)
plt.savefig("img/clvlnd_dt_plt.png")
plt.show()