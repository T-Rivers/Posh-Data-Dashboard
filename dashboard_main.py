# APP LAYOUT 
from dash import Dash
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from dash_bootstrap_templates import load_figure_template

#styling information
#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [dbc.themes.MINTY]
app = Dash(__name__, external_stylesheets=external_stylesheets)#, dbc_css])
load_figure_template("minty")

# load data
from dashboard_data_functions import load_data
df = load_data()

# Initialize dashboard variables
from dashboard_variables import init_dashboard_variables
variables = init_dashboard_variables(df)

# Import the function that initializes your app's layout
from dashboard_layout import init_layout
app.layout = init_layout(variables) 

# Import and call the callback registration function
from dashboard_callback_functions import register_callbacks
register_callbacks(app, df)  # Pass both app and df


if __name__ == '__main__':
    app.run(debug=True)