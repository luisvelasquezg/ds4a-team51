#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization.
#######################################################

from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

import os

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'ds4a-team51 Project'  

#server = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True
