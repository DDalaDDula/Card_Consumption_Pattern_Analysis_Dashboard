from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import json
from graph.group1 import *
from graph.group2 import *
from graph.group3 import *
from graph.group4 import *

# MAPBOX_API_KEY = "pk.eyJ1IjoiZGRhbGFkZHVsYSIsImEiOiJjbHNsMDIxMTIwNHk1MmttemI1azlhdTd1In0.Zr3dn9eBHjGgV0AQwjfEBw"

# dataset & dictionary
jg_df = pd.read_csv("dataset/jg_df.csv")
ddc_df = pd.read_csv("dataset/ddc_df.csv")
nj_df = pd.read_csv("dataset/nj_df.csv")

jg_std = pd.read_csv("dataset/jg_std.csv")
ddc_std = pd.read_csv("dataset/ddc_std.csv")
nj_std = pd.read_csv("dataset/nj_std.csv")

jg_geo = json.load(open('dataset/jg.geojson', 'r', encoding="UTF8"))
ddc_geo = json.load(open('dataset/ddc.geojson', 'r', encoding="UTF8"))
nj_geo = json.load(open('dataset/nj.geojson', 'r', encoding="UTF8"))

df_map = {"/jg":jg_df, "/ddc":ddc_df, "/nj":nj_df} #"/sum":jg_df, 
std_map = {"/jg":jg_std, "/ddc":ddc_std, "/nj":nj_std}
geo_map = {"/jg":jg_geo, "/ddc":ddc_geo, "/nj":nj_geo}
zoom_map = {"/jg":12, "/ddc":10.5, "/nj":9.5}
title_map = {"/jg":"서울특별시(중구)", "/ddc":"경기도(동두천시)", "/nj":"전라남도(나주시)"} #"/sum":jg_df, 

def area_detail_page(pathname):
    # Dropdown에 들어갈 옵션 리스트 생성
    category_options1 = ['Counts', 'Costs']
    category_options2 = ['Sex', 'Age']
    df = df_map.get(pathname, None)
    if df is None:
        return html.Div("Page not found")

    return html.Div([
            html.H1(f"🏙️{title_map[pathname]}", id="page-title"),
            html.Hr(),
        html.Div([
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='pie-chart-basic-container1')]
            ),
            dcc.Dropdown(
                id='pie-graph-dropdown2',
                options=[{'label': option, 'value': option} for option in category_options2],
                value=category_options2[0],  # 기본 선택값 설정
                placeholder="Select",
            ),
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='pie-chart-basic-container2')]
            ),
        ], id="group1"),
        
        html.Div([
            dcc.Dropdown(
                id='bar-graph-dropdown',
                options=[{'label': option, 'value': option} for option in category_options1],
                value=category_options1[0],  # 기본 선택값 설정
                placeholder="Select",
            ),
            dcc.Loading(
                id="loading-bar",
                type="circle",
                children=[html.Div(id='bar-chart-container1')]
            ),
        ], id="group2"),
        
        html.Div([
            dcc.Dropdown(
                id='mapbox-dropdown1',
                options=[{'label': option, 'value': option} for option in category_options1],
                value=category_options1[0],  # 기본 선택값 설정
                placeholder="Select",
            ),
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='mapbox-container1')]
            ),
            dcc.Dropdown(
                id='mapbox-dropdown2',
                options=[{'label': option, 'value': option} for option in category_options1],
                value=category_options1[0],  # 기본 선택값 설정
                placeholder="Select",
            ),
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='mapbox-container2')]
            ),
        ], id="group3"),
        
        html.Div([
            dcc.Dropdown(
                id='pie-graph-dropdown1',
                options=[{'label': option, 'value': option} for option in category_options1],
                value=category_options1[0],  # 기본 선택값 설정
                placeholder="Select",
            ),
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='pie-chart-container1')]
            ),
            dcc.Loading(
                id="loading-pie",
                type="circle",
                children=[html.Div(id='bar-chart-container2')]
            ),
        ], id="group4")
    ], id="area_detail_page")

# area_detail_page.py에 추가된 함수
def generate_area_detail_page_callbacks(app, style_dic):
    @app.callback(Output('pie-chart-basic-container1', 'children'), 
                  [Input("url", "pathname")])
    def update_pie_chart_company(pathname):  # 새로운 파이 차트 함수로 변경
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_basic_pie_chart1(df, style_dic.pie_plot1_styl)  # 새로운 파이 차트 호출

    @app.callback(Output('pie-chart-basic-container2', 'children'), 
                  [Input('pie-graph-dropdown2', 'value'),  # 새로운 드롭다운 추가
                   Input("url", "pathname")])
    def update_pie_chart_sex_age(selected_chart, pathname):  # 새로운 파이 차트 함수로 변경
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_basic_pie_chart2(df, selected_chart, style_dic.pie_plot1_styl)  # 새로운 파이 차트 호출

    @app.callback(Output('bar-chart-container1', 'children'),
                  [Input('bar-graph-dropdown', 'value'),
                   Input("url", "pathname")])
    def update_bar_chart1(selected_category, pathname):
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_bar_chart1(df, selected_category, style_dic.bar_plot1_styl)

    @app.callback(Output('mapbox-container1', 'children'),
                  [Input('mapbox-dropdown1', 'value'),
                   Input("url", "pathname")])
    def update_mapbox1(selected_category, pathname):
        df = df_map.get(pathname, None)
        geojson = geo_map.get(pathname, None)
        zoom = zoom_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_mapbox1(df, geojson, selected_category, zoom, style_dic.mapbox_styl)

    @app.callback(Output('mapbox-container2', 'children'),
                  [Input('mapbox-dropdown2', 'value'),
                   Input("url", "pathname")])
    def update_mapbox2(selected_category, pathname):
        df = df_map.get(pathname, None)
        geojson = geo_map.get(pathname, None)
        zoom = zoom_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_mapbox2(df, geojson, selected_category, zoom)

    @app.callback(Output('pie-chart-container1', 'children'),
                  [Input('pie-graph-dropdown1', 'value'),
                   Input("url", "pathname")])
    def update_pie_chart(selected_category, pathname):
        df = df_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_pie_chart1(df, selected_category, style_dic.pie_plot1_styl)

    @app.callback(Output('bar-chart-container2', 'children'),
                  [Input("url", "pathname")])
    def update_bar_chart2(pathname):
        df = std_map.get(pathname, None)
        if df is None:
            return html.Div("페이지를 찾을 수 없습니다.")
        return generate_bar_chart2(df, style_dic.bar_plot2_styl)