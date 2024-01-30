from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go

def generate_pie_chart(df, selected_graph, graph_style):
    if selected_graph == 'Counts':
        fig = px.pie(
            df['city_s'].value_counts(),
            names=df['city_s'].value_counts().index,
            values=df['city_s'].value_counts().values,
            title='Administration Area Composition Ratio',
            color_discrete_sequence=px.colors.cyclical.IceFire,  # 색상 설정
            custom_data=[df['city_s'].value_counts().values],  # 추가 정보를 custom_data로 설정
            labels={'customdata': 'Count'},  # custom_data에 대한 레이블 설정
        )
        # 레이블을 숫자 옆에 표시
        fig.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])  # pull을 사용하여 일부 조각을 분리
        fig.update_layout(showlegend=False)

    elif selected_graph == 'Costs':
        # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
        cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
        # 도시별 총액의 비율을 파이 차트로 시각화
        fig = px.pie(cost_sum_by_city, 
                    names=cost_sum_by_city.index, 
                    values=cost_sum_by_city.values,
                    title='City Total Cost Ratio',  # 파이 차트 제목 설정
                    color_discrete_sequence=px.colors.cyclical.IceFire,  # 색상 설정
                    custom_data=[cost_sum_by_city.values],  # 추가 정보를 custom_data로 설정
                    labels={'customdata': 'Total Cost'},  # custom_data에 대한 레이블 설정
                    )
        # 레이블을 숫자 옆에 표시
        fig.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.1])  # pull을 사용하여 일부 조각을 분리
        fig.update_layout(showlegend=False)

    else:
        # 빈 레이아웃 생성
        fig = px.pie()

    return html.Div([
        dcc.Graph(
        id='pie-chart',
        figure=fig,
        config={'displayModeBar': False}  # Hide the modebar
    ),
    ], style=graph_style)
