from matplotlib.patches import Ellipse, Polygon
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

top = Ellipse((5, 8), width=3, height=1, facecolor="skyblue", edgecolor="black")
ax.add_patch(top)

connector = Polygon(
    [(4.6, 7.8), (5.4, 7.8), (5.2, 5.2), (4.8, 5.2)],
    closed=True,
    facecolor="mediumseagreen",
    edgecolor="black"
)
ax.add_patch(connector)

bottom = Ellipse((5, 4.7), width=2.2, height=0.9, facecolor="lightgreen", edgecolor="black")
ax.add_patch(bottom)

plt.show()