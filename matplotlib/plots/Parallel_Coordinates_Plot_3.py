import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_class_names = iris.target_names

colors = sns.color_palette('husl', n_colors=len(iris_class_names))

class_dfs = [iris_df[iris_df['target'] == i].drop('target', axis=1) for i in range(len(iris_class_names))]

plt.figure(figsize=(12, 8))

for i, class_df in enumerate(class_dfs):
    sns.lineplot(data=class_df, palette=[colors[i]])

plt.title('Parallel Coordinates Plot - Iris Dataset')
plt.xlabel('Features')
plt.ylabel('Feature Values')

plt.legend(iris_class_names, loc='upper right')
plt.savefig("img/prlll_crdnts_plt.png")
plt.show()