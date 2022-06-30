import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/")

# from components.kpi.kpibadge import kpibadge
# from components.kpi.kpiplot import kpiplot
# from components.table.table import table
# from components.sampledf.model import df_costos
# from components.maps.mapsample import mapsample

# layout=  dbc.Container(
#     [
#         dbc.Row([
#             dbc.Col([
#                 kpi3plot.display()
#             ], className='card'),
#               dbc.Col([
#                 kpi3plot.display()
#             ], className='card'),
#              dbc.Col([
#                 kpi3plot.display()
#             ], className='card'),
#              dbc.Col([
#                 kpi3plot.display()
#             ], className='card')
#         ]),
#         dbc.Row([
#             dbc.Col([
#                 mapa_ejemplo.display()


#             ], md=8), 
#             dbc.Col([
#                 dbc.Row([
#                     dbc.Col([ kpi1.display()]),
#                     dbc.Col([ kpi2.display()])
#                 ]),
#                 dbc.Row([
#                     dbc.Col([ kpi1.display()]),
#                     dbc.Col([ kpi1.display()])
#                 ]),
#             ]), 
#         ]),
#         dbc.Row([
#             dbc.Col([
#                 tablaventas.display()
#             ], className='card')
#         ])
        
      
#     ]
# )  

layout=  dbc.Container()