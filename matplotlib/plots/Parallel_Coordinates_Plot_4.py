import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + 1 + 0.1 * np.random.randn(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data points', color='blue', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')

plt.plot(x, 2 * x + 1, color='red', linestyle='--', label='True Regression Line')

plt.legend()

plt.grid(True)
plt.savefig("img/prlll_crdnts_plt.png")
plt.show()