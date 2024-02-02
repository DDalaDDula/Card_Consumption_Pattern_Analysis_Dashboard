from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

app = Dash(__name__)

models = {'Linear Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

iris_data = px.data.iris()

app.layout = html.Div([
    html.H4("Predicting Iris Sepal Width"),
    html.P("Select model:"),
    dcc.Dropdown(
        id='dropdown-model',
        options=models.keys(),
        value='Decision Tree',
        clearable=False
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input('dropdown-model', "value"))
def train_and_display(selected_model):
    X = iris_data['sepal_length'].values[:, None]
    y = iris_data['sepal_width']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=42)

    model = models[selected_model]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train,
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test,
                   name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range,
                   name='prediction')
    ])
    fig.update_layout(title=f"Predicting Iris Sepal Width - {selected_model}")
    return fig