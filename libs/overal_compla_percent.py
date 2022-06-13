import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import os

import plotly.graph_objects as go
import plotly.express as px


import numpy as np
import pandas as pd

# Recall app
from app import app

#############################
# Load graph data
#############################

df = pd.read_excel(os.path.join("data","BD.xlsx"), header=1)

line_data= pd.DataFrame(df.groupby(["LOCALIDAD","AÑO"])["General"].mean()).reset_index()

fig_line = px.line(line_data, x="AÑO", y="General",color="LOCALIDAD")

##############################
# Map Layout
##############################
lines_graph = html.Div(
    children=[
        dbc.Row(html.Div(html.P(" "))),
        dbc.Row(html.Div(html.P(" "))),
        dbc.Row(html.Div(html.P(" "))),
        dbc.Row(
            dbc.Col(
               dcc.Graph(figure=fig_line, id="overla_lines"),
               width={"size": 12, "offset": 0 }
            )
        )
    ],
    className="ds4a-body",
)
