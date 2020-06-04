from datetime import datetime, timedelta

import plotly.express as px
from dash.dependencies import Input, Output

from app.audits.models import audit_model
from app import app


@app.callback(
    Output('per-day-figure', 'figure'),
    [Input('per-week-figure', 'clickData')])
def display_click_data(clickData):
    if clickData is None:
        clickData = {'points': [{'curveNumber': 0, 'pointNumber': 0, 'pointIndex': 0, 'x': '2020-01-12', 'y': 36, 'label': '2020-01-12', 'value': 36}]}
    data = clickData["points"][0]
    last_day = data['x']
    end_dt = datetime.strptime(last_day+"T23:59:59+0600", "%Y-%m-%dT%H:%M:%S%z")
    start_dt = end_dt-timedelta(days=7)

    start_str = datetime.strftime(start_dt, "%Y-%m-%dT%H:%M:%S%z")
    end_str = datetime.strftime(end_dt, "%Y-%m-%dT%H:%M:%S%z")

    start_beauty = datetime.strftime(start_dt, "%d %b %Y")
    end_beauty = datetime.strftime(end_dt, "%d %b %Y")

    per_day_data = audit_model.daily(start_str, end_str)
    return px.bar(per_day_data, 
                  x='day', y='count', 
                  title=f"Audits {start_beauty} - {end_beauty}", color="grade",
                  color_discrete_map={"1":"blue", "0":"red"},
                  category_orders={"grade": ["1", "0"]})
