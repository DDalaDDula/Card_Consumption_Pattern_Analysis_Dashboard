import dash
from dash import html
from graph.graph1 import graph1
from graph.graph2 import graph2
from graph.graph3 import app as graph
import plotly.express as px

# Iris dataset
iris_data = px.data.iris()

# Dash application
app = dash.Dash(__name__)

# graph of the dashboard
app.layout = html.Div([
    html.H1("Iris Dataset Dashboard", style={'text-align': 'center'}),
    graph1(iris_data),
    graph2(iris_data),
    #graph.layout
    
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(debug=False, host='0.0.0.0', port=8888)
