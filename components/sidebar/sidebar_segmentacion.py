import pathlib
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

import dash_bootstrap_components as dbc

import json
import pandas as pd
from datetime import datetime as dt

from components.dataframe import model_segmentos



####################################################################################
#   DS4A Logo
####################################################################################
DS4A_Img = html.Div(
    children=[
        html.Img(
            src = './assets/c1_logo_tagline.svg',
            id = "ds4a-image",
        )
    ],
)
####################################################################################



####################################################################################
#   Variables
####################################################################################
# opciones_segmento = model_segmentos.listado_segmentos
# opciones_localidad = model_segmentos.listado_localidades
# opciones_tipo = model_segmentos.listado_tipos


listdato_segmentos = model_segmentos.listado_segmentos
listado_localidades = model_segmentos.listado_localidades
listado_tipos = model_segmentos.listado_tipos

dic_tipos = model_segmentos.dic_tipo_jardines

opciones_segmento = [{'label':  i, 'value': i} for i in listdato_segmentos]
opciones_localidad = [{'label':  i, 'value': i} for i in listado_localidades]
opciones_tipo = [{'label': dic_tipos[i], 'value': i} for i in listado_tipos]

####################################################################################



####################################################################################
#   Componentes del Sidebar
####################################################################################
dropdown_segmento = dcc.Dropdown(
    id = 'segmento-dropdown',
    options = opciones_segmento,
    # value = opciones_segmento[0],
    value = listdato_segmentos[0],
    clearable = False   
)

dropdown_localidad = dcc.Dropdown(
    id = 'localidad-dropdown',
    options = opciones_localidad,
    value = listado_localidades[0],
    clearable = False 
    # multi = False,
)

dropdown_tipo = dcc.Dropdown(
    id = 'tipo-dropdown',
    options = opciones_tipo,
    value = listado_tipos[0],
    clearable = False 
)

####################################################################################



####################################################################################
#   Layout del Sidebar
####################################################################################
layout = html.Div(
    [
        DS4A_Img,
        html.Hr(),
        html.H5('Grupo Según Puntuación'),
        dropdown_segmento,
        html.Hr(),
        html.H5('Localidad'),
        dropdown_localidad,
        html.Hr(),
        html.H5('Tipo'),
        dropdown_tipo,
        html.Hr(),
    ],
    className="ds4a-sidebar-segmentacion",
    # style=SIDEBAR_STYLE,
)

####################################################################################