import dash
from dash import html

def layout(style_dic):
    return html.Div(
        [
            html.H1("Summary Page", id="summary-heading"),
            # Summary 페이지의 내용을 추가하면 됩니다.
            html.P("This is the summary page content.", className="lead", id="summary-description"),
            # 추가적으로 필요한 HTML 또는 Dash 컴포넌트를 여기에 넣으세요.
        ],
        style=style_dic.page_style,
    )

def generate_callbacks(app, style_dic):
    # 추가적인 callback 함수가 필요한 경우 여기에 정의하세요.
    pass
