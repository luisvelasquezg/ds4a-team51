# Basics Requirements
import pathlib
import os
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
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
# State Dropdown Card
#############################################################################


##############################################################################
# Date Picker Card
##############################################################################


#############################################################################
# Sidebar Layout
#############################################################################
sidebar = html.Div(
    [
        DS4A_Img,  # Add the DS4A_Img located in the assets folder
        html.Hr(),  # Add an horizontal line
        ####################################################
        # Place the rest of Layout here
        ####################################################
    ],
    className="ds4a-sidebar",
)
