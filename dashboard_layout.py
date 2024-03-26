from dash import html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dashboard_variables import *

def init_layout(variables):
    # Extract variables from the passed dictionary
    header = variables['header']
    banner_path = variables['banner_path']
    checklist_header = variables['checklist_header']
    chart_group1_header = variables['chart_group1_header']
    chart_group2_header = variables['chart_group2_header']
    chart_group3_header = variables['chart_group3_header']
    checklist_paragraph = variables['checklist_paragraph']
    paragraph_chart_group1 = variables['paragraph_chart_group1']
    paragraph_chart_group2 = variables['paragraph_chart_group2']
    paragraph_chart_group3 = variables['paragraph_chart_group3']
    card1 = variables['card1']
    card2 = variables['card2']
    card3 = variables['card3']
    controls = variables['controls']
    grp1_tabs = variables['grp1_tabs']
    #grp2_tabs = variables['grp2_tabs']
    grp3_tabs = variables['grp3_tabs']
    grp4_tabs = variables['grp4_tabs']
    chart_usage_info1 = variables['chart_usage_info1']
    chart_usage_info2 = variables['chart_usage_info2']
    chart_usage_info3 = variables['chart_usage_info3']
    background_image = variables['background_image']

    layout = dbc.Container(
        style={
            'background-image': f'url("{background_image}")',
            'background-size': 'cover',
            'background-repeat': 'no-repeat',
            'background-position': 'center',
            #'height': '100vh',
            'opacity': 0.75
            },

        children = [
            html.Img(src=banner_path, className='img-fluid'),
            html.Br(),
            header,
            html.Br(),

            dbc.Row([
                dbc.Col(card1, width=3),
                dbc.Col(card2, width=3),
                dbc.Col(card3, width=3)
            ],
            className="mb-4",
            justify="center"
            ),
        
            html.Br(),
            checklist_header,
            checklist_paragraph,
            html.Br(),

            dbc.Row([    
                dbc.Col(controls, width=6),
            ],
            className="mb-4",
            justify="center",
            #style={"position": "sticky", "top": 0, "zIndex": 1000},
            ),

            html.Br(),
            chart_group1_header,
            paragraph_chart_group1,
            html.Br(),

            dbc.Row([    
                dbc.Col(chart_usage_info1, width=4),
                dbc.Col(grp1_tabs, width=6),
            ],
            className="mb-4",
            justify="center"
            ),

#            html.Br(),
#            chart_group1_header,
#            paragraph_chart_group1,
#            html.Br(),

#            dbc.Row([    
#                dbc.Col(chart_usage_info, width=4),
#                dbc.Col(grp2_tabs, width=6),
#            ],
#            className="mb-4",
#            justify="center"
#            ),

            html.Br(),
            chart_group2_header,
            paragraph_chart_group2,
            html.Br(),

            dbc.Row([    
                dbc.Col(chart_usage_info2, width=4),
                dbc.Col(grp3_tabs, width=6),
            ],
            className="mb-4",
            justify="center"
            ),

            html.Br(),
            chart_group3_header,
            paragraph_chart_group3,
            html.Br(),

            dbc.Row([    
                dbc.Col(chart_usage_info3, width=4),
                dbc.Col(grp4_tabs, width=6),
            ],
            className="mb-4",
            justify="center"
            ),

            html.Br(),

        ],
        fluid=True,
        className="dbc dbc-ag-grid",
    )
    return layout