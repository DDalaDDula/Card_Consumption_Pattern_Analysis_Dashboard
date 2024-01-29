from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from graph.bar_plot1 import generate_graph
from graph.graph2 import graph2
from graph.graph3 import app as graph
from assets import style_dic # 딕셔너리 형태의 style지정파일(python file)

# card dataset & dictionary
jg_df = pd.read_csv("jg_df.csv")
ddc_df = pd.read_csv("ddc_df.csv")
nj_df = pd.read_csv("nj_df.csv")
df_map = {"/sum":jg_df, "/jg":jg_df, "/ddc":ddc_df, "/nj":nj_df}

def area_detail_page(pathname, df_map):
    # Dropdown에 들어갈 옵션 리스트 생성
    graph_options = ['Counts', 'Costs']
    df = df_map.get(pathname, None)
    if df is None:
        return html.Div("Page not found")

    return html.Div([
        dcc.Dropdown(
            id='graph-dropdown',
            options=[{'label': option, 'value': option} for option in graph_options],
            value=graph_options[0],  # 기본 선택값 설정
            placeholder="Select",
            style=style_dic.dropdown_styl  # Dropdown style
        ),
        html.Div(id='bar-chart-container'),  # 그래프를 넣을 컨테이너 추가
    ])

# area_detail_page.py에 새로 추가된 함수
def generate_area_detail_page_callbacks(app):
    @app.callback(Output('bar-chart-container', 'children'),[Input('graph-dropdown', 'value'), Input("url", "pathname")])
    def update_graph(selected_graph, pathname):
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("Page not found")
        return generate_graph(df, selected_graph, style_dic.bar_plot1_styl)
