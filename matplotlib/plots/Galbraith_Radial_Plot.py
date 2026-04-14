import numpy as np
import matplotlib.pyplot as plt

effect = np.array([0.20, 0.10, 0.35, 0.05, 0.18, 0.40, -0.02])
se = np.array([0.08, 0.10, 0.12, 0.09, 0.07, 0.11, 0.10])

z = effect / se
prec = 1 / se

w = 1 / se**2
mu = np.sum(w * effect) / np.sum(w)

x = np.linspace(0, prec.max() * 1.05, 200)

fig, ax = plt.subplots(figsize=(7, 5))

ax.scatter(prec, z, alpha=0.8)

ax.plot(x, mu * x)

ax.plot(x, mu * x + 2, linestyle="--")
ax.plot(x, mu * x - 2, linestyle="--")

ax.axhline(0, linewidth=1)

ax.set_xlabel("Precision (1 / SE)")
ax.set_ylabel("Standardized effect (effect / SE)")
ax.set_title("Galbraith / Radial Plot")

plt.savefig("img/glbrth_plt.png")
plt.show()