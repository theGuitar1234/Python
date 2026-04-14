import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/headbrain3.csv')
X = df[['Head_size']]
y = df['Brain_weight']

X_c = sm.add_constant(X)

lr = LinearRegression()
lr.fit(X_c, y)

y_pred = lr.predict(X_c)
res = y - y_pred

plt.scatter(X, res)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Head Size')
plt.ylabel('Residuals')
plt.savefig("img/rgrssn_2.png")
plt.show()