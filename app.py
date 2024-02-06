import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from readme import * # readme page import
from sidebar import * # navbar module import
from summary_page import * # summary page module import
from area_detail_page import * # detail page module import

from assets import style_dic # 딕셔너리 형태의 style지정파일(python file)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True # 콜백함수 예외 무시

sidebar = create_sidebar(app)  # sidebar 모듈 호출
content = html.Div(id="page-content", style=style_dic.CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url", refresh=False), sidebar, content], style=style_dic.layout_style)

# summary_page 모듈에서 추가된 부분
# generate_summary_callbacks(app, style_dic)
# area_detail_page 모듈에서 추가된 부분
generate_area_detail_page_callbacks(app, style_dic)

# Nav bar 선택에 따라 페이지 업데이트하는 콜백 함수
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/sum":
        return area_detail_page(pathname)
    
    elif pathname in ["/jg", "/ddc", "/nj"]:
        return area_detail_page(pathname)
    
    return markdown_to_html("README.md", style_dic) # basic page setting(readme)

if __name__ == "__main__":
    app.run_server(debug=True)
