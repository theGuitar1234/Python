import numpy as np
import matplotlib.pyplot as plt

def bland_altman_plot(a, b, ax=None):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")

    mask = np.isfinite(a) & np.isfinite(b)
    a = a[mask]
    b = b[mask]

    if len(a) < 2:
        raise ValueError("Need at least 2 valid paired observations")

    avg = (a + b) / 2
    diff = a - b

    mean_diff = np.mean(diff)
    sd_diff = np.std(diff, ddof=1)

    loa_upper = mean_diff + 1.96 * sd_diff
    loa_lower = mean_diff - 1.96 * sd_diff

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    else:
        fig = ax.figure

    ax.scatter(avg, diff, alpha=0.7)

    ax.axhline(mean_diff, linestyle='-', label=f'Bias = {mean_diff:.3f}')
    ax.axhline(loa_upper, linestyle='--', label=f'+1.96 SD = {loa_upper:.3f}')
    ax.axhline(loa_lower, linestyle='--', label=f'-1.96 SD = {loa_lower:.3f}')

    ax.set_title("Bland–Altman Plot")
    ax.set_xlabel("Mean of two methods")
    ax.set_ylabel("Difference between methods (A - B)")
    ax.legend()

    return fig, ax, {
        "bias": mean_diff,
        "sd_diff": sd_diff,
        "loa_upper": loa_upper,
        "loa_lower": loa_lower,
    }

a = [101, 98, 105, 110, 95, 99, 102, 108]
b = [100, 97, 103, 111, 96, 100, 101, 107]

fig, ax, stats = bland_altman_plot(a, b)
plt.savefig("img/blnd_tmn_plt.png")
plt.show()

print(stats)
# {
#     'bias': np.float64(0.375), 
#     'sd_diff': np.float64(1.1877349391654208), 
#     'loa_upper': np.float64(2.702960480764225), 
#     'loa_lower': np.float64(-1.952960480764225)
# }