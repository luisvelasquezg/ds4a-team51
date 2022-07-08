import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


from components.dataframe import model_jardines

# dash.register_page(__name__, path = '/dashboard')

page_name = 'Dashboard'
page_path = '/dashboard'



####################################################################################
#   Variables
####################################################################################
# Lista de Tipos de Jardines
tipo_jardines = model_jardines.tipo_jardines()

# Serie Pandas de la cantidad de Jardines por cada Tipo
cantidad_tipo_jardines = model_jardines.cantidad_tipo_jardines()

# Cantidad de Jardines en total
total_jardines = cantidad_tipo_jardines.sum()

dic_terms = model_jardines.terminos
####################################################################################



####################################################################################
#   Componentes
####################################################################################
card_tipos = dbc.Card(
    [
        dbc.CardHeader("Tipo de Jardines"),
        dbc.CardBody(
            [
                html.H6(
                    f'{dic_terms[tipo_jardines[0]]}s: {cantidad_tipo_jardines[0]}',
                    className="card-title"
                ),
                html.H6(
                    f'{dic_terms[tipo_jardines[1]]}s: {cantidad_tipo_jardines[1]}',
                    className="card-title"
                ),
            ]
        ),
        dbc.CardFooter(f'Total: {total_jardines}', style = {'font-weight': 'bold'}),
    ],
    style={"width": "12rem"},
    # className= "card"
)

# Pie Chart - Tipos de Jardines
fig_1 = go.Figure(
    data=[
        go.Pie(labels = tipo_jardines, values = cantidad_tipo_jardines)
    ]
)


# Promedio del Cumplimiento General por Tipo de Jardín
cumplimiento_general = model_jardines.info_cumplimiento_tipos()

# Promedio del Cumplimiento de cada Componente Evaluativo por Tipo de Jardín
cumplimiento_componentes = model_jardines.info_cumplimiento_tipos(cumplimiento_general=False)

# Último año a evaluar
annio_reciente = model_jardines.annio_reciente


# Bar Chart - Cumplimiento General de Jardines por Tipo
fig_cumplimiento_general = px.bar(
                cumplimiento_general,
                x = 'TIPO',
                y = 'General',
                color = 'TIPO',
                labels = {'TIPO': 'Tipo', 'General': 'Puntuación'},
                title = f'Cumplimiento General Promedio - Último Año ({annio_reciente})')

fig_cumplimiento_general.update_layout(yaxis_range = [0, 1])


# fig_cumplimiento_general.update_layout(
#                             paper_bgcolor='rgba(0,0,0,0)',
#                             plot_bgcolor='rgba(0,0,0,0)',
#                             template = "seaborn",
#                             margin=dict(t=0)
# )


# Bar Chart - Cumplimiento de cada Componente Evaluativa de Jardines por Tipo
fig_cumplimiento_componentes = px.bar(
                cumplimiento_componentes,
                x = tipo_jardines,
                y = 'COMPONENTE', 
                barmode = 'group',
                title = f'Puntuación de Componentes por Tipo - Último Año ({annio_reciente})',
                labels = {'variable': 'Tipo', 'value': 'Puntuación'})

fig_cumplimiento_componentes.update_layout(
    xaxis_title = 'Puntuación Promedio',
    xaxis_range = [0, 1]                                    
)
####################################################################################



####################################################################################
#   Layout
####################################################################################
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3([page_name], id="div_title_dashboard"),
                    ],
                    style = {
                        'textAlign': 'center',
                        'marginBottom': '2rem',
                        'marginTop': '2rem',
                    }
                    # lg=12
                ), 
            ],
            # className= "card"
        ),
        dbc.Row([
            dbc.Col([
                dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            html.H5(
                                'Tipo de Jardines',
                                style = {'textAlign': 'center'}
                            )
                        ])
                    ]),
                    dbc.Row(
                        [
                            dbc.Col(
                                    card_tipos,
                                    style = {
                                        'textAlign': 'center',
                                        'paddingLeft': '10rem',
                                        # 'paddingRight': '2rem',
                                        # 'padding': '2rem 2rem',
                                    }
                            ),
                            # dbc.Col(
                            #     dcc.Graph(id='pie-tipo-jardines-2', figure = fig_2),
                            #     width=4,
                            #     className= "card"
                            # )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(id='pie-tipo-jardines', figure = fig_1),
                                # width = 4,
                                className= "card"
                            )
                        ]
                    )
                    ],
                className= "card",
                ),
            ]),
            dbc.Col(
                dcc.Graph(
                    id='bar-cumplimiento-general',
                    figure = fig_cumplimiento_general
                ),
                # width = 4,
                className= "card"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='bar-cumplimiento-componentes',
                    figure = fig_cumplimiento_componentes
                ),
                # width = 4,
                className= "card"
            )
        ])
    ],
    style = {'marginTop': '4rem'},
    className= "card"
)
####################################################################################
