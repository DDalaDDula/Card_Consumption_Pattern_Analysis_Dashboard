import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import markdown2

from graph.bar_plot1 import generate_graph
from graph.graph2 import graph2
from graph.graph3 import app as graph

from assets import style_dic # 딕셔너리 형태의 style지정파일

# Iris dataset
iris_data = px.data.iris()

# card dataset
jg_df = pd.read_csv("jg_df.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

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

# Dropdown에 들어갈 옵션 리스트 생성
graph_options = ['Counts', 'Costs']

# Nav bar 선택에 따라 페이지 업데이트하는 콜백 함수
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/jg":
        return html.Div([
            dcc.Dropdown(
                id='graph-dropdown',
                options=[{'label': option, 'value': option} for option in graph_options],
                value=graph_options[0],  # 기본 선택값 설정
                style={'width': '50%'}  # Dropdown의 너비 설정
            ),
            html.Div(id='bar-chart-container'),  # 그래프를 넣을 컨테이너 추가
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

# Dropdown 선택에 따라 그래프 업데이트하는 콜백 함수
@app.callback(Output('bar-chart-container', 'children'),[Input('graph-dropdown', 'value')])
def update_graph(selected_graph):
    return generate_graph(jg_df, selected_graph)

# 대시보드 제목과 설명을 클릭하면 홈화면으로 넘어갈 수 있는 콜백함수(Callback to handle clicking on the dashboard heading and description)
@app.callback(Output("url", "pathname"), [Input("dashboard-heading", "n_clicks"), Input("dashboard-description", "n_clicks")])
def go_to_homepage(click_heading, click_description):
    if click_heading or click_description:
        return "/"
    return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
