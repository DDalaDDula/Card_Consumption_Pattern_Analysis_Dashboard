from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go

def generate_basic_pie_chart1(df, graph_style):
    # 카드사에 대한 파이 차트
    fig = px.pie(df['company'].value_counts(), 
                    names=df['company'].value_counts().index, 
                    values=df['company'].value_counts().values,
                    title='Ratio of Card Company Composition',
                    color_discrete_sequence=px.colors.sequential.Agsunset,
                    hole=0.4)

    # Tooltip에 기타 항목에 대한 정보 추가
    fig.update_layout(showlegend=False, template='plotly_dark')
    fig.update_traces(textinfo='label+percent', pull=[0.05, 0.05, 0.05], marker_line_color= "grey", marker_line_width = 1)  # pull을 사용하여 상위 세 조각을 분리
    
    return html.Div([
        dcc.Graph(
            id='pie-chart-company',
            figure=fig,
            config={'displayModeBar': False},
        ),
    ], style=graph_style)

def generate_basic_pie_chart2(df, selected_chart, graph_style):
    if selected_chart == 'Sex':
        # 성별에 대한 파이 차트
        fig = px.pie(df['sex'].value_counts(), 
                     names=df['sex'].value_counts().index, 
                     values=df['sex'].value_counts().values,
                     title='Ratio of Gender Composition',
                     color_discrete_sequence=px.colors.sequential.Agsunset_r,
                     hole=0.4)
    elif selected_chart == 'Age':
        # 연령대에 대한 파이 차트
        fig = px.pie(df['age'].value_counts(), 
                     names=df['age'].value_counts().index, 
                     values=df['age'].value_counts().values,
                     title='Ratio of Age Group Composition ',
                     color_discrete_sequence=px.colors.cyclical.Twilight,
                     hole=0.4)
    else:
        # 빈 레이아웃 생성
        fig = px.pie()

    # Tooltip에 기타 항목에 대한 정보 추가
    fig.update_layout(showlegend=False, template='plotly_dark')
    fig.update_traces(textinfo='label+percent', pull=[0.05, 0.05, 0.05], marker_line_color= "grey", marker_line_width = 1)  # pull을 사용하여 상위 세 조각을 분리
    
    return html.Div([
        dcc.Graph(
            id='pie-chart-sex-age',
            figure=fig,
            config={'displayModeBar': False},
        ),
    ], style=graph_style)