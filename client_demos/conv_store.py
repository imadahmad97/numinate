# %%
# Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the data
df = pd.read_csv('convenience_store.csv')
split_index = len(df) // 2
df1 = df.iloc[:split_index]
df2 = df.iloc[split_index:]

# Create the Dash layout
app.layout = html.Div([
    # Dropdown for selecting the year
    dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': 'All Years', 'value': 'all'},
            {'label': '2021', 'value': '2021'},
            {'label': '2022', 'value': '2022'}
        ],
        value='all',  # default value
        style={'width': '50%'}
    ),
    # Graph placeholder
    dcc.Graph(id='sales_dashboard')
])

# Callback to update figures based on selected year
@app.callback(
    Output('sales_dashboard', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_dashboard(selected_year):
    if selected_year == '2021':
        # Use df1 for 2021 data
        data_frame = df1
        total_sales = 82241
        total_cost = 95152
        total_profit = total_sales - total_cost
    elif selected_year == '2022':
        # Use df2 for 2022 data
        data_frame = df2
        total_sales = df['store_sales(in millions)'].sum() - 82241
        total_cost = df['store_cost(in millions)'].sum() - 95152
        total_profit = total_sales - total_cost
    else:
        # Use df for all years data
        data_frame = df
        total_sales = df['store_sales(in millions)'].sum()
        total_cost = df['store_cost(in millions)'].sum()
        total_profit = total_sales - total_cost

    # Your original logic for generating figures, but using 'data_frame' which changes based on selected year
    fig = make_subplots(
        rows=4, cols=6,
        subplot_titles=("Total Sales", "Total Cost", "Profit/Loss",
                        "Sales by Food Category",
                        "Sales vs Cost by Food Department", "Monthly Sales Trend",
                        "Top 10 Promotions by Sales"),
        specs=[[{"type": "indicator", "colspan": 2}, None, {"type": "indicator", "colspan": 2}, None, {"type": "indicator", "colspan": 2}, None],
           [{"type": "bar", "colspan": 6}, None, None, None, None, None],
           [{"type": "scatter", "colspan": 3}, None, None, {"type": "scatter", "colspan": 3}, None, None],
           [{"type": "bar", "colspan": 6}, None, None, None, None, None]]
    )
    
    # Add plots
    fig.add_trace(
        go.Indicator(
            mode="number",
            value=total_sales,
            number={"prefix": "$", "valueformat": ".2f", "font": {"color": "green"}}
        ),
        row=1, col=1
    )
    fig.add_trace(
        go.Indicator(
            mode="number",
            value=total_cost,
            number={"prefix": "$", "valueformat": ".2f", "font": {"color": "red"}}
        ),
        row=1, col=3
    )
    fig.add_trace(
        go.Indicator(
            mode="delta",
            delta={'reference': 0},
            value=total_profit,
            number={"prefix": "$", "valueformat": ".2f"}
        ),
        row=1, col=5
    )
    
    # Sales by Food Category
    sales_by_category = data_frame.groupby('food_category')['store_sales(in millions)'].sum().sort_values(ascending=False)
    fig.add_trace(
        go.Bar(x=sales_by_category.index, y=sales_by_category.values, name='Sales by Category'),
        row=2, col=1
    )

    # Sales vs Cost by Food Department
    sales_by_department = data_frame.groupby('food_department')['store_sales(in millions)'].sum()
    cost_by_department = data_frame.groupby('food_department')['store_cost(in millions)'].sum()
    fig.add_trace(
        go.Scatter(x=sales_by_department.index, y=sales_by_department.values, mode='markers', name='Sales'),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x=cost_by_department.index, y=cost_by_department.values, mode='markers', name='Cost'),
        row=3, col=1
    )

    # Monthly Sales Trend (Placeholder logic, you can replace it with actual data)
    monthly_sales = pd.Series([total_sales * i * 0.01 for i in range(1, 13)], index=[f'Month {i}' for i in range(1, 13)])
    fig.add_trace(
        go.Scatter(x=monthly_sales.index, y=monthly_sales.values, mode='lines+markers', name='Monthly Sales'),
        row=3, col=4
    )

    # Top 10 Promotions by Sales
    top_promotions = data_frame.groupby('promotion_name')['store_sales(in millions)'].sum().sort_values(ascending=False).head(10)
    fig.add_trace(
        go.Bar(x=top_promotions.index, y=top_promotions.values, name='Top Promotions'),
        row=4, col=1
    )

    # Update layout
    fig.update_layout(
        title="Sales Dashboard",
        height=1200,  # You can adjust this value
        width=2400,   # You can adjust this value
        showlegend=False
    )
    fig.update_xaxes(tickangle=45)

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)


