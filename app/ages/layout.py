import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from app.ages.models import ages_model

# ages = px.bar(ages_model.ages(), 
#                      x='date_of_birth', y='count', 
#                      title="Users age",
#                      color="gender", 
#                      color_discrete_map={"Male":"blue", "Female":"red", "Unknown": "yellow"}, 
#                      category_orders={"gender": ["Male", "Female", "Unknown"]})
# ages = px.pie(ages_model.ages(), 
#                 names='date_of_birth', values='count', 
#                 title="Users age")
ages = px.sunburst(ages_model.ages(), 
                path=['date_of_birth', 'gender'], values='count',
                title="Users age")

layout = html.Div(children=[
    dcc.Graph(id="date-of-birth", figure=ages),
])
