import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# from app import app
from components.dataframe import model_segmentos
from components.sidebar import sidebar_segmentacion

page_name = 'Segmentación'
page_path = '/segmentacion'

suppress_callback_exceptions=False



####################################################################################
#   Variables
####################################################################################
tabla_segmentos = model_segmentos.generar_tabla_segmentos()
####################################################################################



####################################################################################
#   Layout
####################################################################################
layout = html.Div([
    sidebar_segmentacion.layout,
    dbc.Container([
        dbc.Row(
            dbc.Col(
                [
                    html.H3([page_name], id="div_title_segmentacion"),
                ],
                style = {'textAlign': 'center'}
            )
        ),
        dbc.Row([
            dbc.Col([
                html.P(
                    # Mensaje sobre la consulta
                    id = 'seccion-mensaje-segmentacion',
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
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                tabla_segmentos.display()
            ])
        ])
    ],
    className="ds4a-body-with-sidebar",
    )
])
####################################################################################



####################################################################################
# Callbacks
####################################################################################
@callback(
    # Output(component_id, component_property),
    Output('bar-componentes-segmento', 'figure'),
    Output('seccion-mensaje-segmentacion', 'children'),
    Input('segmento-dropdown', 'value'),
    Input('localidad-dropdown', 'value'),
    Input('tipo-dropdown', 'value')
)
def actualizar_grafica_bar_componentes(segmento_seleccion, localidad_seleccion, tipo_seleccion):
# def actualizar_grafica_bar_componentes(segmento_seleccion, localidad_seleccion):
    
    segmento_seleccion = [segmento_seleccion]
    localidad_seleccion = [localidad_seleccion]
    tipo_seleccion = [tipo_seleccion]

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
                    title = f'Promedio por Componentes - Último Año ({ultimo_annio})'
                )

    fig_componentes_segmento.update_layout(yaxis_range=[0, 1])

    return fig_componentes_segmento, mensaje_consulta

    # mi_mensaje = f'{segmento_seleccion} {type(segmento_seleccion)} \
    #                {localidad_seleccion} {tipo_seleccion}'
    # return mi_mensaje
####################################################################################