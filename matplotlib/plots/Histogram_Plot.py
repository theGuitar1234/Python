import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import colors

# data = np.random.randn(1000)
# # plt.hist(data, bins=100, color='lightblue', edgecolor='black')
# sns.histplot(data, bins=30, kde=True, color='blue', edgecolor='white')
# plt.show()

# np.random.seed(23685752)
# N_points = 10000

# x = np.random.randn(N_points)
# y = 0.8 ** x + np.random.randn(N_points) + 25

# fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

# N, bins, patches = axs.hist(x, bins=20)

# fracs = ((N ** (1 / 5)) / N.max())
# norm = colors.Normalize(fracs.min(), fracs.max())

# for thisfrac, thispatch in zip(fracs, patches):
#     color = plt.cm.viridis(norm(thisfrac))
#     thispatch.set_facecolor(color)
# plt.show()

data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)
plt.hist([data1, data2], bins=30, stacked=True, color=['red', 'blue'], edgecolor='green')

plt.savefig("img/hstgrm_plt.png")
plt.show()