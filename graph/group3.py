from dash import html, dcc
import plotly.express as px
import pandas as pd
from shapely.geometry import shape
from shapely.ops import unary_union
import pydeck as pdk
import dash_deck

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
                            color_continuous_scale="Agsunset", mapbox_style="carto-positron", zoom=zoom, opacity=0.9, labels={'count':'Counts'}) #carto-darkmatter

    elif selected_category == 'Costs':
        # 'city_s' 컬럼 값에 따른 'cost'의 합 계산
        cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
        # 도시별 총액의 비율을 파이 차트로 시각화
        fig = px.choropleth_mapbox(cost_sum_by_city, geojson=geojson, color=cost_sum_by_city.values,
                    locations=cost_sum_by_city.index, featureidkey="properties.ADM_NM",
                    center={"lat": centroid_point.y, "lon": centroid_point.x},
                    color_continuous_scale="Gnbu_r", mapbox_style="carto-positron", zoom=zoom, opacity=0.9, labels={'color':'Costs'}) #carto-darkmatter
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

def generate_mapbox2(df, geojson, selected_category, zoom):
    MAPBOX_API_KEY = "pk.eyJ1IjoiZGRhbGFkZHVsYSIsImEiOiJjbHNtcXp3ZDcwcWx6MmpyMHVkbnhoMHduIn0.2AYgy1ZaalPZO_rQUTBZiA"
    union_polygon = unary_union([shape(feature['geometry']) for feature in geojson['features'] if feature['geometry']['type'] == 'Polygon'])
    centroid_point = union_polygon.centroid
    
    gdf = pd.json_normalize(geojson['features'])
    
    # 행정동 - Counts dict생성
    count_dic = dict(zip(df['city_s'].value_counts().index, df['city_s'].value_counts().values))
    # 행정동 - Costs dict생성
    cost_sum_by_city = df.groupby('city_s')['cost'].sum().sort_values(ascending=False)
    cost_dic = dict(zip(cost_sum_by_city.index, cost_sum_by_city.values))
    
    gdf['city_s'] = gdf['properties.ADM_NM'].copy()
    gdf['Counts'] = gdf['city_s'].map(count_dic)
    gdf['Costs'] = gdf['city_s'].map(cost_dic)
    gdf['Scaling_Counts'] = (gdf['Counts'] - gdf['Counts'].min()) / (gdf['Counts'].max() - gdf['Counts'].min())
    gdf['Scaling_Costs'] = (gdf['Costs'] - gdf['Costs'].min()) / (gdf['Costs'].max() - gdf['Costs'].min())
    gdf = gdf.rename(columns={'geometry.coordinates':'coordinates'})

    # Agsunset_r 색상 팔레트
    color_palette = px.colors.sequential.Agsunset_r if selected_category == 'Counts' else px.colors.sequential.Gnbu_r
    # Make layer
    layer = pdk.Layer(
        'PolygonLayer', # 사용할 Layer 타입
        gdf, # 시각화에 쓰일 데이터프레임
        get_polygon='coordinates', # geometry 정보를 담고있는 컬럼 이름
        get_fill_color='[255*Scaling_Counts, 0, 0]' if selected_category == 'Counts' else '[0, 0, 255*Scaling_Counts]',
        extruded = True,
        get_elevation = 'Scaling_Counts' if selected_category == 'Counts' else 'Scaling_Costs',
        elevation_scale = 2000 if zoom == 12 else 3000 if zoom == 10.5 else 5000,
        opacity=0.8,
        pickable=True, # 지도와 interactive 한 동작 on
        auto_highlight=True # 마우스 오버(hover) 시 박스 출력
    )
    # Add sunlight shadow to the polygons
    sunlight = {
        "@@type": "_SunLight",
        "timestamp": 1707895936,
        "color": [255, 255, 255],
        "intensity": 1.0,
        "_shadow": True,
    }
    ambient_light = {"@@type": "AmbientLight", "color": [255, 255, 255], "intensity": 1.0}
    lighting_effect = {
        "@@type": "LightingEffect",
        "shadowColor": [0, 0, 0, 0.5],
        "ambientLight": ambient_light,
        "directionalLights": [sunlight],
    }

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=centroid_point.x,
        latitude=centroid_point.y,
        bearing=0,
        pitch=45,
        zoom=zoom)

    if selected_category == 'Counts':
        tooltip = {"html": "<b>Area:</b> {city_s} <br /><b>Counts:</b> {Counts}"}
    else: # Costs
        tooltip = {"html": "<b>Area:</b> {city_s} <br /><b>Counts:</b> {Costs}"}

    r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style=pdk.map_styles.LIGHT, effects=[lighting_effect], tooltip=tooltip)
    deck_component = dash_deck.DeckGL(r.to_json(), id="deck-gl", mapboxKey=MAPBOX_API_KEY, enableEvents=True)
    return deck_component