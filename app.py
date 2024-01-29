import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import markdown2
from sidebar import create_sidebar # navbar module import
from area_detail_page import area_detail_page, generate_area_detail_page_callbacks # detail page module import
from assets import style_dic # 딕셔너리 형태의 style지정파일(python file)

# card dataset & dictionary
jg_df = pd.read_csv("jg_df.csv")
ddc_df = pd.read_csv("ddc_df.csv")
nj_df = pd.read_csv("nj_df.csv")
df_map = {"/sum":jg_df, "/jg":jg_df, "/ddc":ddc_df, "/nj":nj_df}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True # 콜백함수 예외 무시

sidebar = create_sidebar(app) # sidebar 모듈 호출
content = html.Div(id="page-content", style=style_dic.CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style=style_dic.layout_style)
    
# Markdown to HTML function
def markdown_to_html(markdown_url):
    # Read README file
    readme_content = open(markdown_url, "r", encoding="utf-8").read()
    return dcc.Markdown(children=readme_content, style=style_dic.readme_style)

# area_detail_page 모듈에서 추가된 부분
generate_area_detail_page_callbacks(app)

# Nav bar 선택에 따라 페이지 업데이트하는 콜백 함수
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/sum":
        return area_detail_page(pathname, df_map)
    elif pathname in ["/jg", "/ddc", "/nj"]:
        return area_detail_page(pathname, df_map)
    # basic page setting(readme)
    return markdown_to_html("README.md")

if __name__ == "__main__":
    app.run_server(debug=True)
