from dash import html, dcc
import plotly.express as px

def graph2(iris_data):
    return html.Div([

        # Histogram
        dcc.Graph(
            id='histogram',
            figure=px.histogram(iris_data, x='petal_length', color='species', title='Histogram'),
            config={'displayModeBar': False}  # Hide the modebar
        ),

        # Regression visualization
        dcc.Graph(
            id='regression-plot',
            figure=px.scatter(iris_data, x='petal_length', y='petal_width', color='species', title='Regression Plot'),
            config={'displayModeBar': False}  # Hide the modebar
        ),
    ], style={'display': 'flex', 'justify-content': 'center'})
