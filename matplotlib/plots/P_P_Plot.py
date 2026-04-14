# from scipy import stats
# stats.probplot(x, dist="expon", plot=ax)

import matplotlib.pyplot as plt
import statsmodels.api as sm
from spicy import stats

x = stats.expon.rvs(size=500, random_state=42)

fix,ax = plt.subplots(figsize=(6,6))
sm.ProbPlot(x, dist=stats.expon, fit=True).ppplot(line='45', ax=ax)
plt.savefig("img/pp_plt.png")
plt.show()