from dash import html, dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from assets import style_dic

def create_sidebar(app):
    return html.Div(
        [
            html.H1("📋Dashboard", id="dashboard-heading"),
            html.P(
                "📈Card Consumption\nPattern Analysis", className="lead", id="dashboard-description"
            ),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("데이터 개요", href="/sum", active="exact", style=style_dic.navlink_style),
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
    
    # 대시보드 제목과 설명을 클릭하면 홈화면으로 넘어갈 수 있는 콜백함수
    @app.callback(Output("url", "pathname"), [Input("dashboard-heading", "n_clicks"), Input("dashboard-description", "n_clicks")])
    def go_to_homepage(click_heading, click_description):
        if click_heading or click_description:
            return "/"
        return dash.no_update
    
    return navbar

    