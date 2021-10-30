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

app_name = 'app2_'
app.layout = html.Div([
    # html.H3('过程曲线切分'),
    html.Div([
        html.Div([
            # html.Label('监控指标'),
            html.Div(
                [html.H4('切分策略',style={'text-align': 'center'}),
                 html.Br(),
                 html.Br(),
                 html.Br(),
                 html.Table(
                     [
                         html.Tr([

                             html.Td(dcc.Checklist(
                     id=app_name + "checklist1",
                     options=[
                         {"label": "基于信号切分", "value": "solid"},

                     ],
                 ))
                         ]),
                         html.Tr([

                             html.Td(dcc.Checklist(
                                 id=app_name + "checklist2",
                                 options=[

                                     {"label": "智能曲线切分", "value": "U"},

                                 ],
                             ))
                         ]),
                         html.Tr([

                             html.Td(dcc.Checklist(
                                 id=app_name + "checklist3",
                                 options=[

                                     {"label": "混合模式", "value": "p"},
                                 ],
                             ))
                         ]),
                     ],style={'margin': 'auto',}
                 ),

                 ],
                style = {
                'width': '30%',
                'height': '400px',
                # 'padding': '30px 0',
                # 'padding': '100px 0',
                # 'position': 'relative',
                'border-style':'solid',
                'border-color':'#98bf21',
                # 'background-color': '#b0c4de',
                'display': 'inline-block'
            }),

            html.Div(
                [html.H4('信号数据源', style={'text-align': 'center'}),
                 html.Br(),
                 html.Br(),
                 html.Br(),
                html.Table(
                        [
                            html.Tr([
                                html.Td('开始信号'),
                                html.Td(dcc.Input(id='input1'))
                            ]),
                        ], style={'margin': 'auto',}
                    ),
                 html.Table(
                     [
                         html.Tr([
                             html.Td('结束信号'),
                             html.Td(dcc.Input(id='input2'))
                         ]),
                         html.Tr([
                             html.Td('延迟'),
                             html.Td(dcc.Input(id='input3'))
                         ]),
                     ], style={'margin': 'auto', }
                 ),




            ],
                style={
                    'width': '65%',
                    'height': '400px',

                    # 'padding': '30px 0',
                    # 'padding': '100px 0',
                    # 'position': 'relative',
                    'border-style': 'solid',
                    'border-color': '#98bf21',
                    # 'background-color': '#b0c4de',
                    'display': 'inline-block'
                }
        )
    ],style={
                'display': 'flex',
                'flex-direction': 'row',
                # 'align-items':' center',
                'justify-content': 'space-between',
            }),


])])


if __name__ == '__main__':
    app.run_server(debug=True)


