import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.onboarding_steps_trend.models import onboarding_steps_trend_model

steps = px.bar(onboarding_steps_trend_model.steps(), 
                     x='step', y='count', 
                     title="People passed the step", color="step")
step = {}

layout = html.Div(children=[
    dcc.Graph(id="onboarding-steps-trend", figure=steps),
    dcc.Graph(id="onboarding-step-trend", figure=step),
])
