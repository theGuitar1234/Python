import numpy as np
import matplotlib.pyplot as plt

w = np.logspace(-2, 2, 2000)

H = 10 / ((1j * w)**2 + 0.8 * (1j * w) + 1)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(H.real, H.imag, label="Positive frequencies")
ax.plot(H.real, -H.imag, linestyle="--", label="Negative frequencies")

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)
ax.plot(-1, 0, "x", markersize=10, label="Critical point (-1, 0)")

ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_title("Nyquist Plot")
ax.set_aspect("equal")
ax.grid(True)
ax.legend()

plt.savefig("img/nyqst_plt_2.png")
plt.show()

