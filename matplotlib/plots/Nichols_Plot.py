import numpy as np
import matplotlib.pyplot as plt

w = np.logspace(-2, 2, 1000)

# Example second-order transfer function:
# H(jw) = 10 / ((jw)^2 + 0.8(jw) + 1)
H = 10 / ((1j * w)**2 + 0.8 * (1j * w) + 1)

mag_db = 20 * np.log10(np.abs(H))
phase_deg = np.unwrap(np.angle(H)) * 180 / np.pi

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(phase_deg, mag_db)
ax.axvline(-180, linewidth=1)
ax.axhline(0, linewidth=1)

ax.set_xlabel("Phase (degrees)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title("Nichols Plot")
ax.grid(True)
plt.savefig("img/nchls_plt.png")
plt.show()