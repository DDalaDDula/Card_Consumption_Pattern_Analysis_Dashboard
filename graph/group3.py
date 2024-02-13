from dash import html, dcc
import plotly.express as px
import geopandas as gpd
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.geometry import Point

def generate_pie_chart1(df, selected_category, graph_style):
    if selected_category == 'Counts':
        fig = px.pie(
            df['city_s'].value_counts(),
            names=df['city_s'].value_counts().index,
            values=df['city_s'].value_counts().values,
            title='Ratio of Area payments',
            color_discrete_sequence=px.colors.cyclical.Twilight_r,  # 색상 설정
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
                    color_discrete_sequence=px.colors.cyclical.Edge,  # 색상 설정
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

def generate_mapbox1(df, geojson, selected_category, zoom, graph_style):
    union_polygon = unary_union([shape(feature['geometry']) for feature in geojson['features'] if feature['geometry']['type'] == 'Polygon'])
    centroid_point = union_polygon.centroid
    if selected_category == 'Counts':
        # value_cnt 계산
        df = df['city_s'].value_counts()
        df = df.reset_index()
        fig = px.choropleth_mapbox(df, geojson=geojson, color="count",
                           locations="city_s", featureidkey="properties.ADM_NM",
                           center={"lat": centroid_point.y, "lon": centroid_point.x},
                           mapbox_style="carto-positron", zoom=zoom, opacity=0.7, labels={'count':'Counts'}) #carto-darkmatter

    elif selected_category == 'Costs':
        # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
        cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
        # 도시별 총액의 비율을 파이 차트로 시각화
        fig = px.choropleth_mapbox(cost_sum_by_city, geojson=geojson, color=cost_sum_by_city.values,
                    locations=cost_sum_by_city.index, featureidkey="properties.ADM_NM",
                    center={"lat": centroid_point.y, "lon": centroid_point.x},
                    color_continuous_scale="Gnbu_r", mapbox_style="carto-positron", zoom=zoom, opacity=0.7, labels={'color':'Costs'}) #carto-darkmatter
    else:
        # 빈 레이아웃 생성
        fig = px.pie()
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return html.Div([
        dcc.Graph(
        id='mapbox',
        figure=fig,
        config={'displayModeBar': False}  # Hide the modebar
    ),
    ], style=graph_style)
