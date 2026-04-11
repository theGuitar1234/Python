import matplotlib.pyplot as plt
import pandas as pd

df2 = pd.read_csv('data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv')

plt.title("histogram")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.show()