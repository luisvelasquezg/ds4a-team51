# Basics Requirements
from multiprocessing.sharedctypes import Value
import pathlib
import os
from tkinter import DOTBOX
import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
# import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px

##### (Librerías de prueba)
import dash_labs as dl

#####

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app


##### (Pruebas)
# Dash instance declaration
app = Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY],
    update_title='Cargando...'
)
app.config.suppress_callback_exceptions=False
#####

###########################################################
#
#           APP LAYOUT:
#
###########################################################

#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(dbc.NavLink( "Inicio", href="/")),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(page["name"], href = page["path"])
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ],
            nav=True,
            label="Opciones",
        ),
        dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand="DS4A Project - Team 51",
    color="primary",
    dark=True,
    # className="mb-2",
    className= "ds4a-nav",
)


# LOAD THE DIFFERENT FILES
from libs import title, sidebar, overal_compla_percent

# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = html.Div(
    [
        navbar,
        sidebar.sidebar,
        dl.plugins.page_container,
        overal_compla_percent.lines_graph,
        
        
        # title.title,
        
        
    ],
    # className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
    # className = 'ds4a-app'
)

###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
# Load and modify the data that will be used in the app.
#################################################################

df = pd.read_excel(os.path.join("data","BD.xlsx"), header=1)

#############################################################
# LINE PLOT : Add sidebar interaction here
#############################################################


#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################


#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################


#############################################################
# Lines: Add interactions here
#############################################################

@app.callback(
    Output("overla_lines", "figure"),
    [Input("location_dropdown", "value"),
    Input("year_dropdown", "value"),
    Input("type_dropdown", "value"),
    Input("type_analysis_dropdown", "value")
    ],
)
def update_overal_lines_graph(location_dropdown, year_dropdown, type_dropdown, type_analysis_dropdown):
    new_df = df[df["LOCALIDAD"].isin(location_dropdown) & df["AÑO"].isin(year_dropdown)]
    line_data= pd.DataFrame(new_df.groupby(["LOCALIDAD","AÑO"])["General"].mean()).reset_index()

    fig_line = px.line(line_data, x="AÑO", y="General",color="LOCALIDAD")
    return fig_line

# MAP date interaction


# MAP click interaction


if __name__ == "__main__":
    app.run_server(debug=True)
