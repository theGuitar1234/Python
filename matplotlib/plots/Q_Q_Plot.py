import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

datapoints = np.random.normal(0, 1, 100)
sm.qqplot(datapoints, line='45')
plt.savefig("img/qq_plt.png")
plt.show()