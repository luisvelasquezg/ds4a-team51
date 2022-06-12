# Basics Requirements
import pathlib
import os
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
from lib import title, sidebar, us_map, stats, selector

# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = dbc.Container(
    [ 
        dbc.Row([
            dbc.Col([
                sidebar.sidebar]),
        ]),
        dbc.Row([
              title.title
        ]),
        dbc.Row([]),
        dbc.Row([]),
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
DATA_DIR = "data"
superstore_path = os.path.join(DATA_DIR, "superstore.csv")
us_path = os.path.join(DATA_DIR, "us.json")
states_path = os.path.join(DATA_DIR, "states.json")
df = pd.read_csv(superstore_path, parse_dates=["Order Date", "Ship Date"])

with open(us_path) as geo:
    geojson = json.loads(geo.read())

with open(states_path) as f:
    states_dict = json.loads(f.read())

df["State_abbr"] = df["State"].map(states_dict)
df["Order_Month"] = pd.to_datetime(df["Order Date"].dt.to_period("M").astype(str))

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
