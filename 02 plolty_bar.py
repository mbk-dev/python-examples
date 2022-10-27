import plotly.express as px
import okama as ok

s = ok.AssetList(['SPY.US', 'AGG.US', 'GC.COMM'], inflation=False).get_cagr()

fig = px.bar(s, x=s.index, y=s.values * 100, color=['red', 'green', 'yellow'])
fig.show()
