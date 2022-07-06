import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


from components.dataframe import model_jardines

# dash.register_page(__name__, path = '/dashboard')

page_name = 'Dashboard'
page_path = '/dashboard'

def get_name():
    return page_name
    
def get_path():
    return page_path


# layout = html.Div([
#     html.H1('Dashboard'),
#     html.Div(
#         [
#             'My content'
#         ]
#     )
# ])



# Lista de Tipos de Jardines
tipo_jardines = model_jardines.tipo_jardines()

# Serie Pandas de la cantidad de Jardines por cada Tipo
cantidad_tipo_jardines = model_jardines.cantidad_tipo_jardines()

# Cantidad de Jardines en total
total_jardines = cantidad_tipo_jardines.sum()


# table_1 =  dash_table.DataTable(
#     id = 'kindergarten-type',
#     columns = [{'name': col, 'id': col} for col in columnas_tipo_jardines],
#     data = cantidad_tipo_jardines.to_dict('records')
#     # data = electricity.to_dict('records')
# )

dic_terms = model_jardines.terminos

card_1 = dbc.Card(
    [
        dbc.CardHeader("Tipo de Jardines"),
        dbc.CardBody(
            [
                html.H6(
                    f'{dic_terms[tipo_jardines[0]]}s: {cantidad_tipo_jardines[0]}',
                    # {'name': col, 'id': col} for col in tipo_jardines,
                    className="card-title"
                ),
                html.H6(
                    f'{dic_terms[tipo_jardines[1]]}s: {cantidad_tipo_jardines[1]}',
                    # {'name': col, 'id': col} for col in tipo_jardines,
                    className="card-title"
                ),
                # html.H4("Card title", className="card-title"),
                # html.P(f'Total: {total_jardines}', className="card-text"),
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

fig_1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    template = "seaborn",
    # margin=dict(t=0, b=10, pad=10),
)


# fig_2 = px.pie(values = cantidad_tipo_jardines, labels = tipo_jardines, names = tipo_jardines)

# fig_2.update_layout(
#     paper_bgcolor='rgba(0,0,0,0)',
#     plot_bgcolor='rgba(0,0,0,0)',
#     template = "seaborn",
#     # margin=dict(t=0, b=10, pad=10),
# )


# Promedio del Cumplimiento General por Tipo de Jardín
cumplimiento_general = model_jardines.info_cumplimiento_tipos()

# Promedio del Cumplimiento de cada Componente Evaluativo por Tipo de Jardín
cumplimiento_componentes = model_jardines.info_cumplimiento_tipos(cumplimiento_general=False)

# Último año a evaluar
ultimo_annio = model_jardines.ultimo_annio


# Bar Chart - Cumplimiento General de Jardines por Tipo
fig_cumplimiento_general = px.bar(
                cumplimiento_general,
                x = 'TIPO',
                y = 'General',
                color = 'TIPO',
                labels = {'TIPO': 'Tipo', 'General': 'Puntuación'},
                title = f'Cumplimiento General Promedio - Último Año ({ultimo_annio})')

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
                title = f'Puntuación de Componentes por Tipo - Último Año ({ultimo_annio})',
                labels = {'variable': 'Tipo', 'value': 'Puntuación'})

fig_cumplimiento_componentes.update_layout(xaxis_title = 'Puntuación Promedio')


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1([page_name], id="div_title_dashboard"),
                    ],
                    style = {'textAlign': 'center'}
                    # lg=12
                ), 
            ],
            # className= "card"
        ),
        dbc.Row([
            dbc.Col([
                dbc.Container([
                    dbc.Row(
                        [
                            dbc.Col([
                                    # table_1
                                    card_1
                            ]),
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
                # className= "card",
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
    className= "card"
)


## layout backup ##
# layout = dbc.Container(
#     [
#         dbc.Container([
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [
#                             html.H1([page_name], id="div_title_dashboard"),
#                         ],
#                         style = {'textAlign': 'center'}
#                         # lg=12
#                     ), 
#                 ],
#                 # className= "card"
#             ),
#             dbc.Row(
#                 [
#                     dbc.Col([
#                             # table_1
#                             card_1
#                     ]),
#                     # dbc.Col(
#                     #     dcc.Graph(id='pie-tipo-jardines-2', figure = fig_2),
#                     #     width=4,
#                     #     className= "card"
#                     # )
#                 ]
#             ),
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         dcc.Graph(id='pie-tipo-jardines', figure = fig_1),
#                         width = 4,
#                         className= "card"
#                     )
#                 ]
#             )
#         ],
#         className= "card"
#         )
#     ],
#     className= "card"
# )