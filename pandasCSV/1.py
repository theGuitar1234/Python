import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Trending_Movies.csv')

data = {
    "Name": ["Alice", "Bob", "Charlie", "Dana"],
    "Gender": ["Female", "Male", "Male", "Female"],
    "Salary": [60000, 72000, 65000, 62000],
    "Department": ["HR", "IT", "IT", "HR"]
}

df = pd.DataFrame(data)

df['Salary'] = df['Salary'].astype(str)
df['Salary'] += "$"
df['Salary'] = df['Salary'].apply(lambda x: x[:-1])
df.sort_values('Name', inplace=True)

df.sort_index(ascending=False, inplace=True)

df['Salary_Rank'] = df['Salary'].rank()

print(df)

s = pd.DataFrame(
    {"Values": [100, 200, 200, 300]}
)
s['Rankings'] = s.rank(method="average")
print(s)

print(df["Gender"].value_counts(normalize=True))

print(df['Gender'].index)

