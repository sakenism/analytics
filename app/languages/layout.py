import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.languages.models import languages_model

languages = px.pie(languages_model.languages(), 
                names='language', values='count',
                title="User Languages")

layout = html.Div(children=[
    dcc.Graph(id="languages", figure=languages),
])
