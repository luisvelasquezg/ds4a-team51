from gc import callbacks
import dash
from dash import html, dcc, dash_table, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

from components.dataframe import model_segmentos

page_name = 'Segmentación'
page_path = '/segmentacion'


# def get_name():
#     return page_name
    
# def get_path():
#     return page_path



# Prueba del gráfico
######################################################################
segmento_1 = ['Alto']
localidad_1 = ['LOS MARTIRES']
tipo_1 = ['PUBLICO']
datos_consultados = model_segmentos.consultar_datos_componentes(
        segmento = segmento_1, localidad = localidad_1, tipo = tipo_1
    )


fig_componentes_segmento = px.bar(datos_consultados, x = 'COMPONENTE', y = 'PROMEDIO',
                  color = 'COMPONENTE', #labels = {'TIPO': 'Tipo'},
                  # title = 'Cumplimiento General - Último Año (2019)'
                  title = f'Componentes ({segmento_1[0]},  {localidad_1[0]}, {tipo_1[0]}) - Último Año (2019)'
              )

fig_componentes_segmento.update_layout(yaxis_range=[0, 1])

######################################################################




layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            [
                html.H1([page_name], id="div_title_segmentacion"),
            ],
            style = {'textAlign': 'center'}
        )
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-componentes-segmento', figure = fig_componentes_segmento),
            # width=4
        ])
    ])
])


# @app.callback(
#     # Output(component_id, component_property),
#     Output('bar-componentes-segmento', 'figure'),
#     Input(),
#     Input(),
#     Input()
# )