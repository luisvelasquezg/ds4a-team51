from gc import callbacks
import dash
from dash import html, dcc, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# from app import app
from components.dataframe import model_segmentos
from components.sidebar import sidebar_segmentacion

page_name = 'Segmentación'
page_path = '/segmentacion'

suppress_callback_exceptions=False

# def get_name():
#     return page_name
    
# def get_path():
#     return page_path



# Prueba del gráfico
######################################################################
# segmento_1 = ['Medio']
# localidad_1 = ['LOS MARTIRES']
# tipo_1 = ['PRIVADO']
# datos_consultados, existen_datos = model_segmentos.consultar_datos_componentes(
#         segmento = segmento_1, localidad = localidad_1, tipo = tipo_1
#     )

# mensaje_consulta = ''
# if not existen_datos:
#     mensaje_consulta = '[NO SE ENCONTRARON DATOS]'

# fig_componentes_segmento = px.bar(datos_consultados, x = 'COMPONENTE', y = 'PROMEDIO',
#                 color = 'COMPONENTE', #labels = {'TIPO': 'Tipo'},
#                 # title = 'Cumplimiento General - Último Año (2019)'
#                 title = f'Componentes ({segmento_1[0]},  {localidad_1[0]}, {tipo_1[0]}) - Último Año (2019)'
#             )

# fig_componentes_segmento.update_layout(yaxis_range=[0, 1])

######################################################################




layout = html.Div([
    sidebar_segmentacion.layout,
    dbc.Container([
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
                html.P(
                    # mensaje_consulta,
                    id = 'seccion-mensaje',
                    style = {
                        'color': 'rgb(239,85,59)',
                        'textAlign': 'center',
                        'fontWeight': 'bold',
                        'fontFamily': 'Courier New'
                    }
                ),
                dcc.Graph(
                    id = 'bar-componentes-segmento',
                    # figure = fig_componentes_segmento
                ),
                # width=4
            ])
        ])
    ],
    className="ds4a-body-with-sidebar",
    )
])


####################################################################################
# Callbacks
####################################################################################
@callback(
    # Output(component_id, component_property),
    Output('bar-componentes-segmento', 'figure'),
    Output('seccion-mensaje', 'children'),
    Input('segmento-dropdown', 'value'),
    Input('localidad-dropdown', 'value'),
    Input('tipo-dropdown', 'value')
)
def actualizar_grafica_bar_componentes(segmento_seleccion, localidad_seleccion, tipo_seleccion):
    
    segmento_seleccion = list(segmento_seleccion)
    localidad_seleccion = list(localidad_seleccion)
    tipo_seleccion = list(tipo_seleccion)

    datos_consultados, existen_datos = model_segmentos.consultar_datos_componentes(
        segmento = segmento_seleccion,
        localidad = localidad_seleccion,
        tipo = tipo_seleccion
    )

    ultimo_annio = model_segmentos.annio_reciente

    mensaje_consulta = ''
    if not existen_datos:
        mensaje_consulta = '[NO SE ENCONTRARON DATOS]'

    fig_componentes_segmento = px.bar(datos_consultados, x = 'COMPONENTE', y = 'PROMEDIO',
                    color = 'COMPONENTE', #labels = {'TIPO': 'Tipo'},
                    # title = 'Cumplimiento General - Último Año (2019)'
                    title = f'Promedio Componentes - Último Año ({ultimo_annio})'
                )

    fig_componentes_segmento.update_layout(yaxis_range=[0, 1])

    return fig_componentes_segmento, mensaje_consulta
####################################################################################