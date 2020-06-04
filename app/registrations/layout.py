import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.registrations.models import registration_model

figure_month = px.bar(registration_model.monthly(), 
                     x='month', y='count', title="Users per month",
                     color="gender", 
                     color_discrete_map={"Male":"blue", "Female":"red", "Unknown": "yellow"}, 
                     category_orders={"gender": ["Male", "Female", "Unknown"]})
figure_day = {}

layout = html.Div(children=[
    dcc.Graph(id="users-per-month-figure", figure=figure_month),
    dcc.Graph(id="users-per-day-figure", figure=figure_day)
])
