import numpy as np
import matplotlib.pyplot as plt

# fake example data
s12 = np.random.normal(1.3, 0.2, 100000)
s13 = np.random.normal(1.8, 0.3, 100000)

fig, ax = plt.subplots(figsize=(6, 6))

h = ax.hist2d(s12, s13, bins=150, cmap="Reds")
fig.colorbar(h[3], ax=ax)

ax.set_xlabel(r"$m_{12}^2$")
ax.set_ylabel(r"$m_{13}^2$")
ax.set_title("Dalitz Plot")

plt.savefig("img/dltz_plt_2.png")
plt.show()