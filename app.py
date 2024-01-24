import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from graph.graph1 import graph1
from graph.graph2 import graph2
from graph.graph3 import app as graph
import plotly.express as px
import markdown2
from assets import style_dic # 딕셔너리 형태의 style지정파일

# Iris dataset
iris_data = px.data.iris()

# card dataset
jg_df = pd.read_csv("jg_df.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@500&display=swap'])

sidebar = html.Div(
    [
        html.H1("📋Dashboard", id="dashboard-heading"),
        html.P(
            "📈Card Consumption\nPattern Analysis", className="lead", id="dashboard-description"
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("서울특별시", href="/jg", active="exact", style=style_dic.navlink_style),
                dbc.NavLink("경기도", href="/ddc", active="exact", style=style_dic.navlink_style),
                dbc.NavLink("전라남도", href="/nj", active="exact", style=style_dic.navlink_style),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=style_dic.SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=style_dic.CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style=style_dic.layout_style)

# Read README file
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_content = readme_file.read()
    
# Markdown to HTML function
def markdown_to_html(markdown_text):
    return dcc.Markdown(children=markdown_text, style=style_dic.readme_style)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/jg":
        return html.Div([
            graph1(jg_df),
        ])
    elif pathname == "/ddc":
        return html.Div([
            graph2(iris_data),
        ])
    elif pathname == "/nj":
        return html.Div([
            graph2(iris_data),
        ])

    # basic page setting(readme)
    return markdown_to_html(readme_content)

# Callback to handle clicking on the dashboard heading and description
@app.callback(Output("url", "pathname"), [Input("dashboard-heading", "n_clicks"), Input("dashboard-description", "n_clicks")])
def go_to_homepage(click_heading, click_description):
    if click_heading or click_description:
        return "/"
    return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
