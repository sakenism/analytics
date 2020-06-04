import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.audits.models import audit_model

figure_week = px.bar(audit_model.weekly(), 
                     x='last_day', y='count', 
                     title="Audits per week", color="grade", 
                     color_discrete_map={"1":"blue", "0":"red"}, 
                     category_orders={"grade": ["1", "0"]})
figure_day = {}

layout = html.Div(children=[
    dcc.Graph(id="per-week-figure", figure=figure_week),
    dcc.Graph(id="per-day-figure", figure=figure_day)
])
