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
def actualizar_grafica_linea_exploracion(cumplimiento, localidades, annios, tipos):
    datos_consultados, mensaje_consulta = model_jardines.consultar_promedio_cumplimiento(cumplimiento, localidades, annios, tipos)
    fig_linea = px.line(datos_consultados, x = "AÑO", y = cumplimiento, color = "LOCALIDAD")
    fig_linea.update_layout(yaxis_range = [0, 1])
    return fig_linea, mensaje_consulta
####################################################################################