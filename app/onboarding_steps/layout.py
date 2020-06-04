import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.onboarding_steps.models import onboarding_steps_model

steps = px.bar(onboarding_steps_model.steps(), 
                     x='step', y='count', 
                     title="People waiting for next step", color="step")

layout = html.Div(children=[
    dcc.Graph(id="onboarding-steps", figure=steps),
])
