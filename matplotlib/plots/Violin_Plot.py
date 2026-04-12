import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# np.random.seed(1)
# data = np.random.randn(100)

# plt.violinplot(data, showmedians=True)

# plt.savefig("img/vln_plt.png")
# plt.show()

np.random.seed(2)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1.5, 100)
data3 = np.random.normal(-2, 0.5, 100)
categories = ['Category 1', 'Category 2', 'Category 3']
all_data = [data1, data2, data3]

plt.violinplot(all_data, showmedians=True)

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bivariate Violin Plot')

plt.xticks(np.arange(1, len(categories) + 1), categories)
plt.savefig("img/vln_plt.png")
plt.show()