from dash.dependencies import Input, Output
import plotly.express as px
from dashboard_variables import *

def register_callbacks(app, df):
    @app.callback(
        [Output('sunburst-chart', 'figure'),
         Output('quantity-bar-chart', 'figure'),
         Output('total-dollar-bar-chart', 'figure'),
         #Output('subcategory-bar-chart', 'figure'),
         Output('price-range-bar-chart', 'figure'),
         Output('days-range-bar-chart', 'figure'),
         Output('price-range-brand-count-chart', 'figure'),
         Output('days-range-brand-count-chart', 'figure'),
         Output('brand_sunburst_fig', 'figure')],
        [Input('market-checklist', 'value'),
         Input('category-checklist', 'value')]
    )
    def update_all_charts(selected_market, selected_categories):
        filtered_data = df[(df['market'].isin(selected_market)) &
                          (df['category'].isin(selected_categories))].copy()
        
        market_colors = {'Women': '#FF794C','Men': '#54CC9C', 'Kids': '#FCD361'}
        #'Women': '#F19799','Men': '#7CC0AB', 'Kids': '#FCD361'} pink primary blue yellow


        # Update Sunburst Chart
        sunburst_fig = px.sunburst(filtered_data, path=['market', 'category', 'subcategory'],
                                   color='market', color_discrete_map=market_colors, 
                                   title=f"Category Overview: {selected_market} {', '.join(selected_categories)}",
                                   width=800, height=600)
        
        sunburst_fig.update_traces(hovertemplate='Info: %{id}<br>Count: %{value}<extra></extra>')
        sunburst_fig.update_layout(hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                   font=dict(size=14, color='black'))
        
        
        # Update Quantity Bar Chart
        quantity_bar_fig = px.bar(filtered_data.groupby(['category','market']).size().reset_index(name='count'),
                                  x='category', y='count', 
                                  color='market',
                                  color_discrete_map=market_colors,
                                  title=f"Category Review: Quantity Sold  {selected_market} {', '.join(selected_categories)}",
                                  hover_data={'count': True},
                                  labels={'market':'Market','category': 'Category', 'count': 'Quantity Sold'})
        quantity_bar_fig.update_layout(barmode='group',
                                       hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                       font=dict(size=14, color='black')
                                       )

        # Update Total Dollar Bar Chart
        total_dollar_bar_fig = px.bar(filtered_data.groupby(['category','market'])['price'].sum().reset_index(name='total'),
                                      x='category', y='total', 
                                      color='market',
                                      color_discrete_map=market_colors,
                                      title=f"Category Review: Total Sales (USD $) {selected_market} {', '.join(selected_categories)}",
                                      hover_data={'total': True},
                                      labels={'market': 'Market', 'category': 'Category', 'total': 'Total Sales (USD $)'})
        total_dollar_bar_fig.update_layout(barmode='group',
                                           hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                           font=dict(size=14, color='black')
                                           )
        
    #    subcategory_bar_fig = px.bar(filtered_data.groupby(['subcategory','category','market']).size().reset_index(name='count'),
    #                                x='subcategory', y='count',
    #                                color='market',
    #                                color_discrete_map=market_colors,
    #                                title=f"Subcategory Counts: {selected_market} {', '.join(selected_categories)}",
    #                                hover_data={'market': True, 'category': True, 'count': True},
    #                                labels={'market':'Market', 'category': 'Category', 'subcategory': 'Subcategory', 'count': 'Count'})
    #    subcategory_bar_fig.update_traces(hovertemplate='Market: %{customdata[0]}<br>Category: %{customdata[1]}<br>Subcategory: %{x}<br>Count: %{y}<extra></extra>')

    #    subcategory_bar_fig.update_layout(hoverlabel = dict(font = dict(family="Arial", size=14, color="black")))

        #Update Price Range figure
        price_range_counts = filtered_data.groupby(['price range', 'market', 'category']).size().reset_index(name='count')
        price_range_bar_fig = px.bar(price_range_counts, x='price range', y='count',
                                    color='market',
                                    color_discrete_map=market_colors,
                                    title=f"Category Review: Price Points {selected_market} {', '.join(selected_categories)}",
                                    hover_data={'market': True, 'category': True, 'count': True},
                                    labels={'market': 'Market', 'category':'Category', 'price range': 'Price Point', 'count': 'Quantity Sold'})
        
        price_range_bar_fig.update_traces(marker_line_width=1.0,
                                          hovertemplate='Market: %{customdata[0]}<br>Category: %{customdata[1]}<br>Price Point: %{x}<br>Count: %{y}<extra></extra>')
        price_range_bar_fig.update_layout(barmode='group',
                                          hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                          font=dict(size=14, color='black')
                                          )

        #update x axis order:
        custom_order = ['price $3-10', 'price $11-26', 'price $26-50', 'price $51-100', 'price $101-150', 'price $151-200', 'price $201-300', 'price $301-400',
                    'price $401-500', 'price $501-700', 'price $701-900', 'price $901-1500', 'more than $1500']
        price_range_bar_fig.update_xaxes(categoryorder='array', categoryarray=custom_order)

        # Update Days Range figure
        days_range_counts = filtered_data.groupby(['range of days', 'market', 'category']).size().reset_index(name='count')
        days_range_bar_fig = px.bar(days_range_counts, x='range of days', y='count',
                                    color='market',
                                    color_discrete_map=market_colors,
                                    title=f"Category Review: Days Listed {selected_market} {', '.join(selected_categories)}",
                                    hover_data={'market': True, 'category': True, 'count': True},
                                    labels={'market':'Market', 'category':'Category', 'range of days': 'Days Listed', 'count': 'Quantity Sold'})
        #days_range_bar_fig.update_traces(hovertemplate='Days Range: %{x}<br>Count: %{y}')
        days_range_bar_fig.update_traces(marker_line_width=1.0,
                                         hovertemplate='Market: %{customdata[0]}<br>Category: %{customdata[1]}<br>Days Listed: %{x}<br>Count: %{y}<extra></extra>')
        days_range_bar_fig.update_layout(barmode='group',
                                         hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                         font=dict(size=14, color='black')
                                         )

        #update x axis order
        custom_order2 = ['0-15 days', '16-40 days', '41-60 days', '61-80 days','81-100 days', 'more than 100 days']
        days_range_bar_fig.update_xaxes(categoryorder='array', categoryarray=custom_order2)
        
        #Update Price Range Brands Bar chart
        brand_price_counts_filtered = filtered_data.groupby('market & category & brand').filter(lambda x: len(x) >= 10)
        brand_price_counts_filtered = brand_price_counts_filtered .groupby(['market', 'category & brand', 'market & category & brand', 'price range']).size().reset_index(name='count')
        
        # Create bar chart showing count of items for each price range
        brands_price_range_bar_fig = px.bar(brand_price_counts_filtered, x='price range', y='count',
                                    color='market',
                                    color_discrete_map=market_colors,
                                    title=f"Brands Review: Price Points  {selected_market} {', '.join(selected_categories)}",
                                    hover_data={'market': True, 'category & brand': True, 'count': True},
                                    labels={'market':'Market', 'price range': 'Price Point', 'count': 'Total Quantity Sold'})
        #brands_price_range_bar_fig.update_traces(hovertemplate='Price Range: %{x}<br>Count: %{y}')
        brands_price_range_bar_fig.update_traces(marker_line_width=1.0,
                                                 hovertemplate = 'Market: %{customdata[0]}<br>Brand & Category: %{customdata[1]}<br>Price Point: %{x}<br>Count: %{y}<extra></extra>')
        brands_price_range_bar_fig.update_layout(barmode='group',
                                                 hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                                 font=dict(size=14, color='black')
                                                 )

        #update x axis order:
        brands_price_range_bar_fig.update_xaxes(categoryorder='array', categoryarray=custom_order)

        #Update Day Range Brands Bar chart
        brand_days_counts_filtered = filtered_data.groupby('market & category & brand').filter(lambda x: len(x) >= 10)
        brand_days_counts_filtered = brand_days_counts_filtered .groupby(['market', 'category & brand', 'market & category & brand', 'range of days']).size().reset_index(name='count')

        # Create bar chart showing count of items for each price range
        brands_days_range_bar_fig = px.bar(brand_days_counts_filtered, x='range of days', y='count',
                                    color='market',
                                    color_discrete_map=market_colors,
                                    title=f"Brands Review: Days Listed {selected_market} {', '.join(selected_categories)}",
                                    hover_data={'market': True, 'category & brand': True, 'count': True},
                                    labels={'market':'Market', 'category & brand': 'Brand & Category', 'range of days': 'Days Listed', 'count': 'Total Quantity Sold'})
        #brands_days_range_bar_fig.update_traces(hovertemplate='Days Range: %{x}<br>Count: %{y}')
        brands_days_range_bar_fig.update_traces(marker_line_width=1.0,
                                                hovertemplate = 'Market: %{customdata[0]}<br>Brand & Category: %{customdata[1]}<br>Days Listed: %{x}<br>Count: %{y}<extra></extra>')
        brands_days_range_bar_fig.update_layout(barmode='group',
                                                hoverlabel = dict(font = dict(family="Arial", size=14, color="black")),
                                                font=dict(size=14, color='black')
                                                )
        
        #update x axis order:
        brands_days_range_bar_fig.update_xaxes(categoryorder='array', categoryarray=custom_order2)

        #Sunburst Brand chart
        sunburst_brand_filtered =  filtered_data.groupby('market & category & brand').filter(lambda x: len(x) >= 10)
        #sunburst_brand_filtered =  filtered_data.groupby('market', 'category', 'brand','market & category & brand')
        
        brand_sunburst_fig = px.sunburst(sunburst_brand_filtered, path=['market', 'category', 'brand'],
                                   color='market', color_discrete_map=market_colors, 
                                   title=f"Brands Overview: {selected_market} {', '.join(selected_categories)}",
                                   width=800, height=600)
        
        #brand_sunburst_fig.update_traces(hovertemplate='<b>Market</b>: %{customdata[0]}<br><b>Brand</b>: %{label}<br><b>Count</b>: %{value}')
        brand_sunburst_fig.update_traces(hovertemplate='Info: %{id}<br>Count: %{value}<extra></extra>')
        #brand_sunburst_fig.update_layout(hoverlabel = dict(font = dict(family="Arial", size=14, color="black")))
        brand_sunburst_fig.update_layout(hoverlabel=dict(font=dict(family="Arial", size=14, color="black")),
                                         font=dict(size=14, color='black'))
    
        
    
        
        # Return the figures for all the charts in the same order as the Outputs are listed
        return (sunburst_fig, quantity_bar_fig, total_dollar_bar_fig,
                #subcategory_bar_fig, 
                price_range_bar_fig, 
                days_range_bar_fig, brands_price_range_bar_fig,brands_days_range_bar_fig, brand_sunburst_fig) #, subcategory_bar_fig, 
                # price_range_bar_fig, days_range_bar_fig)
        #       , price_range_brand_count_fig, days_range_brand_count_fig)

