import numpy as np
import matplotlib.pyplot as plt

w = np.logspace(-1, 3, 500)

R = 1
C = 1

H = 1 / (1 + 1j * w * R * C)

mag = np.abs(H)
mag_db = 20 * np.log10(mag)
phase_deg = np.angle(H, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.semilogx(w, mag_db)
ax1.set_ylabel("Magnitude (dB)")
ax1.set_title("Bode Plot")
ax1.grid(True, which="both")

ax2.semilogx(w, phase_deg)
ax2.set_xlabel("Frequency (rad/s)")
ax2.set_ylabel("Phase (deg)")
ax2.grid(True, which="both")

plt.savefig("img/bd_plt.png")
plt.show()