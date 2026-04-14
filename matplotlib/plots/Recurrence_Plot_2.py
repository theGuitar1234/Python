import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")
rng = np.random.default_rng(7)

n = 180
u = np.linspace(0, 6 * np.pi, n)

motif = np.sin(u) + 0.35 * np.sin(3 * u)

x = np.r_[
    motif,
    0.8 * motif + 0.12 * rng.normal(size=n),
    np.sin(np.linspace(0, 8 * np.pi, n)) + 0.20 * rng.normal(size=n),
    motif + 0.10 * rng.normal(size=n)
].astype(float)

def delay_embed(x, m=3, tau=2):
    N = len(x) - (m - 1) * tau
    return np.column_stack([x[k:k+N] for k in range(0, m * tau, tau)])

X = delay_embed(x, m=3, tau=2)

D = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)

off_diag = D[~np.eye(len(D), dtype=bool)]

eps = np.percentile(off_diag, 6)

R = D <= eps

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(8, 8),
    gridspec_kw={"height_ratios": [1, 4]}
)

ax1.plot(x, linewidth=0.8, color="white")
ax1.set_title("Signal")
ax1.set_ylabel("Value")
ax1.grid(alpha=0.25)

ii, jj = np.where(R)
ax2.scatter(jj, ii, s=1, c="white", marker="s")
ax2.set_facecolor("black")
ax2.set_title(f"Recurrence Plot (eps={eps:.3f})")
ax2.set_xlabel("Time")
ax2.set_ylabel("Time")
ax2.set_aspect("equal")

plt.tight_layout()
plt.savefig("img/rcrrnc_plt_2.png")
plt.show()