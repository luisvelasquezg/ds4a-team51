import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


page_name = 'Nosotros'
page_path = '/nosotros'

nombre_programa = 'DS4A Colombia - Cohort 6'
nombre_equipo = 'Team 51'
listado_integrandes = [
    'María Camila Díaz Jiménez',
    'Helena Sofía Muñoz Muñoz',
    'Juan Felipe Carvajal Restrepo',
    'Daniel Guerrero',
    'Jose Luis Charria Cifuentes',
    'Luis Enrique Velásquez Gómez'
]





card_tipos = dbc.Card([
        dbc.CardHeader(nombre_equipo),
        dbc.CardBody(
            [
                html.H5(
                    'Integrantes:',
                    className="card-title"
                ),
                html.H6(
                    # [{html.Li(i)} for i in listado_integrandes],
                    [html.Li(i) for i in listado_integrandes],
                    # listado_integrandes,
                    className="card-title"
                ),
            ]
        ),
        dbc.CardFooter(nombre_programa),
    ],
    # style={"width": "12rem"},
    className= "card-nosotros"
)


layout = html.Div(card_tipos)




