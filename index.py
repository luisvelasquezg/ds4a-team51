# Basics Requirements
from multiprocessing.sharedctypes import Value
import pathlib
import os
from tkinter import DOTBOX
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px

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

###########################################################
#
#           APP LAYOUT:
#
###########################################################



# LOAD THE DIFFERENT FILES
from libs import title, sidebar,overal_compla_percent

# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = html.Div(
    [
        title.title,
        sidebar.sidebar,
        overal_compla_percent.lines_graph
    ],
    className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
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
def update_overal_lines_graph(location_dropdown,year_dropdown,type_dropdown,type_analysis_dropdown):
    new_df= df[df["LOCALIDAD"].isin(location_dropdown)&df["AÑO"].isin(year_dropdown)]
    line_data= pd.DataFrame(new_df.groupby(["LOCALIDAD","AÑO"])["General"].mean()).reset_index()

    fig_line = px.line(line_data, x="AÑO", y="General",color="LOCALIDAD")
    return fig_line

# MAP date interaction


# MAP click interaction


if __name__ == "__main__":
    app.run_server(debug=True)
