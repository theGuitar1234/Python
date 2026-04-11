import matplotlib.pyplot as plt
import numpy as np

plt.ion()  # interactive mode on

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)

x_data = []
y_data = []

for i in range(100):
    x_data.append(i)
    y_data.append(np.sin(i * 0.1))

    line.set_data(x_data, y_data)

    # if limits can change:
    # ax.relim()
    # ax.autoscale_view()

    fig.canvas.draw_idle()
    plt.pause(0.05)   # GUI update