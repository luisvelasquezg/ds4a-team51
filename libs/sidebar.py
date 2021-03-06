# Basics Requirements
import pathlib
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
import pandas as pd
from datetime import datetime as dt


# Recall app
from app import app

####################################################################################
# Add the DS4A_Img
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
# type of analysis Dropdown Card
#############################################################################

df = pd.read_excel(os.path.join("data","BD.xlsx"), header=1)

exclude_columns=["AÑO","CONSECUTIO","INSCRIPCION","LOCALIDAD","TIPO","COD TIPO","NOMBRE"]
type_analysis= list(df.columns)
for column in exclude_columns:
    type_analysis.remove(column)


dropdown_type_analysis = dcc.Dropdown(
    id="type_analysis_dropdown",
    value=["General"],
    options=type_analysis 
)

#############################################################################
# Location Dropdown Card
#############################################################################

localidades_list=list(df["LOCALIDAD"].drop_duplicates().dropna()) #Creates a list for the locations from the database

dropdown_loc = dcc.Dropdown(
    id="location_dropdown",
    options=localidades_list,
    value=["SUBA", "USAQUEN"],
    multi=True,
)

##############################################################################
# year Dropdown Card
##############################################################################

year_list=list(df["AÑO"].drop_duplicates().dropna()) #Creates a list for the years from the database

dropdown_year = dcc.Dropdown(
    id="year_dropdown",
    options=year_list,
    value=year_list,
    multi=True,
)

##############################################################################
# type Dropdown Card
##############################################################################

type=list(df["TIPO"].drop_duplicates().dropna()) #Creates a list for the TIPO from the database

dropdown_type = dcc.Dropdown(
    id="type_dropdown",
    options=type,
    value=["PRIVADO", "PUBLICO"],
    multi=True,
)

#############################################################################
# Sidebar Layout
#############################################################################
sidebar = html.Div(
    [
        DS4A_Img,  # Add the DS4A_Img located in the assets folder
        html.Hr(),  # Add an horizontal line
        ####################################################
        html.H5("Seleccionar tipo de cumplimiento"),
        dropdown_type_analysis,   
        html.Hr(),     
        html.H5("Seleccionar localidad"),
        dropdown_loc,
        html.Hr(),
        html.H5("Seleccionar año"),
        dropdown_year,
        html.Hr(),
        html.H5("Seleccionar tipo de jardin"),
        dropdown_type,
        html.Hr()
        ####################################################
    ],
    className="ds4a-sidebar",
)
