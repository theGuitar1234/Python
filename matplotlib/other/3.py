import matplotlib.pyplot as plt
import pandas as pd
import math
import random

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5))

# ax.set_xlim(-10, 10)
# ax.set_ylim(-2, 2)

ax.grid(True, alpha=0.3)
# ax.set_xticks(range(-10, 11, 1))
# ax.set_yticks(np.linspace(-2, 2, 9))

# ax.spines["left"].set_position("zero")
# ax.spines["bottom"].set_position("zero")

# ax.spines["right"].set_color("none")
# ax.spines["top"].set_color("none")

# ax.xaxis.set_ticks_position("bottom")
# ax.yaxis.set_ticks_position("left")

start = -1000
end = 1000
for i in range(-100*3, 100*3):
    ax.scatter(i, i**2)

plt.show()

