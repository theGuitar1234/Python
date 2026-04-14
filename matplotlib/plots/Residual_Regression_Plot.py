import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt  
import statsmodels.api as sm  
from statsmodels.formula.api import ols 
df = pd.read_csv('data/headbrain3.csv')  

lm = ols('Brain_weight ~ Head_size', data=df).fit()
print(lm.summary())
fig = plt.figure(figsize=(14, 8))
fig = sm.graphics.plot_regress_exog(lm, 'Head_size', fig=fig)
plt.savefig("img/rgrssn_plt.png")
plt.show()