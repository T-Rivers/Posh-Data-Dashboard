from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

def init_dashboard_variables(df):
    # Dropdown and checklist variables based on df
    markets = df['market'].unique().tolist()
    categories = df['category'].unique().tolist()

    # Components for GROUP 1 to GROUP 4
    grp1_sunburst_tab = dbc.Tab([dcc.Graph(id="sunburst-chart")], label="Category Overview")
    grp1_quantity_bar_tab = dbc.Tab([dcc.Graph(id="quantity-bar-chart")], label="Category Review: Quantity Sold")
    grp1_total_dollar_bar_tab = dbc.Tab([dcc.Graph(id="total-dollar-bar-chart")], label="Category Review: Total Sales(USD)")
    grp1_tabs = dbc.Card(dbc.Tabs([grp1_sunburst_tab, grp1_quantity_bar_tab, grp1_total_dollar_bar_tab]))

    grp2_subcategory_bar_tab = dbc.Tab([dcc.Graph(id="subcategory-bar-chart")], label="Subcategory Review")
    grp2_tabs = dbc.Card(dbc.Tabs(grp2_subcategory_bar_tab))

    grp3_price_range_bar_fig_tab = dbc.Tab([dcc.Graph(id="price-range-bar-chart")], label="Category Review: Price Points")
    grp3_days_range_bar_fig_tab = dbc.Tab([dcc.Graph(id="days-range-bar-chart")], label="Category Review: Days Listed")
    grp3_tabs = dbc.Card(dbc.Tabs([grp3_price_range_bar_fig_tab, grp3_days_range_bar_fig_tab]))

    grp4_price_range_brand_count_tab = dbc.Tab([dcc.Graph(id="price-range-brand-count-chart")], label="Brand Review: Price Points")
    grp4_days_range_brand_count_tab = dbc.Tab([dcc.Graph(id="days-range-brand-count-chart")], label="Brand Review: Days Listed")
    grp4_sunburst_brand_count_tab = dbc.Tab([dcc.Graph(id="brand_sunburst_fig")], label="Brand Overview")

    grp4_tabs = dbc.Card(dbc.Tabs([grp4_sunburst_brand_count_tab, grp4_price_range_brand_count_tab, grp4_days_range_brand_count_tab]))

    # UI components used in layout
    banner_path = 'assets/banner-3.png'
    header = html.H3('A Visual Exploration of Poshmark Sales Data', className="bg-primary text-white p-2 mb-2 text-center")

    checklist_header = html.H2('Select Market & Category', className="bg-transparent default text color p-2 mb-2 text-center")
    checklist_paragraph = html.Div([
        "You can select multiple options,",
        html.Br(),
        "but we recommend starting with one until you are familiar with reading the charts.",
    ],className="fs-5 text-dark text-center",)

    chart_group1_header = html.H2('Category Review: Sales Overview', className="bg-transparent default text color p-2 mb-2 text-center")
    paragraph_chart_group1 = html.Div([
        "The charts below provide information about amount sold and total dollar sales within selected markets/categories.",
        html.Br(),
        "Be sure to read the 'How to Read These Charts' for helpful information about reading the charts.",
    ],className="fs-5 text-dark text-center",)

    chart_group2_header = html.H2('Category Review: Price Points & Days Listed', className="bg-transparent default text color p-2 mb-2 text-center")
    paragraph_chart_group2 = html.Div([
        "The charts below provide information about setting price points and sell-through data within selected markets/categories.",
        html.Br(),
        "Be sure to read the 'How to Read These Charts' for helpful information about reading the charts.",
    ],className="fs-5 text-dark text-center",)

    chart_group3_header = html.H2('Brand Review: Overview of Top Brands, Price Points & Days Listed', className="bg-transparent default text color p-2 mb-2 text-center")
    paragraph_chart_group3 = html.Div([
        "The charts below provide information about top selling brands, setting price points and their sell-through rates within selected markets/categories.",
        html.Br(),
        "Be sure to read the 'How to Read These Charts' for helpful information about reading the charts.",
    ],className="fs-5 text-dark text-center",)

    card1 = dbc.Card([dbc.CardHeader("Card 1 Header"),dbc.CardBody([html.H5("Card 1 Title", className="card-title"),html.P("Card 1 Content",className="card-text"),]),],color="primary",inverse=True,)
    card2 = dbc.Card([dbc.CardHeader("Card Header 2"),dbc.CardBody([html.H5("Card 2 Title", className="card-title"),html.P("Card 2 Content",className="card-text"),]),],color="secondary",inverse=True,)
    card3 = dbc.Card([dbc.CardHeader("Card 3 Header"),dbc.CardBody([html.H5("Card 3 Title"),html.P("Card 3 Content",className="card-text"),]),],color="info",inverse=True,)

    market_checklist = html.Div([dbc.Label("Please Select a Market",style={'text-align': 'center', 'font-weight': 'bold', 'font-size': '20px'}),
                                 dbc.Checklist(
                                     id="market-checklist",
                                     options=markets,value=[],
                                     inline=True,
                                     style={'margin': 'auto', 'text-align': 'center'}
                                     ),
                                 ],className="mb-4",style={'text-align': 'center'})
    
    category_checklist = html.Div([dbc.Label("Please Select a Category", style={'text-align': 'center', 'font-weight': 'bold', 'font-size': '20px'}),
                                   dbc.Checklist(
                                       id="category-checklist",
                                       options=categories,
                                       value=[],
                                       inline=True,
                                       style={'margin': 'auto', 'text-align': 'center'}
                                       ),
                                   ],className="mb-4",style={'text-align': 'center'})

    controls = dbc.Card([market_checklist, category_checklist],body=True, style={'width': '10'})

    chart_tips = html.Div([
        html.Strong("Tips and Tricks:"),
        " Hover over any area of the chart with your mouse for more information about the section you are looking at. Charts are equipped with zoom-in and zoom-out funcationality, icons are located at the upper right corner double click anywhere on the graph to return to a normal view."
    ])    

    group1_chart1 = html.Div([
        html.Strong("Category Overview:"),
        " A sunburst chart displaying the market(s) in the center, categories in the middle ring, and subcategories in the outer ring. The purpose is to provide an overview of market selections and detailed information about category/subcategory breakdowns."
    ])
    group1_chart2 = html.Div([
        html.Strong("Quantity Sold:"),
        " A bar chart displaying the number of items sold within selected category/markets. Categories are displayed along the bottom of the chart and the bars height shows the number of items sold indicated at left side of the chart. The purpose is to allow for easy comparison of quantities sold within different markets/categories."
    ])    
    group1_chart3 = html.Div([
        html.Strong("Total Sales:"),
         " A bar chart displaying the total dollar value (USD) of sales within selected category/market. Categories are displayed along the bottom of the chart and the bars height shows total dollar sales indicated at the left side of the chart. The purpose is to allow for easy comparison of total dollar sales within different markets/categories."
    ])

    chart_usage_info1 = dbc.Card([
        dbc.CardBody([
            html.H5("How To Read These Charts", className="card-title"),
            html.Hr(),
            html.P(chart_tips, className="card-text"),]),
        dbc.CardBody(
            [html.P(group1_chart1, className="card-text"),]),
        dbc.CardBody(
            [html.P(group1_chart2, className="card-text"),]),
        dbc.CardBody(
            [html.P(group1_chart3, className="card-text"),]),
        ], className="h-100")
    
    group2_chart1 = html.Div([
        html.Strong("Price Points:"),
        " A bar chart displaying the number of items sold within selected category/market that fall within a price point. Price points are listed at the bottom of the chart and the bars height shows the number of items sold within each price point indicated at the left side of the chart. The purpose is to illustrate popular price points per categories/market."
    ])
    group2_chart2 = html.Div([
        html.Strong("Days Listed:"),
        " A bar chart displaying the duration of time items within selected category/market have been listed before being sold. Day ranges are listed at the bottom of the chart and the bars height shows the number of items sold that fall within day ranges indicated at the left side of the chart. The purpose is to illustrate how quickly items in categories/market sell."
    ])

    chart_usage_info2 = dbc.Card([
        dbc.CardBody([
            html.H5("How To Read These Charts", className="card-title"),
            html.Hr(),
            html.P(chart_tips, className="card-text"),]),
        dbc.CardBody(    
            [html.P(group2_chart1, className="card-text"),]),
        dbc.CardBody(
            [html.P(group2_chart2, className="card-text"),]),
        ], className="h-100")
    
    group3_chart1 = html.Div([
        html.Strong("Brand Overview:"),
        " A sunburst chart displaying the market(s) in the center, categories in the middle ring, and popular brands (those occurring more than 10 times in sales data) in the outer ring. The purpose is to provide an overview of market selections and detailed information about popular category/brand breakdowns."
    ])
    group3_chart2 = html.Div([
        html.Strong("Brand Price Points:"),
        " A segmented bar chart displaying how popular brands fall within different price points. Price points are listed at the bottom of the chart and the segments within a bar indicate different brands. The bars height shows the number of items sold within each price point indicated at the left side of the chart. The purpose is to illustrate popular price points within brands and category/markets."
    ])
    group3_chart3 = html.Div([
        html.Strong("Brand Days Listed:"),
        " A segmented bar chart displaying the time duration popular brands have been listed before being sold. Day ranges are listed at the bottom of the chart and the segments within a bar indicate different brands. The bars height shows the number of items sold that fall within the different time durations indicated at the left side of the chart. The purpose is to illustrate how quickly popular brands will sell."
    ])

    chart_usage_info3 = dbc.Card([
        dbc.CardBody([
            html.H5("How To Read These Charts", className="card-title"),
            html.Hr(),
            html.P(chart_tips, className="card-text"),]),
        dbc.CardBody(   
            [html.P(group3_chart1, className="card-text"),]),
        dbc.CardBody(
            [html.P(group3_chart2, className="card-text"),]),
        dbc.CardBody(
            [html.P(group3_chart3, className="card-text"),]),
        ], className="h-100")
    
    background_image = "/assets/background.png"
    
    # Return a dictionary of all these components for use in layout and callbacks
    return {
        "markets": markets,
        "categories": categories,
        "grp1_tabs": grp1_tabs,
        "grp2_tabs": grp2_tabs,
        "grp3_tabs": grp3_tabs,
        "grp4_tabs": grp4_tabs,
        "header": header,
        "banner_path": banner_path,
        "chart_group1_header": chart_group1_header,
        "chart_group2_header": chart_group2_header,
        "chart_group3_header": chart_group3_header,
        "checklist_header": checklist_header,
        "paragraph_chart_group1": paragraph_chart_group1,
        "paragraph_chart_group2": paragraph_chart_group2,
        "paragraph_chart_group3": paragraph_chart_group3,
        "checklist_paragraph": checklist_paragraph,
        "card1": card1,
        "card2": card2,
        "card3": card3,
        "market_checklist": market_checklist,
        "category_checklist": category_checklist,
        "controls": controls,
        "chart_usage_info1": chart_usage_info1,
        "chart_usage_info2": chart_usage_info2,
        "chart_usage_info3": chart_usage_info3,
        "background_image": background_image
    }
