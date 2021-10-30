#_*_coding:utf-8_*_
# Author MHU1SGH   
# Create Date: 9/3/2021
# Create Time  9:35 AM
# Product_name PyCharm

import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

import pandas as pd

import dash_table
from apps import app


app = app
server = app.server


app_name = 'label_'


select_curve = pd.DataFrame(columns=['DMC','start_time', 'end_time', 'Failure_mode'])



app.layout = html.Div([
                html.Div(
                [
                    html.Table([
                        html.Tr([
                            html.Td('开始时间', ),
                            html.Td(dcc.Input(id=app_name + 'input1', value='eg: 2020/06/01 11:32:01')),
                            html.Td('结束时间', ),
                            html.Td(dcc.Input(id=app_name + 'input2', value='eg: 2020/06/01 11:32:01')),
                            html.Td('监控指标', ),
                            html.Td(dcc.Dropdown(id=app_name + 'dropdown1',
                                                 options=[
                                                     {'label': '扭矩-时间', 'value': 'torque'},
                                                     {'label': '角度-时间', 'value': 'angle'},
                                                 ],

                                                 value='time'
                                                 ), style = {'width': '15%'}),
                            html.Td('显示曲线数目', ),
                            html.Td(daq.NumericInput(id=app_name+'daq', value=3 )),

                            html.Td(html.Button('查询', id=app_name + 'query1', n_clicks=0)),
                        ], ),

                    ], style={'width': '95%'}
                    ),
                ], style={'width': '95%',
                          'display': 'flex',
                          'flex-direction': 'row',
                          # 'align-items':' center',
                          'justify-content': 'space-between', }
                ),
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(id='label_figure',
                                  config={'displaylogo': False, }),
                        # html.Pre(id='relayout-data',),
                        html.Table(
                            [
                                html.Tr([
                                    html.Td('标记起点', style={'width': '15%'}),
                                    html.Td(dcc.Input(id='label_input3')),
                                    html.Td('标记终点', style={'width': '15%'}),
                                    html.Td(dcc.Input(id='label_input4')),

                                ]),

                            ], style={'width': '90%'}
                        ),
                        html.Table(
                            [

                                html.Tr([

                                    html.Td('异常类型', style={'width': '15%'}),
                                    html.Td(dcc.Dropdown(id=app_name + 'dropdown2',
                                                         options=[
                                                             {'label': '失效1', 'value': 1},
                                                             {'label': '失效2', 'value': 2},
                                                             {'label': '失效3', 'value': 3}, ]

                                                         )),
                                    html.Td(html.Button('添加到样本集', id=app_name + 'query2', n_clicks=0)),
                                ], style={'width': '90%'}),

                            ], style={'width': '90%'}
                        ),
                    ],
                    )
                ], style={'width': '60%'}
                ),
                html.Div([
                    html.Br(),
                    html.Br(),

                    html.Table([html.Tr([html.Td('  失效样本集'), ], style={'background-color': 'gray'})],
                               style={'width': '100%'}),
                    dash_table.DataTable(
                        id='label_datatable-interactivity',
                        columns=[
                            {"name": i, "id": i, "deletable": True, "selectable": True} for i in select_curve.columns
                        ],
                        # data=df.to_dict('records'),
                        editable=True,
                        filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        column_selectable="single",
                        row_selectable="multi",
                        row_deletable=True,
                        selected_columns=[],
                        selected_rows=[],
                        page_action="native",
                        page_current=0,
                        page_size=10,
                    ),
                ], style={'width': '40%'}),

            ], style={
                'display': 'flex',
                'flex-direction': 'row',
                # 'align-items':' center',
                'justify-content': 'space-between',
            }),



        ],
        )

if __name__ == '__main__':
    app.run_server(debug=True)