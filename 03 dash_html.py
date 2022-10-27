from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import okama as ok

app = Dash(__name__)

df = ok.AssetList(['RGBITR.INDX', 'RUCBITR.INDX', 'OKID.INDX'], ccy='RUB', inflation=True).wealth_indexes
index = df.index.to_timestamp('M')

fig = px.line(df, x=index, y=df.columns[:-1], log_y=True, height=800)
fig.add_trace(
    go.Scatter(
        x=index,
        y=df.iloc[:, -1],
        mode='none',
        fill='tozeroy',
        fillcolor='rgba(26,150,65,0.5)',
        name='Inflation'
    )
)

fig.update_xaxes(title='Date', rangeslider_visible=True)
fig.update_yaxes(title=None)

app.layout = html.Div(
        children=[
            html.H1('Сравнение активов'),
            dcc.Graph(
                figure=fig
            )
        ]
    )

app.run_server(debug=True)
