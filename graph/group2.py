from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go

def generate_bar_chart1(df, selected_graph, graph_style):
    if selected_graph == 'Counts':
        # value_cnt 계산
        value_cnt = df['city_s'].value_counts()
        # 바 차트 그리기 (Counts)
        fig = px.bar(
            x=value_cnt.index,
            y=value_cnt.values,
            color=value_cnt.values,
            color_continuous_scale='agsunset',  # reverse 하고싶으면 "_r" 붙이기
            labels={'x': 'Area', 'y': 'Counts(K)', 'color': 'Counts'},
        )
    elif selected_graph == 'Costs':
        # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
        cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
        # 바 차트 그리기 (Costs)
        fig = px.bar(
            x=cost_sum_by_city.index,
            y=cost_sum_by_city.values,
            color=cost_sum_by_city.values,
            color_continuous_scale='gnbu_r',  # reverse 하고싶으면 "_r" 붙이기
            labels={'x': 'Area', 'y': 'Costs(B)', 'color': 'Costs'},
        )
    else:
        # 빈 레이아웃 생성
        fig = go.Figure()

    # 레이아웃 업데이트
    fig.update_layout(
        xaxis_title='Area',
        yaxis_title='Counts' if selected_graph == 'Counts' else 'Costs',
        title='Count of area payments' if selected_graph == 'Counts' else 'Total cost of area payments',
        margin=dict(t=90),  # 그래프 상단 margin 조절
        barmode='group',
        template='plotly_dark',  # 사용할 템플릿
        font=dict(
            family='Arial, sans-serif',  # 사용할 폰트 설정
            size=12,  # 폰트 크기 설정
        ),
    )

    fig.update_traces(marker_line_color= "grey", marker_line_width = 2)
    return html.Div([
        dcc.Graph(
            id='bar-chart1',
            figure=fig,
            config={'displayModeBar': False}  # Hide the modebar
        ),
    ], style=graph_style)