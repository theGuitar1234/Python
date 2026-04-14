import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

n = 80000

s12_bg = rng.uniform(0.4, 2.0, n)
s13_bg = 3.2 - s12_bg + rng.normal(0, 0.18, n)

n1 = 25000
s12_r1 = rng.normal(1.0, 0.05, n1)
s13_r1 = rng.uniform(1.0, 3.0, n1)

n2 = 20000
s12_r2 = rng.uniform(0.4, 2.0, n2)
s13_r2 = rng.normal(1.4, 0.05, n2)

s12 = np.concatenate([s12_bg, s12_r1, s12_r2])
s13 = np.concatenate([s13_bg, s13_r1, s13_r2])

mask = (
    (s12 > 0.3) & (s12 < 2.1) &
    (s13 > 1.0) & (s13 < 3.1) &
    (s13 < 3.4 - 0.9 * (s12 - 0.5)) &
    (s13 > 1.0 + 0.15 * (s12 - 1.6)**2)
)

s12 = s12[mask]
s13 = s13[mask]

fig, ax = plt.subplots(figsize=(6, 6))
h = ax.hist2d(s12, s13, bins=220, cmap="Reds")
fig.colorbar(h[3], ax=ax)

ax.set_xlabel(r"$s_{12}$")
ax.set_ylabel(r"$s_{13}$")
ax.set_title("Dalitz Plot")
plt.savefig("img/dltz_plt.png")
plt.show()