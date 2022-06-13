# Basics Requirements
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
# MAP : Add interactions here
#############################################################

# MAP date interaction


# MAP click interaction


if __name__ == "__main__":
    app.run_server(debug=True)
