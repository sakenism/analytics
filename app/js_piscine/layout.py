import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go

from app.js_piscine.models import js_piscine_model

data = js_piscine_model.steps()

firstEnd = 45
secondEnd = 78

fig_first = go.Figure(data=[
	go.Bar(name='Success', x=data[0][:firstEnd], y=data[1][:firstEnd]),
	go.Bar(name='Fail', x=data[0][:firstEnd], y=data[2][:firstEnd])
])

fig_second = go.Figure(data=[
	go.Bar(name='Success', x=data[0][firstEnd:secondEnd], y=data[1][firstEnd:secondEnd]),
	go.Bar(name='Fail', x=data[0][firstEnd:secondEnd], y=data[2][firstEnd:secondEnd])
])

fig_third = go.Figure(data=[
	go.Bar(name='Success', x=data[0][secondEnd:], y=data[1][secondEnd:]),
	go.Bar(name='Fail', x=data[0][secondEnd:], y=data[2][secondEnd:])
])

fig_first.update_layout(title_text='JS piscine FIRST week quests', barmode='stack')
fig_second.update_layout(title_text='JS piscine SECOND week quests', barmode='stack')
fig_third.update_layout(title_text='JS piscine THIRD week quests', barmode='stack')

layout = html.Div(children=[
	dcc.Graph(id="js-first-week-quests", figure=fig_first),
	dcc.Graph(id="js-second-week-quests", figure=fig_second),
	dcc.Graph(id="js-third-week-quests", figure=fig_third)
])
