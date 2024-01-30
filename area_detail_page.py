from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from graph.bar_plot1 import generate_bar_chart
from graph.pie_plot1 import generate_pie_chart
from graph.graph3 import app as graph

# card dataset & dictionary
jg_df = pd.read_csv("dataset/jg_df.csv")
ddc_df = pd.read_csv("dataset/ddc_df.csv")
nj_df = pd.read_csv("dataset/nj_df.csv")
df_map = {"/jg":jg_df, "/ddc":ddc_df, "/nj":nj_df} #"/sum":jg_df, 

def area_detail_page(pathname, style_dic):
    # Dropdown에 들어갈 옵션 리스트 생성
    graph_options = ['Counts', 'Costs']
    df = df_map.get(pathname, None)
    if df is None:
        return html.Div("Page not found")

    return html.Div([
        #html.Label('막대 차트 선택:'),
        dcc.Dropdown(
            id='bar-graph-dropdown',
            options=[{'label': option, 'value': option} for option in graph_options],
            value=graph_options[0],  # 기본 선택값 설정
            placeholder="Select",
        ),
        dcc.Loading(
            id="loading-bar",
            type="default",
            children=[html.Div(id='bar-chart-container')]
        ),
        dcc.Dropdown(
            id='pie-graph-dropdown',
            options=[{'label': option, 'value': option} for option in graph_options],
            value=graph_options[0],  # 기본 선택값 설정
            placeholder="Select",
        ),
        dcc.Loading(
            id="loading-pie",
            type="default",
            children=[html.Div(id='pie-chart-container')]
        ),
    ])

# area_detail_page.py에 추가된 함수
def generate_area_detail_page_callbacks(app, style_dic):
    @app.callback(Output('bar-chart-container', 'children'),
                  [Input('bar-graph-dropdown', 'value'),
                   Input("url", "pathname")])
    def update_bar_chart(selected_graph, pathname):
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_bar_chart(df, selected_graph, style_dic.bar_plot1_styl)

    @app.callback(Output('pie-chart-container', 'children'),
                  [Input('pie-graph-dropdown', 'value'),
                   Input("url", "pathname")])
    def update_pie_chart(selected_graph, pathname):
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_pie_chart(df, selected_graph, style_dic.pie_plot1_styl)