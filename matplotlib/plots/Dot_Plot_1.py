import matplotlib.pyplot as plt

categories = {
    "Badminton": 6,
    "Tennis": 2,
    "Soccer": 5,
    "Ice Hockey": 1,
    "Basketball": 3
}

labels = list(categories.keys())
counts = list(categories.values())
x_positions = range(len(labels))

x_dots = []
y_dots = []

for i, count in enumerate(counts):
    x_dots.extend([i] * count)
    y_dots.extend(range(1, count + 1))

fig, ax = plt.subplots(figsize=(9, 4))
ax.grid(axis="y", alpha=0.2)
ax.scatter(x_dots, y_dots, s=200, alpha=0.8, edgecolors="black")
ax.set_xticks(list(x_positions))
ax.set_xticklabels(labels)
ax.set_ylabel("How Many")
ax.set_ylim(0.5, 6.8)
ax.set_yticks(range(1, 7))
ax.set_title("Preferred Sports Dot Plot")
plt.savefig("img/dt_plt_1.png")
plt.show()