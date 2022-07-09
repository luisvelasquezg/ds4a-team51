import dash

from dash import Dash, html, dcc, Input, Output

import dash_bootstrap_components as dbc
# import dash_labs as dl
# from dash.exceptions import PreventUpdate

# Pages import
from pages import dashboard, exploracion, segmentacion, nosotros


###########################################################
#           APP DECLARATION
###########################################################

app = Dash(
    __name__,
    # use_pages = True,
    external_stylesheets = [dbc.themes.FLATLY]
)

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True

# app = dash.Dash(
#     __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY], update_title='Cargando...'
# )

# app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
#                 meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'DS4A Team 51 - Project'

# DS4A_Logo_1 = 'assets/ds4a_colombia.svg'
DS4A_Logo_1 = 'ds4a_colombia.svg'

DS4A_Img = html.Div(
    children=[
        html.Img(
            src = app.get_asset_url(DS4A_Logo_1),          
            id = "ds4a-image",
        )
    ],
)

DS4A_Img_2 = html.Img(
            src = app.get_asset_url(DS4A_Logo_1),
            # src = DS4A_Logo_1,
            height = '30px',
            id = "ds4a-image",
)

project_brand = "DS4A Project - Team 51"



# Navigation Bar
navbar_2 = dbc.NavbarSimple(
    children = [
        dbc.NavItem(dbc.NavLink(dashboard.page_name, href=dashboard.page_path)),
        # dbc.NavItem(dbc.NavLink(exploracion.page_name, href=exploracion.page_path)),
        dbc.NavItem(dbc.NavLink(segmentacion.page_name, href=segmentacion.page_path)),
        dbc.NavItem(dbc.NavLink(nosotros.page_name, href=nosotros.page_path)),
    ],
    brand = project_brand,
    # brand_href = "#",
    color = "primary",
    dark = True,
    fluid = True,
    # className="mb-2",
    className = 'ds4a-navbar'
)


###########################################################
#           APP LAYOUT
###########################################################
app.layout = html.Div(
    [
        dcc.Location(id = 'url', refresh = False),
        navbar_2,
        html.Div(
            id = 'page-content',
            style = {'padding-top': '40px'}
        )
    ],
)


###########################################################
#           APP CALLBACKS
###########################################################
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == dashboard.page_path:
        return dashboard.layout
    elif pathname == exploracion.page_path:
        return exploracion.layout
    elif pathname == segmentacion.page_path:
        return segmentacion.layout
    elif pathname == nosotros.page_path:
        return nosotros.layout
    elif pathname == '/':
        return dashboard.layout
    



# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=False)

# if __name__ == "__main__":
#     app.run_server(debug=True)
