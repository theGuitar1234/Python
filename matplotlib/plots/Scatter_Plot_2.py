import matplotlib.pyplot as plt
import pandas as pd
import random

fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(True, alpha=0.3)

n = 1

for i in range(0, 100):
    ax.scatter(random.randint(i-10 - n, i+10 - n), random.randint(i-10 - n, i+10 - n))
    n -= 1

plt.savefig("img/scttr_plt_2.png")
plt.show()