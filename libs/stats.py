import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os

# Recall app
from app import app

DATA_DIR = "data"
superstore_path = os.path.join(DATA_DIR, "superstore.csv")

df = pd.read_csv(superstore_path, parse_dates=["Order Date", "Ship Date"])

##############################################################
# SCATTER PLOT
###############################################################

###############################################################
# LINE PLOT
###############################################################


#################################################################################
# Here the layout for the plots to use.
#################################################################################
stats = html.Div(
    [
        # Place the different graph components here.
    ],
    className="ds4a-body",
)
