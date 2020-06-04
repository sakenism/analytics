import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.gender.models import gender_model

gender = px.pie(gender_model.gender(), 
                     names='gender', values='count', 
                     title="Users gender",
                     color_discrete_map={"Male":"blue", "Female":"red", "Unknown": "yellow"})

layout = html.Div(children=[
    dcc.Graph(id="gender", figure=gender),
])
