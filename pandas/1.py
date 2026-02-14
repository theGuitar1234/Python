import pandas as pd 

df = {}
df1 = {}
df2 = {}

rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

rng = pd.date_range("1/1/2012", periods=700, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])

