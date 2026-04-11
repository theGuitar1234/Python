import matplotlib.pyplot as plt
import pandas as pd

df2 = pd.read_csv('data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv')
df2['Datetime'] = pd.to_datetime(df2['Timestamp'])
df2.sort_values("Datetime", inplace=True, ascending=False)
plt.plot(df2['Datetime'])
plt.show()

# print(df2['Datetime'].plot(kind="line")) # Works on Jupyter. Automatically plots