from dash import html, dcc
import plotly.express as px

def graph1(iris_data):
    return html.Div([

        # Scatter plot
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(iris_data, x='sepal_width', y='sepal_length', color='species', title='Scatter Plot'),
            config={'displayModeBar': False}  # Hide the modebar
        ),

        # Box plot
        dcc.Graph(
            id='box-plot',
            figure=px.box(iris_data, x='species', y='petal_width', title='Box Plot'),
            config={'displayModeBar': False}  # Hide the modebar
        ),
    ], style={'display': 'flex', 'justify-content': 'center', "backgroundColor": "#353535", "color": "#ffffff"})
