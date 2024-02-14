from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go

# def generate_mapbox2(df, geojson, selected_category, zoom, graph_style):
    
#     if selected_category == 'Counts':
#         # value_cnt 계산
#         df = df['city_s'].value_counts()
#         df = df.reset_index()
#         fig = px.choropleth_mapbox(df, geojson=geojson, color="count",
#                            locations="city_s", featureidkey="properties.ADM_NM",
#                            center={"lat": centroid_point.y, "lon": centroid_point.x},
#                            mapbox_style="carto-positron", zoom=zoom, opacity=0.7, labels={'count':'Counts'}) #carto-darkmatter

#     elif selected_category == 'Costs':
#         # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
#         cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
#         # 도시별 총액의 비율을 파이 차트로 시각화
#         fig = px.choropleth_mapbox(cost_sum_by_city, geojson=geojson, color=cost_sum_by_city.values,
#                     locations=cost_sum_by_city.index, featureidkey="properties.ADM_NM",
#                     center={"lat": centroid_point.y, "lon": centroid_point.x},
#                     color_continuous_scale="Gnbu_r", mapbox_style="carto-positron", zoom=zoom, opacity=0.7, labels={'color':'Costs'}) #carto-darkmatter
#     else:
#         # 빈 레이아웃 생성
#         fig = px.pie()
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
#     return html.Div([
#         dcc.Graph(
#         id='mapbox',
#         figure=fig,
#         config={'displayModeBar': False}  # Hide the modebar
#     ),
#     ], style=graph_style)

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