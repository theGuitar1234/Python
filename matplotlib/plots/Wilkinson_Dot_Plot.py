import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

data = np.array([62, 65, 65, 67, 68, 68, 68, 70, 71, 72, 72, 75, 75, 75, 76, 79])
data = np.sort(data)

bin_width = 4

stack_counts = defaultdict(int)

x_dots = []
y_dots = []

for value in data:
    slot = round(value / bin_width) * bin_width
    stack_counts[slot] += 1
    x_dots.append(slot)
    y_dots.append(stack_counts[slot])

fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(x_dots, y_dots, s=100, edgecolors="black", alpha=0.8)
ax.set_yticks([])
ax.set_ylabel("")
ax.set_xlabel("Value")
ax.set_title("Wilkinson-Style Dot Plot")
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.savefig("img/wlknsn_dt_plt.png")
plt.show()