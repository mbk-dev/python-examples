import plotly.express as px
import okama as ok

df = ok.AssetList(['SPY.US', 'AGG.US', 'GC.COMM'], inflation=False).wealth_indexes

fig = px.line(df, x=df.index.to_timestamp('M'), y=df.columns)
fig.show()
