from dash import html, dcc
import plotly.express as px

def graph1(df):
    # value_cnt 계산
    value_cnt = df['city_s'].value_counts()
    # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
    cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)

    # 바 차트 그리기
    fig1 = px.bar(
        x=value_cnt.index,
        y=value_cnt.values,
        color=value_cnt.values,
        color_continuous_scale='agsunset', # reverse 하고싶으면 "_r" 붙이기
        labels={'x': 'Area', 'y': 'Counts', 'color': 'Counts'},
    )
    # 바 차트 그리기
    fig2 = px.bar(
        x=cost_sum_by_city.index,
        y=cost_sum_by_city.values,
        color=cost_sum_by_city.values,
        color_continuous_scale='gnbu', # reverse 하고싶으면 "_r" 붙이기
        labels={'x': 'Area', 'y': 'Costs', 'color': 'Costs'},
    )

    # 레이아웃 업데이트
    fig1.update_layout(
        xaxis_title='Area',
        yaxis_title='Counts',
        width=1200,  # 그래프의 너비
        height=400,  # 그래프의 높이
        template='plotly_dark',  # 사용할 템플릿
        font=dict(
        family='Arial, sans-serif',  # 사용할 폰트 설정
        size=14,  # 폰트 크기 설정
        )
    )
    # 레이아웃 업데이트
    fig2.update_layout(
        xaxis_title='Area',
        yaxis_title='Counts',
        width=1200,  # 그래프의 너비
        height=400,  # 그래프의 높이
        template='plotly_dark',  # 사용할 템플릿
        font=dict(
        family='Arial, sans-serif',  # 사용할 폰트 설정
        size=14,  # 폰트 크기 설정
        )
    )
    return html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=fig1,
            config={'displayModeBar': False}  # Hide the modebar
        ),
        dcc.Graph(
            id='bar-chart',
            figure=fig2,
            config={'displayModeBar': False}  # Hide the modebar
        ),
    ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'})
