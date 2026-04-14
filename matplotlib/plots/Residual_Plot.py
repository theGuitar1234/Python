import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

X = np.random.normal(loc=100, scale=10, size=100)
Y = 2 * X + np.random.normal(loc=0, scale=15, size=100)
sns.residplot(x=X, y=Y)
plt.savefig("img/rsdl_plt.png")
plt.show()