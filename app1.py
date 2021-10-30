#_*_coding:utf-8_*_
# Author MHU1SGH   
# Create Date: 9/3/2021 
# Create Time  9:35 AM 
# Product_name PyCharm


import dash_core_components as dcc
import dash_html_components as html

from apps import app
app = app
server = app.server

app_name = 'realtime_process_curve_'

app.layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.Label('监控指标（Y轴）'),
                dcc.Dropdown(
                id=app_name+"dropdown1",
                options=[
                    {'label': '扭矩', 'value': 'torque'},
                    {'label': '位置', 'value': 'position'},
                    {'label': '速度', 'value': 'speed'},

                ],
                value='torque'
                )],style = {
                'width': '15%',
                'display': 'inline-block'
            }),

            html.Div([
                html.Label('参照指标（X轴）'),
                dcc.Dropdown(
                id=app_name+"dropdown2",
                options=[
                    {'label': '时间', 'value': 'time'},
                ],
                value = 'time'
                ),], style={
                'width': '15%',
                'display': 'inline-block'
            }),
            #
            html.Div([
                html.Label('对比曲线数目'),
                dcc.Dropdown(
                id=app_name+"dropdown3",
                options=[
                    {'label': '1', 'value': 1},
                    {'label': '2', 'value': 2},
                    {'label': '3', 'value': 3},
                    {'label': '4', 'value': 4},
                    {'label': '5', 'value': 5},
                    {'label': '6', 'value': 6}
                ],
                    value=2,

                ),], style={
                'width': '15%',
                'display': 'inline-block'
            }),
            # html.Label('更新频率'),
            html.Div([
                html.Label('更新频率'),
                dcc.Dropdown(
                id=app_name+"dropdown4",
                options=[
                    {'label': '1s', 'value': 1},
                    {'label': '2s', 'value': 2},
                    {'label': '3s', 'value': 3},
                    {'label': '4s', 'value': 4},
                    {'label': '5s', 'value': 5},
                ],
                value = 1
                ),], style={
                'width': '15%',
                'display': 'inline-block',
            }),

            html.Div(
                html.Button("触发更新", id=app_name+'click', style={'background-color':'#6495ed'}),
                style={
                'width': '15%',
                'display': 'inline',
                }

            )

            ],
            style={
                  'height': 'fit-content',
                  # 'background-color': '#1e2130',
                  'display': 'flex',
                  'flex-direction': 'row',
                  'align-items':' center',
                  'justify-content': 'space-between',
                  # border-bottom: 1px solid #4B5460;
                  # padding: 1rem 10rem;
                  'width':'100%',                }
        )
    ]),
    html.Div([
        html.Div([
            html.H4(['实时过程曲线'], style={'text-align': 'center'}),
            dcc.Graph(
                id = app_name+ 'figure1',
                config={'displaylogo': False}
            ),],
            style={'width':'48%'}
                ),
        html.Div([
            html.H4(['多周期对比图'], style={'text-align': 'center'}),
            dcc.Graph(
                id= app_name+'figure2',
                config={'displaylogo': False}
                    ),
                ],
            style={'width':'48%'}
                ),

                ],
        style={
            'height': 'fit-content',
              # 'background-color': '#1e2130',
              'display': 'flex',
              'flex-direction': 'row',
              'align-items':' center',
              'justify-content': 'space-between',
              # border-bottom: 1px solid #4B5460;
              # padding: 1rem 10rem;
              'width':'100%',              }
            ),



])



if __name__ == '__main__':
    app.run_server(debug=True)