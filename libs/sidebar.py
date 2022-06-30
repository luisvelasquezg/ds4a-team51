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



# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}



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
    options=type_analysis, 
)

# dropdown_type_analysis = dbc.DropdownMenu(
#     id="type_analysis_dropdown",
#     # value=["General"],
#     children=type_analysis, 
#     size="sm"
# )


#############################################################################
# Location Dropdown Card
#############################################################################

# localidades_list=list(df["LOCALIDAD"].drop_duplicates().dropna()) #Creates a list for the locations from the database

localidades_list = sorted(list( df["LOCALIDAD"].dropna().unique() ))

dropdown_loc = dcc.Dropdown(
    id="location_dropdown",
    options=localidades_list,
    value=["SUBA", "USAQUEN"],
    multi=True,
)

# dropdown_loc = dbc.DropdownMenu(
#     id="location_dropdown",
#     children=localidades_list,
#     # value=["SUBA", "USAQUEN"],
#     # multi=True,
#     size="sm"
# )


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

# dropdown_year = dbc.DropdownMenu(
#     id="year_dropdown",
#     children=year_list,
#     # value=year_list,
#     # multi=True,
#     size="sm"
# )


##############################################################################
# type Dropdown Card
##############################################################################

type_list = list(df["TIPO"].drop_duplicates().dropna()) #Creates a list for the TIPO from the database

dropdown_type = dcc.Dropdown(
    id="type_dropdown",
    options=type_list,
    value=["PRIVADO", "PUBLICO"],
    multi=True,
)

# dropdown_type = dbc.DropdownMenu(
#     id="type_dropdown",
#     children=type_list,
#     # value=["PRIVADO", "PUBLICO"],
#     # multi=True,
#     size="sm"
# )

#############################################################################
# Sidebar Layout
#############################################################################
sidebar = html.Div(
    [
        DS4A_Img,  # Add the DS4A_Img located in the assets folder
        html.Hr(),  # Add an horizontal line
        ####################################################
        html.H5("Tipo de cumplimiento"),
        dropdown_type_analysis,   
        html.Hr(),     
        html.H5("Localidad"),
        dropdown_loc,
        html.Hr(),
        html.H5("Año"),
        dropdown_year,
        html.Hr(),
        html.H5("Tipo de Jardín"),
        dropdown_type,
        html.Hr()
        ####################################################
    ],
    className="ds4a-sidebar",
    # style=SIDEBAR_STYLE,
)





# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Page 1", href="/page-1", active="exact"),
#                 dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )
