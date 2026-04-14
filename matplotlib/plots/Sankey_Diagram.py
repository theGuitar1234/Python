import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])

sankey = Sankey(ax=ax, scale=1.0, unit=None)

whole = 100
rhd_neg = 20
all_del = 5
asian_del = 4

sankey.add(
    flows=[whole, -rhd_neg, -(whole - rhd_neg)],
    labels=['Whole population', 'RhD-negative', 'Other'],
    orientations=[0, -1, 1]
)

sankey.finish()
plt.title("Hierarchy shown as Sankey")
plt.savefig("img/snky_dgrm.png")
plt.show()