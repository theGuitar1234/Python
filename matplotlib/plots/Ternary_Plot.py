import plotly.express as px

df = px.data.iris()
fig = px.scatter_ternary(df, a="sepal_length", b="sepal_width", c="petal_length", color="species", size_max=20)

fig.show()