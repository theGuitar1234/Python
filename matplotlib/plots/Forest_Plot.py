import numpy as np
import matplotlib.pyplot as plt

def forest_plot(est, ci_low, ci_high, labels, ax=None, null=0):
    est = np.asarray(est, dtype=float)
    ci_low = np.asarray(ci_low, dtype=float)
    ci_high = np.asarray(ci_high, dtype=float)

    if not (len(est) == len(ci_low) == len(ci_high) == len(labels)):
        raise ValueError("est, ci_low, ci_high, and labels must have the same length")

    y = np.arange(len(est))

    xerr = np.vstack([est - ci_low, ci_high - est])

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 0.5 * len(est) + 1), layout="constrained")
    else:
        fig = ax.figure

    ax.errorbar(
        est, y,
        xerr=xerr,
        fmt="o",
        linestyle="none",
        capsize=3
    )

    ax.axvline(null, linewidth=1)

    ax.set_yticks(y, labels=labels)
    ax.invert_yaxis()
    ax.set_xlabel("Effect estimate")
    ax.set_ylabel("")
    ax.set_title("Forest Plot")

    return fig, ax

labels = ["Study A", "Study B", "Study C", "Study D"]
est = np.array([0.20, -0.10, 0.35, 0.05])
ci_low = np.array([0.05, -0.30, 0.10, -0.08])
ci_high = np.array([0.35,  0.10, 0.60,  0.18])

# fig, ax = forest_plot(est, ci_low, ci_high, labels, null=0)
fig, ax = forest_plot(est, ci_low, ci_high, labels, null=1)
ax.set_xscale("log")
ax.set_xlabel("Odds ratio")
plt.savefig("img/frst_plt.png")
plt.show()