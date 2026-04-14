import numpy as np
import matplotlib.pyplot as plt

def funnel_plot(effect, se, ax=None):
    effect = np.asarray(effect, dtype=float)
    se = np.asarray(se, dtype=float)

    if effect.shape != se.shape:
        raise ValueError("effect and se must have the same shape")

    mask = np.isfinite(effect) & np.isfinite(se) & (se > 0)
    effect = effect[mask]
    se = se[mask]

    if len(effect) < 2:
        raise ValueError("Need at least 2 valid studies")

    w = 1 / se**2
    mu = np.average(effect, weights=w)

    order = np.argsort(se)
    se_sorted = se[order]

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6), layout="constrained")
    else:
        fig = ax.figure

    ax.scatter(effect, se, alpha=0.7)
    ax.axvline(mu, linewidth=1)

    ax.plot(mu + 1.96 * se_sorted, se_sorted, linestyle="--")
    ax.plot(mu - 1.96 * se_sorted, se_sorted, linestyle="--")

    ax.invert_yaxis()
    ax.set_xlabel("Effect estimate")
    ax.set_ylabel("Standard error")
    ax.set_title("Funnel plot")

    return fig, ax, {"pooled_effect": mu}

effect = np.array([0.12, 0.05, -0.03, 0.20, 0.08, 0.15, -0.01, 0.10, 0.18, 0.04])
se = np.array([0.04, 0.06, 0.09, 0.03, 0.05, 0.04, 0.08, 0.05, 0.03, 0.07])

w = 1 / se**2
mu = np.average(effect, weights=w)

order = np.argsort(se)
se_sorted = se[order]

fig, ax = plt.subplots(figsize=(6, 6))

ax.scatter(effect, se)

ax.axvline(mu, linewidth=1)

ax.plot(mu + 1.96 * se_sorted, se_sorted, linestyle="--")
ax.plot(mu - 1.96 * se_sorted, se_sorted, linestyle="--")

ax.invert_yaxis()

ax.set_xlabel("Effect estimate")
ax.set_ylabel("Standard error")
ax.set_title("Funnel Plot")

plt.savefig("img/fnnl_plt.png")
plt.show()