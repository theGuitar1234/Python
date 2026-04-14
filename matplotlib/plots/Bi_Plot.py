import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 5.1, 1.8],
    [5.5, 2.3, 4.0, 1.3],
    [6.5, 2.8, 4.6, 1.5]
])

feature_names = ["Sepal length", "Sepal width", "Petal length", "Petal width"]

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X2 = pca.fit_transform(X_scaled)

loadings = pca.components_.T

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(X2[:, 0], X2[:, 1], alpha=0.7)

for i, (lx, ly) in enumerate(loadings):
    ax.arrow(0, 0, lx, ly, head_width=0.05, length_includes_head=True)
    ax.text(lx * 1.1, ly * 1.1, feature_names[i])

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA Biplot")

plt.savefig("img/b_plt.png")
plt.show()