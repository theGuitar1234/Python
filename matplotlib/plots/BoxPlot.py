import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(10)
# d = np.random.normal(100, 20, 200)

# fig = plt.figure(figsize=(10,7))
# plt.boxplot(d)

# d_1 = np.random.normal(100, 10, 200)
# d_2 = np.random.normal(90, 20, 200)
# d_3 = np.random.normal(80, 30, 200)
# d_4 = np.random.normal(70, 40, 200)
# d = [d_1, d_2, d_3, d_4]

# ax = fig.add_axes([0, 0, 1, 1])
# bp = ax.boxplot(d)

np.random.seed(10)
d_1 = np.random.normal(100, 10, 200)
d_2 = np.random.normal(90, 20, 200)
d_3 = np.random.normal(80, 30, 200)
d_4 = np.random.normal(70, 40, 200)
d = [d_1, d_2, d_3, d_4]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(d, patch_artist = True,
                notch ='True', vert = 0)

colors = ['#0000FF', '#00FF00', 
          '#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")

for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)

for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)

for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)

ax.set_yticklabels(['d_1', 'd_2', 
                    'd_3', 'd_4'])
 
plt.title("Customized box plot")

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.savefig("img/bxplt.png")
plt.show()