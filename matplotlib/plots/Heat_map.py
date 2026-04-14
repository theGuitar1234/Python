import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")
heatmap_data = data.pivot_table(index="day", columns="sex", values="tip", aggfunc="mean")
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu")
plt.savefig("img/ht_mp.png")
plt.show()