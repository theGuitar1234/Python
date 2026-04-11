import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

plt.hist(df['Attack'], bins=69, color='red', edgecolor='green')
plt.boxplot(df['Speed'])
plt.pie(df['Name'].value_counts(), labels=df['Name'].value_counts().index, autopct='%1.1f%%', startangle=135, counterclock=True)
plt.plot(df['HP'], df['Sp. Atk'])

plt.show()