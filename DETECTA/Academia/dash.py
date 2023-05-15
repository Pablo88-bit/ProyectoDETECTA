#import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

app = DjangoDash('MyDashApp')

app.layout = html.Div([
    dcc.Graph(id='example-graph', figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Example'}
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    })
])
