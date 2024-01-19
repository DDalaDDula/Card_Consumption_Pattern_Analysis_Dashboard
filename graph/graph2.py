from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

def graph2(iris_data):
    # Linear regression model
    regression_model = LinearRegression()
    regression_model.fit(iris_data[['petal_length']], iris_data['petal_width'])
    iris_data['predicted_petal_width'] = regression_model.predict(iris_data[['petal_length']])
    
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
            figure=px.scatter(iris_data, x='petal_length', y='petal_width', color='species', title='Regression Plot', trendline='ols'),
            config={'displayModeBar': False}  # Hide the modebar
        ),
    ], style={'display': 'flex', 'justify-content': 'center'})
