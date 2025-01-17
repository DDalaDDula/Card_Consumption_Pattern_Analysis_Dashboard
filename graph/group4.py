from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go

def generate_pie_chart1(df, selected_category, graph_style):
    if selected_category == 'Counts':
        fig = px.pie(
            df['city_s'].value_counts(),
            names=df['city_s'].value_counts().index,
            values=df['city_s'].value_counts().values,
            title='Ratio of Area payments',
            color_discrete_sequence=px.colors.sequential.Agsunset_r,  # 색상 설정
            custom_data=[df['city_s'].value_counts().values],  # 추가 정보를 custom_data로 설정
            labels={'customdata': 'Count'},  # custom_data에 대한 레이블 설정
            hole=0.4
        )

    elif selected_category == 'Costs':
        # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
        cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
        # 도시별 총액의 비율을 파이 차트로 시각화
        fig = px.pie(cost_sum_by_city, 
                    names=cost_sum_by_city.index, 
                    values=cost_sum_by_city.values,
                    title='Ratio of Area Cost ',  # 파이 차트 제목 설정
                    color_discrete_sequence=px.colors.sequential.Agsunset,  # 색상 설정
                    custom_data=[cost_sum_by_city.values],  # 추가 정보를 custom_data로 설정
                    labels={'customdata': 'Total Cost'},  # custom_data에 대한 레이블 설정
                    hole=0.4
                    )

    else:
        # 빈 레이아웃 생성
        fig = px.pie()

    # Tooltip에 기타 항목에 대한 정보 추가
    fig.update_layout(showlegend=False, template='plotly_dark')
    fig.update_traces(textinfo='label+percent', pull=[0.05, 0.05, 0.05], marker_line_color= "grey", marker_line_width = 2)  # pull을 사용하여 상위 세 조각을 분리
    
    return html.Div([
        dcc.Graph(
        id='pie-chart',
        figure=fig,
        config={'displayModeBar': False}  # Hide the modebar
    ),
    ], style=graph_style)

def generate_bar_chart2(df, graph_style):
    # 바 차트 그리기 (Counts)
    fig = px.bar(
        x=df['데이터건수'],
        y=df['표준산업분류(중)'],
        color=df['데이터건수'],
        color_continuous_scale=px.colors.sequential.Agsunset,
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
        margin=dict(t=100, l=0), 
        template='plotly_dark',  # 사용할 템플릿
        font=dict(
            family='Arial, sans-serif',  # 사용할 폰트 설정
            size=12,  # 폰트 크기 설정
        ),
    )

    fig.update_traces(marker_line_color= "grey", marker_line_width = 2)
    fig.update_layout(coloraxis_showscale=False)
    return html.Div([
        dcc.Graph(
            id='bar-chart2',
            figure=fig,
            config={'displayModeBar': False}  # Hide the modebar

        ),
    ], style=graph_style)