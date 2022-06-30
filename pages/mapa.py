import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/mapa")

# from components.kpi.kpibadge import kpibadge
# from components.kpi.kpiplot import kpiplot
# from components.table.table import table
# from components.sampledf.model import df_costos
# from components.maps.mapsample import mapsample

layout=  dbc.Container(
    className="dbc"
)