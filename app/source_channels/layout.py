import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.source_channels.models import source_channels_model

sources = px.pie(source_channels_model.source_channels(), 
                names='source', values='count',
                title="Source channels")

layout = html.Div(children=[
    dcc.Graph(id="source-channels", figure=sources),
])
