import numpy as np
import matplotlib.pyplot as plt

w = np.logspace(-2, 2, 500)

H = 1 / (1 + 1j * w)

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

plt.show()