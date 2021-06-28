import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash()
df = pd.read_csv('arthur.hoffman@ampf.csv')
dfff = pd.read_csv('convoTest.csv')

trace1 = go.Pie(
    labels=['Microsoft', 'Amazon', 'Honeywell'],
    values=[15, 30, 42],
    name='Lets Test This'
)
dataTestPieChart = [trace1]
layout = go.Layout(title='Overall Engagement Per Campaign')
pie_fig = go.Figure(data=dataTestPieChart,layout=layout)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(children=[
    html.H1(
        children='Weekly Overview',
        style={
            'textAlign': 'center'
        }
    ),
    html.Div(children='A summary of this weeks campaign actions and performance', style={
        'textAlign': 'center'
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [104, 131, 152, 118, 127, 140, 100], 'type': 'bar', 'name': 'Microsoft Engineers'},
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [56, 100, 135, 140, 77, 160, 106], 'type': 'bar', 'name': u'Amazon Engineers'},
            ],
            'layout': {
                'xaxis':{'title':'Day of The Week'},
                'yaxis':{'title':'Num Messages Sent'},
                'font': {'color': 'black'}
            }
        }
    )
,
    dcc.Graph(
        id='Graph2',
        figure={
            'data': [
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [4, 1, 2, 10, 15, 30, 42], 'type': 'bar', 'name': 'Microsoft Engineers'},
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [2, 4, 5, 8, 20, 33, 77], 'type': 'bar', 'name': u'Amazon Engineers'},

            ],
            'layout': {
                'title':'New Connections',
                'xaxis':{'title':'Day of The Week'},
                'yaxis':{'title':'New Connections Made'},
                'font': {'color': 'black'}
            }
        }
    )
    ,
    html.Div([
        dcc.Graph(
        id='Graph3',
        figure={
            'data': [
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [4, 1, 2, 10, 15, 30, 42], 'type': 'line', 'name': 'Microsoft Engineers'},
                {'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'y': [2, 4, 5, 8, 20, 33, 77], 'type': 'line', 'name': u'Amazon Engineers'},
            ],
            'layout': {
                'title':'Conversations',
                'xaxis':{'title':'Day of The Week'},
                'yaxis':{'title':'Conversations Started'},
                'font': {'color': 'black'}
            }
        }
    ),

    html.Div(className='mat-card', style={"display": "block", "margin": "15px"},
             children=[
                 html.H4(children='Segments size'),
                 dcc.Graph(
                     figure=pie_fig
                 )
             ])

    ], className="row"),
dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10,
)

    ]
)










if __name__ == '__main__':
    app.run_server()