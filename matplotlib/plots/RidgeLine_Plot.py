import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

rng = np.random.default_rng(42)

years = np.arange(1976, 1985)
data = {
    year: rng.normal(loc=3.1 + 0.03 * (year - 1976), scale=0.22, size=250)
    for year in years
}

fig, ax = plt.subplots(figsize=(10, 6))

x_grid = np.linspace(1.8, 4.1, 400)
spacing = 1.0

for i, year in enumerate(years):
    values = data[year]

    kde = gaussian_kde(values)
    density = kde(x_grid)

    density = density / density.max() * 0.9

    baseline = i * spacing

    ax.fill_between(x_grid, baseline, baseline + density, alpha=0.6)
    ax.plot(x_grid, baseline + density, linewidth=1)
    ax.hlines(baseline, x_grid.min(), x_grid.max(), linewidth=0.8)

ax.set_yticks(np.arange(len(years)) * spacing)
ax.set_yticklabels(years)
ax.set_xlabel("wage")
ax.set_ylabel("year")
ax.set_title("Ridgeline Plot")

plt.savefig("img/rdgln_plt.png")
plt.show()