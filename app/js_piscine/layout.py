import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go

from app.js_piscine.models import js_piscine_model

data = js_piscine_model.steps()

print(data)

figchildren = go.Figure(data=go.Bar(x=data[0], y=data[1]))
figgrandchildren = go.Figure(data=go.Bar(x=data[3], y=data[4]))
figgrandchildrenfail = go.Figure(data=go.Bar(x=data[3], y=data[5]))

# figchildren.show()




# figure_week = px.bar(audit_model.weekly(), 
#                      x='last_day', y='count', 
#                      title="Audits per week", color="grade", 
#                      color_discrete_map={"1":"blue", "0":"red"}, 
#                      category_orders={"grade": ["1", "0"]})
# figure_day = {}

layout = html.Div(children=[
    # dcc.Graph(id="some-id", figure=figchildren),
    dcc.Graph(id="another-id", figure=figgrandchildren),
    dcc.Graph(id="anothe-id", figure=figgrandchildrenfail)
])


# figgrandchildren = go.Figure(data=go.Bar(x=bin_grandchildren_name, y=bin_grandchildren_success))
# figgrandchildren.show()
