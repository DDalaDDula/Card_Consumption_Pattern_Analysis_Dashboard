from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash
from assets import style_dic

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

def create_sidebar(app):
    return html.Div(
        [
            dcc.Link(html.H1("📋Dashboard", id="dashboard-heading"), href="/", style={"textDecoration": "none", "color": "inherit"}),
            dcc.Link(html.P("📈Card Consumption\nPattern Analysis", className="lead", id="dashboard-description"), href="/", style={"textDecoration": "none", "color": "inherit"}),
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