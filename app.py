import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from graph.graph1 import graph1
from graph.graph2 import graph2
from graph.graph3 import app as graph
import plotly.express as px
import markdown2

# Iris dataset
iris_data = px.data.iris()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/styles/nav.css'])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#353535",
    "color": "#ffffff",
    "-webkit-text-stroke-width": "thick"
}

# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

navlink_style = {
    "color": "#ffffff",
    "margin-top": "1rem",
    "font-size": "1.3rem",
}
sidebar = html.Div(
    [
        html.H3("📋Dashboard", className="3"),
        html.P(
            "Card Consumption Pattern Analysis", className="lead"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("서울특별시", href="/jg", active="exact", style=navlink_style),
                dbc.NavLink("경기도", href="/ddc", active="exact", style=navlink_style),
                dbc.NavLink("전라남도", href="/nj", active="exact", style=navlink_style),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style={"backgroundColor": "#353535", "color": "#ffffff"})

# Read README file
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_content = readme_file.read()
    
# Markdown to HTML function
def markdown_to_html(markdown_text):
    return dcc.Markdown(children=markdown_text)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/jg":
        return html.Div([
                html.H1("Card Consumption Pattern Analysis Dashboard", style={'text-align': 'center'}),
                graph1(iris_data),
        ])
    elif pathname == "/ddc":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/nj":
        return html.P("Oh cool, this is page 2!")

    # basic page setting(readme)
    return markdown_to_html(readme_content)

if __name__ == "__main__":
    app.run_server(debug=True)


# app.layout = dbc.Container(
#     [
#         dcc.Store(id="store"),
#         html.Div([html.H1("Dynamically rendered tab content", style={'font-weight': 'bold'})], style={'margin': '5%'}),
#         html.Hr(),
#         dbc.Tabs(
#             [
#                 dbc.Tab(label="중구", tab_id="jg"),
#                 dbc.Tab(label="동두천시", tab_id="ddc"),
#                 dbc.Tab(label="나주시", tab_id="nj"),
#             ],
#             id="tabs",
#             active_tab="jg",
#         ),
#         html.Div(id="tab-content", className="p-4"),
#     ]
# )

# @app.callback(
#     Output("tab-content", "children"),
#     [Input("tabs", "active_tab"), Input("store", "data")],
# )
# def render_tab_content(active_tab, data):
#     """
#     This callback takes the 'active_tab' property as input, as well as the
#     stored graphs, and renders the tab content depending on what the value of
#     'active_tab' is.
#     """
#     if active_tab and data is not None:
#         if active_tab == "jg":
#             return dcc.Graph(figure=data["scatter"])
#         elif active_tab == "ddc":
#             return dbc.Row(
#                 [
#                     dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
#                     dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
#                 ]
#             )
#         elif active_tab == "nj":
#             return dbc.Row(
#                 [
#                     dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
#                     dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
#                 ]
#             )
#     return "No tab selected"


# @app.callback(Output("store", "data"), [Input("button", "n_clicks")])
# def generate_graphs(n):
#     """
#     This callback generates three simple graphs from random data.
#     """
#     if not n:
#         # generate empty graphs when app loads
#         return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}

#     # simulate expensive graph generation process
#     time.sleep(2)

#     # generate 100 multivariate normal samples
#     data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

#     scatter = go.Figure(
#         data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
#     )
#     hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
#     hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])

#     # save figures in a dictionary for sending to the dcc.Store
#     return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2}


# if __name__ == "__main__":
#     app.run_server(debug=True)

# # Iris dataset
# iris_data = px.data.iris()

# # Dash application
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # graph of the dashboard
# app.layout = html.Div([
#     html.H1("Card Consumption Pattern Analysis Dashboard", style={'text-align': 'center'}),
#     graph1(iris_data),
#     graph2(iris_data),
#     #graph.layout
    
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
#     #app.run_server(debug=False, host='0.0.0.0', port=8888)
