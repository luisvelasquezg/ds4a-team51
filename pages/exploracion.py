import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

from components.dataframe import model_jardines
from components.sidebar import sidebar_exploracion


page_name = 'Exploración'
page_path = '/exploracion'

suppress_callback_exceptions=False


####################################################################################
#   Layout
####################################################################################

# # layout = html.Div([
# #     sidebar_exploracion.layout
# ])


layout = html.Div([
    sidebar_exploracion.layout,
    dbc.Container([
        dbc.Row(
            dbc.Col(
                [
                    html.H3([page_name], id="div_title_exploracion"),
                ],
                style = {'textAlign': 'center'}
            )
        ),
        dbc.Row([
            dbc.Col([
                html.P(
                    # Mensaje sobre la consulta 
                    id = 'seccion-mensaje-exploracion',
                    style = {
                        'color': 'rgb(239,85,59)',
                        'textAlign': 'center',
                        'fontWeight': 'bold',
                        'fontFamily': 'Courier New'
                    }
                ),
                dcc.Graph(
                    id = 'line-exploracion',
                    # figure = fig_componentes_segmento
                ),
                # width=4
            ]),
        ]),
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
    Output('line-exploracion', 'figure'),
    Output('seccion-mensaje-exploracion', 'children'),
    Input('cumplimiento-exploracion-dropdown', 'value'),
    Input('localidad-exploracion-dropdown', 'value'),
    Input('annio-exploracion-dropdown', 'value'),
    Input('tipo-exploracion-dropdown', 'value')
)
def actualizar_grafica_linea_exploracion(cumplimiento_seleccion, localidades_seleccion,
                        annios_seleccion, tipos_seleccion):
    
    # print(cumplimiento_seleccion, localidades_seleccion,
    #                     annios_seleccion, tipos_seleccion)

    print(type(cumplimiento_seleccion))

    # cumplimiento_seleccion = [cumplimiento_seleccion]
    # localidades_seleccion = [localidades_seleccion]
    # annios_seleccion = [annios_seleccion]
    # tipos_seleccion = [tipos_seleccion]
    print('segunda variable:', type(cumplimiento_seleccion))
    # print(cumplimiento_seleccion, localidades_seleccion,
    #                     annios_seleccion, tipos_seleccion)

    datos_consultados, existen_datos = model_jardines.consultar_promedio_cumplimiento(
        cumplimiento = cumplimiento_seleccion,
        localidades = localidades_seleccion,
        annios = annios_seleccion,
        tipos = tipos_seleccion
    )

    # ultimo_annio = model_jardines.annio_reciente

    mensaje_consulta = ''
    if not existen_datos:
        mensaje_consulta = '[NO SE ENCONTRARON DATOS]'

    fig_linea_exploracion = px.line(
        datos_consultados,
        x = 'AÑO',
        y = cumplimiento_seleccion,
        color = 'LOCALIDAD'
    )

    # fig_linea_exploracion.update_layout(yaxis_range=[0, 1])


    # fig_linea_exploracion = px.bar(datos_consultados, x = 'COMPONENTE', y = 'PROMEDIO',
    #                 color = 'COMPONENTE', #labels = {'TIPO': 'Tipo'},
    #                 # title = 'Cumplimiento General - Último Año (2019)'
    #                 title = f'Promedio por Componentes - Último Año ({ultimo_annio})'
    #             )

    # fig_componentes_segmento.update_layout(yaxis_range=[0, 1])
    # mensaje_consulta = print(cumplimiento_seleccion, localidades_seleccion,
    #                     annios_seleccion, tipos_seleccion)
    return fig_linea_exploracion, mensaje_consulta

    # mi_mensaje = f'{segmento_seleccion} {type(segmento_seleccion)} \
    #                {localidad_seleccion} {tipo_seleccion}'
    # return mi_mensaje
####################################################################################