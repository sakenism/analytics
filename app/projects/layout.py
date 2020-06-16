import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.projects.models import projects_model

synchronous = px.bar(projects_model.projects("synchronous"), x='name', y='count', title="Synchronous projects")
asynchronous = px.bar(projects_model.projects("asynchronous"), x='name', y='count', title="Open projects")
enrichment = px.bar(projects_model.projects("enrichment"), x='name', y='count', title="Optional projects")

layout = html.Div(children=[
    dcc.Graph(id="projects-synchronous", figure=synchronous),
    dcc.Graph(id="projects-asynchronous", figure=asynchronous),
    dcc.Graph(id="projects-enrichment", figure=enrichment)
])
