from datetime import datetime, timedelta

import plotly.express as px
from dash.dependencies import Input, Output

from app.onboarding_steps_trend.models import onboarding_steps_trend_model
from app import app

@app.callback(
    Output('onboarding-step-trend', 'figure'),
    [Input('onboarding-steps-trend', 'clickData')])
def display_click_data(clickData):
    if clickData is None:
        clickData = {'points': [{'x': 'toad'}]}
    data = clickData["points"][0]
    step = data['x']
    step_data = onboarding_steps_trend_model.step(step)

    return px.bar(step_data, 
                  x='month', y='count', 
                  title=f"{step} registration")