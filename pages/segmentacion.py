import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


from components.table.table import *
# from components.sampledf.model import df_costos, df_opsales
import os
import pandas as pd
df = pd.read_excel(os.path.join("data","segmentos.xlsx"), header=0)

# data = df_costos
# data2 = df_opsales

register_page(__name__, path="/segmentacion")
# register_page('Segmentación', path="/segmentacion")

# columnas = [
#     'AÑO',
#     'CONSECUTIO',
#     'INSCRIPCION',
#     'LOCALIDAD',
#     'TIPO',
#     'COD TIPO',
#     'NOMBRE',
#     'General',
#     'Nutrición y Salubridad',
#     'Ambientes Adecuados y Seguros',
#     'Proceso Pedagógico',
#     'Talento Humano',
#     'Proceso Administrativo',
#     'Segmento'
# ]

columnas = [
    'INSCRIPCION',
    'NOMBRE',
    'LOCALIDAD',
    'TIPO',
    'Segmento'
]

# data = df[columnas][0:10]
data = df[columnas]



parametros = {
    'title': 'Segmentos',
    'description': 'Tabla de segmentación de los jardines',
    'columns': columnas
}

# params1 = {
#             'title': 'Users', 
#             'description': 'Tabla de lista de usuarios',
#             'columns': ['ID', 'CIUDAD', 'TIPO', 'FECHA']
# }

# params2 = {
#             'title': 'Municipios', 
#             'description': 'Tabla de lista de municipios',
#             'columns': ['Type','Sales per customer','Delivery Status','Category Name']
            
# }


# tablausuarios = table(data,params1)
# tablamunicipios = table(data2, params2)
tabla_segmentos = table(data, parametros)

layout= dbc.Container([
    dbc.Row([
        dbc.Col([         
            tabla_segmentos.display()
            ])
        ],
        className= "card"
    ),
    # dbc.Row([
    #     dbc.Col([
    #         tablausuarios.display()
    #     ])
    # ], className= "card"),
    ],
    className="ds4a-body"
    # className="card"
)