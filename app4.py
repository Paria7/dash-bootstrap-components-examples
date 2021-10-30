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

select_curve = pd.DataFrame(columns=['start_time', 'end_time', 'Curve_start'])


# %%
app.layout = html.Div([


            html.Div([
                html.Br(),
                html.Br(),
                html.Button('更新数据', id='reference_curve_update', n_clicks=0),
                html.Table([html.Tr([html.Td('待确认参考曲线列表'), ], style={ 'background-color':'gray'})], style={'width':'100%'}),
                dash_table.DataTable(
                        id='reference_datatable-interactivity',
                        columns=[
                            {"name": i, "id": i, "deletable": True, "selectable": True} for i in select_curve.columns
                        ],
                        # data=data.to_dict('records'),
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
                        page_current= 0,
                        page_size= 10,
                    ),
            ], style={'width':'50%'}),
            html.Div([
                dcc.Graph(id='reference_curve_figure')

            ], style={'width': '50%'}
            ),

        ],style={
                'display': 'flex',
                'flex-direction': 'row',
                # 'align-items':' center',
                'justify-content': 'space-between',
            }
        )


if __name__ == '__main__':
    app.run_server(debug=True)