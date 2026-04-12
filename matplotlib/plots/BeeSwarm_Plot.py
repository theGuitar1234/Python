import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)
data = np.random.normal(loc=70, scale=4, size=100)
data = np.sort(data)

diameter = 2
step = 10

points = []

for yi in data:
    candidate_levels = [0.0]
    for k in range(1, 100):
        candidate_levels.extend([k * step, -k * step])
    for xi in candidate_levels:
        collision = any(
            (xi - xj) ** 2 + (yi - yj) ** 2 < diameter ** 2
            for xj, yj in points
        )
        if not collision:
            points.append((xi, yi))
            break

x_plot, y_plot = zip(*points)
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(x_plot, y_plot, s=80, alpha=0.7, edgecolors="black")
ax.set_yticks([])
ax.set_ylabel("")
ax.axhline(0, linewidth=1, alpha=0.3)
ax.set_xlabel("Value")
ax.set_title("Manual Beeswarm Plot in Matplotlib")
plt.savefig("img/bswrm_plt.png")
plt.show()