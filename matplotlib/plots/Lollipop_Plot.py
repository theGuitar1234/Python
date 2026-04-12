import matplotlib.pyplot as plt
import numpy as np

y = np.random.randint(100, size=(100))
x = np.arange(0, len(y), 1)

fig, ax = plt.subplots()

# ax.stem(x, y, basefmt=' ')
ax.hlines(x, xmin=0, xmax=y)
ax.plot(y, x, "o")
ax.set_ylim(0)

plt.savefig("img/lllpp_plt.png")
plt.show()