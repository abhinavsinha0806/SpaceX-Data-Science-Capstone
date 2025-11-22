# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
a
# Read the airline data into pandas dataframe directly from the URL
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create the dropdown options list dynamically
launch_sites = spacex_df['Launch Site'].unique()
options_list = [{'label': 'All Sites', 'value': 'ALL'}]
for site in launch_sites:
    options_list.append({'label': site, 'value': site})

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a Launch Site Drop-down Input Component
    dcc.Dropdown(
        id='site-dropdown',
        options=options_list,
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    
    html.Br(),

    # TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a Range Slider to Select Payload
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    # TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Callback function for the Pie Chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # If ALL sites selected, show contribution of each site to total successes
        fig = px.pie(
            spacex_df, 
            values='class', 
            names='Launch Site', 
            title='Total Success Launches By Site'
        )
        return fig
    else:
        # If specific site selected, show Success (1) vs Failure (0) count
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Group by class to count success (1) and failure (0)
        site_counts = filtered_df['class'].value_counts().reset_index()
        site_counts.columns = ['class', 'count']
        fig = px.pie(
            site_counts, 
            values='count', 
            names='class', 
            title=f'Total Success Launches for site {entered_site}'
        )
        return fig

# TASK 4: Callback function for the Scatter Chart
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    # Filter data based on slider range first
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if entered_site == 'ALL':
        # Render scatter plot for all sites
        fig = px.scatter(
            filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version Category',
            title='Correlation between Payload and Success for all Sites'
        )
        return fig
    else:
        # Filter for the specific site
        site_filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        # Render scatter plot for specific site
        fig = px.scatter(
            site_filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for {entered_site}'
        )
        return fig

# Run the app
if __name__ == '__main__':
    # Updated from app.run_server() to app.run() to fix ObsoleteAttributeException
    app.run(debug=True)