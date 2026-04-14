import os
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4*np.pi, 100)
x = np.sin(t)

D = np.abs(x[:, None] - x[None, :])

off_diag = D[~np.eye(len(x), dtype=bool)]
eps = np.percentile(off_diag, 10)

R = (D <= eps).astype(int)

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(R, cmap="binary", origin="lower", interpolation="nearest", aspect="equal")
ax.set_title(f"Recurrence Plot (eps={eps})")
ax.set_xlabel("Time index j")
ax.set_ylabel("Time index i")

os.makedirs("img", exist_ok=True)
plt.savefig("img/rcrrnc_plt.png")
plt.show()