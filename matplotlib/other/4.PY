import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(True, alpha=0.3)

ax.plot([5, 60], [10, 23], marker='o', alpha=0.4)

plt.show()

