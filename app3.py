#_*_coding:utf-8_*_
# Author MHU1SGH   
# Create Date: 9/3/2021
# Create Time  9:35 AM
# Product_name PyCharm

#_*_coding:utf-8_*_
# Author MHU1SGH
# Create Date: 9/3/2021
# Create Time  9:35 AM
# Product_name PyCharm




import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from apps import app

app = app
server = app.server

app_name = 'intelligent_interception_'

select_curve = pd.DataFrame(columns=['start_time', 'end_time', 'Curve_start'])

app.layout = html.Div([

            html.Div(
                [
                    html.Table([
                        html.Tr([
                            html.Td('开始时间',  ),
                            html.Td(dcc.Input(id=app_name + 'input1', value='eg: 2020/06/01 11:32:01')),
                            html.Td('结束时间', ),
                            html.Td(dcc.Input(id=app_name + 'input2', value='eg: 2020/06/01 11:32:01')),
                            html.Td('切分参考信号', ),
                            html.Td(dcc.Dropdown(id=app_name + 'select_measures1',
                                                 options=[
                                                     {'label': '扭矩', 'value': 'torque'},
                                                     {'label': '速度', 'value': 'speed'},
                                                     {'label': '位置', 'value': 'position'},
                                                 ],
                                                 value='torque',
                                                 ),style={'width': '20%'}
                                    ),

                            html.Td(html.Button('查询', id=app_name + 'range_query', n_clicks=0)),

                        ], ),

                    ], style={'width': '90%'}
                    ),
                ], style={'width': '90%',
                            'display': 'flex',
                            'flex-direction': 'row',
                            # 'align-items':' center',
                            'justify-content': 'space-between',}
            ),
            html.Div(
                [
                    html.Div([

                            dcc.Graph(id=app_name + 'figure',
                                      config={'displaylogo': False, }),
                            html.Table(
                                [
                                    html.Tr([
                                        html.Td('起始时刻点'),
                                        html.Td(dcc.Input(id=app_name + 'input3')),
                                        html.Td('终止时刻点'),
                                        html.Td(dcc.Input(id=app_name + 'input4')),
                                        html.Td(html.Button(["插入数据"], id=app_name + "insert_data", ))
                                    ]),
                                ],
                            ),


                        ],  style={'width': '60%'}
                    ),
                    html.Div([
                        html.Br(),
                        html.Table(
                            [
                                html.Tr([
                                    html.Td(html.Button('保存参考曲线', id='save_reference_curve', n_clicks=0)),
                                    html.Td(html.Div(id='save_status'))
                                ]),
                            ],
                        ),


                        html.Table([html.Tr([html.Td('待确认参考曲线列表'), ], style={'background-color': 'gray'})],
                                   style={'width': '100%'}),
                        dash_table.DataTable(
                            id=app_name + 'datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in
                                select_curve.columns
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
                    'justify-content': 'space-between',}
            ),
        ],
        )


if __name__ == '__main__':
    app.run_server(debug=True)