from datetime import datetime, timedelta
from dateutil import relativedelta

import plotly.express as px
from dash.dependencies import Input, Output

from app.registrations.models import registration_model
from app import app


@app.callback(
    Output('users-per-day-figure', 'figure'),
    [Input('users-per-month-figure', 'clickData')])
def display_click_data(clickData):
    if clickData is None:
        clickData = {'points': [{'curveNumber': 0, 'pointNumber': 2, 'pointIndex': 2, 'x': '2019-07-01', 'y': 1989, 'label': '2019-07-01', 'value': 1989}]}
    data = clickData["points"][0]
    month = data['x']
    start_dt = datetime.strptime(month+"T00:00:00+0600", "%Y-%m-%dT%H:%M:%S%z")
    end_dt = start_dt + relativedelta.relativedelta(months=1)

    start_str = datetime.strftime(start_dt, "%Y-%m-%dT%H:%M:%S%z")
    end_str = datetime.strftime(end_dt, "%Y-%m-%dT%H:%M:%S%z")

    start_beauty = datetime.strftime(start_dt, "%d %b %Y")
    end_beauty = datetime.strftime(end_dt, "%d %b %Y")

    per_day_data = registration_model.daily(start_str, end_str)
    return px.bar(per_day_data, 
                  x='day', y='count', 
                  title=f"Users {start_beauty} - {end_beauty}",
                  color="gender", 
                  color_discrete_map={"Male":"blue", "Female":"red", "Unknown": "yellow"}, 
                  category_orders={"gender": ["Male", "Female", "Unknown"]})
