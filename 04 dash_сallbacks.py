from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go
import okama as ok

app = Dash(__name__)

app.layout = html.Div(
        children=[
            html.H1('Сравнение активов'),
            dcc.Dropdown(
                options=['SPY.US', 'BND.US', 'GLD.US', 'VNQ.US', 'MCFTR.INDX'],
                multi=True,
                placeholder='Выберите ценные бумаги',
                id='assets',
                value='SPY.US'
            ),
            html.Button(id="button", n_clicks=0, children="Отобразить график"),
            dcc.Graph(
                id='wealth_indexes'
            ),
            daq.BooleanSwitch(
                id='logarithmic-switch',
                on=False,
                label='Логарифмическая шкала',
                labelPosition='bottom'
            )

        ]
    )


@app.callback(
    Output('wealth_indexes', 'figure'),
    Input('logarithmic-switch', 'on'),
    Input('button', 'n_clicks'),
    State('assets', 'value')
)
def update_graf(on, n_clicks, value: list):
    symbols = value if isinstance(value, list) else [value]
    df = ok.AssetList(symbols, ccy='USD', inflation=True).wealth_indexes
    index = df.index.to_timestamp('M')

    fig = px.line(df, x=index, y=df.columns[:-1], log_y=on, height=800)
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
    return fig


app.run_server(debug=True)
