from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

import dash_bootstrap_components as dbc

from components.dataframe import model_jardines

####################################################################################
# Imagen DS4A_Img
####################################################################################

DS4A_Img = html.Div(
    children=[
        html.Img(
            src=app.get_asset_url("c1_logo_tagline.svg"),
            id="ds4a-image",
        )
    ],
)

#############################################################################



####################################################################################
# Variables
####################################################################################
listado_cumplimiento = model_jardines.listado_tipos
listado_localidades = model_jardines.listado_localidades
listado_annios = model_jardines.listado_annios
listado_tipos = model_jardines.listado_tipos
####################################################################################



####################################################################################
#   Componentes del Sidebar
####################################################################################
dropdown_segmento = dcc.Dropdown(
    id = 'cumplimiento-dropdown',
    options = listado_cumplimiento,
    # value = listado_cumplimiento[0],
    # value = listado_cumplimiento[0],
    clearable = False   
)

dropdown_localidad = dcc.Dropdown(
    id = 'localidad-dropdown',
    options = listado_localidades,
    # value = listado_localidades[0],
    clearable = False 
    # multi = False,
)

dropdown_annio = dcc.Dropdown(
    id = 'annio-dropdown',
    options = listado_tipos,
    # value = listado_tipos[0],
    multi = False, 
)

dropdown_tipo = dcc.Dropdown(
    id = 'tipo-dropdown',
    options = listado_tipos,
    # value = listado_tipos[0],
    multi = False,
)

####################################################################################


####################################################################################
#   Layout del Sidebar
####################################################################################
layout = html.Div(
    [
        DS4A_Img,
        html.Hr(),
        html.H5('Tipo de Cumplimiento'),
        dropdown_segmento,
        html.Hr(),
        html.H5('Localidad'),
        dropdown_localidad,
        html.Hr(),
        html.H5('Año'),
        dropdown_annio,
        html.Hr(),
        html.H5('Tipo'),
        dropdown_tipo,
        html.Hr(),
    ],
    className="ds4a-sidebar-segmentacion",
    # style=SIDEBAR_STYLE,
)

####################################################################################