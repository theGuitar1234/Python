#Dot plot
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)

x = np.random.normal(loc=70, scale=8, size=40)

fig, ax = plt.subplots(figsize=(8, 2))

ax.scatter(x, np.zeros_like(x), alpha=0.6)

ax.set_yticks([])
ax.set_xlabel("Value")
ax.set_title("1D dot plot")

plt.savefig("img/dt_plt.png")
plt.show()