import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])
ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1))
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)
plt.show()