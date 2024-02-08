from dash import html, dcc
import plotly.express as px

def generate_bar_chart2(df, graph_style):
    # 바 차트 그리기 (Counts)
    fig = px.bar(
        x=df['데이터건수'],
        y=df['표준산업분류(중)'],
        color_continuous_scale='Agsunset',  # reverse 하고싶으면 "_r" 붙이기
    )

    # 레이아웃 업데이트
    fig.update_layout(
        xaxis_title='',
        xaxis=dict(
            title_font=dict(size=14),  # x축 제목의 폰트 크기를 설정합니다.
            side='top'  # x축을 위쪽에 배치합니다.
        ),
        yaxis_title='',
        title='Count of Standard Industry',
        margin=dict(t=100), 
        template='plotly_dark',  # 사용할 템플릿
        font=dict(
            family='Arial, sans-serif',  # 사용할 폰트 설정
            size=12,  # 폰트 크기 설정
        ),
    )

    fig.update_traces(marker_line_color= "grey", marker_line_width = 2)
    return html.Div([
        dcc.Graph(
            id='bar-chart2',
            figure=fig,
            config={'displayModeBar': False}  # Hide the modebar

        ),
    ], style=graph_style)