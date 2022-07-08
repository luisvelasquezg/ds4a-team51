import pathlib
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

import dash_bootstrap_components as dbc

import json
import pandas as pd
from datetime import datetime as dt

from components.dataframe import model_segmentos

# # Recall app
# from app import app


####################################################################################
# Estilos
####################################################################################
# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }


# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }
####################################################################################



####################################################################################
# DS4A Logo
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



# exclude_columns=["AÑO","CONSECUTIO","INSCRIPCION","LOCALIDAD","TIPO","COD TIPO","NOMBRE"]
# type_analysis= list(df.columns)
# for column in exclude_columns:
#     type_analysis.remove(column)



####################################################################################
# Variables
####################################################################################
# opciones_segmento = model_segmentos.listado_segmentos
# opciones_localidad = model_segmentos.listado_localidades
# opciones_tipo = model_segmentos.listado_tipos

dic_tipos = {'PRIVADO': 'Privado', 'PUBLICO': 'Público'}

opciones_segmento = [{'label':  i, 'value': i} for i in model_segmentos.listado_segmentos]
opciones_localidad = [{'label':  i, 'value': i} for i in model_segmentos.listado_localidades]
opciones_tipo = [{'label':  dic_tipos[i], 'value': i} for i in model_segmentos.listado_tipos]
####################################################################################



####################################################################################
# Componentes del Sidebar
####################################################################################
dropdown_segmento = dcc.Dropdown(
    id = 'segmento-dropdown',
    options = opciones_segmento,
    value = opciones_segmento[0],
    clearable = False   
)

dropdown_localidad = dcc.Dropdown(
    id = 'localidad-dropdown',
    options = opciones_localidad,
    value = opciones_localidad[0],
    clearable = False 
    # multi = False,
)

dropdown_tipo = dcc.Dropdown(
    id = 'tipo-dropdown',
    options = opciones_tipo,
    value = opciones_tipo[0],
    clearable = False 
)
####################################################################################



####################################################################################
# Layout del Sidebar
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