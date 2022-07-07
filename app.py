import dash

from dash import Dash, html, dcc, Input, Output

import dash_bootstrap_components as dbc
# import dash_labs as dl
# from dash.exceptions import PreventUpdate

# Pages import
from pages import dashboard, segmentacion


###########################################################
#           APP DECLARATION
###########################################################

app = Dash(
    __name__,
    # use_pages = True,
    external_stylesheets = [dbc.themes.FLATLY]
)

# app = dash.Dash(
#     __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY], update_title='Cargando...'
# )

# app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
#                 meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
# app.title = 'ds4a-team51 Project'

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

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(DS4A_Img_2),
                        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand(project_brand, className="ms-2")),
                    ],
                    align="left",
                    # className="g-0"
                    )
            ),
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
            # dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            # dbc.Collapse(
            #     search_bar,
            #     id="navbar-collapse",
            #     is_open=False,
            #     navbar=True,
            # ),
        ],
    ),
    color = "primary",
    dark = True,
)


navbar_2 = dbc.NavbarSimple(
    children = [
        dbc.NavItem(dbc.NavLink("Inicio", href="/")),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem(page["name"], href=page["path"])
                #     for page in dash.page_registry.values(),
                dbc.DropdownMenuItem("Listado de Opciones", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
                dbc.DropdownMenuItem("Listado de Opciones 2", header=True),
                # dbc.DropdownMenuItem(dashboard, href=dashboard.get_path()),
                dbc.DropdownMenuItem(dashboard.page_name, href=dashboard.page_path),
                dbc.DropdownMenuItem(segmentacion.page_name, href=segmentacion.page_path),
            ],
            nav=True,
            in_navbar=True,
            label="Opciones",
        ),
        dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand = project_brand,
    # brand_href = "#",
    color = "primary",
    dark = True,
    fluid = True,
    # className="mb-2",
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
        segmentacion
    elif pathname == segmentacion.page_path:
        return segmentacion.layout
    

    # elif pathname == '/singapore':
    #     return singapore.layout
    # else:
    #     return home.layout


# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)

# if __name__ == "__main__":
#     app.run_server(debug=True)
