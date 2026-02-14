import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df2 = pd.read_csv('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv')

plt.title("My histogram")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)

#plt.hist(df['Attack'], bins=69, color='red', edgecolor='green')
#plt.boxplot(df['Speed'])
#plt.pie(df['Name'].value_counts(), labels=df['Name'].value_counts().index, autopct='%1.1f%%', startangle=135, counterclock=True)
# plt.plot(df['HP'], df['Sp. Atk'])

df2['Datetime'] = pd.to_datetime(df2['Timestamp'])
df2.sort_values("Datetime", inplace=True, ascending=False)
# plt.plot(df2['Datetime'])

print(df2['Datetime'].plot(kind="line")) # works on Jupyter

# plt.show()