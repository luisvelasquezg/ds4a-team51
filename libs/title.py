# Basics Requirements
import pathlib
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app import app

title=html.Div(className="ds4a-title", 
    children=[
        dbc.Row([
            dbc.Col(
                html.H1("ds4a-team51 Project"),
                width={"size": 6, "offset": 3}
                )
        ])
    ],
    id="title")