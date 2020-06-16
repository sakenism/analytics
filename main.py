import dash_html_components as html

from app import app, server
from app.audits import callback
from app.registrations import callback
from app.onboarding_steps_trend import callback
from app.audits import layout as audits_layout
from app.registrations import layout as registrations_layout
from app.onboarding_steps import layout as onboarding_steps_layout
from app.onboarding_steps_trend import layout as onboarding_steps_trend_layout
from app.ages import layout as ages_layout
from app.gender import layout as gender_layout
from app.source_channels import layout as source_channels_layout
from app.languages import layout as languages_layout
from app.projects import layout as projects_layout


app.layout = html.Div(children=[
    html.H1(children='01 Platform analytics'),

    html.Div([
        onboarding_steps_layout.layout
    ], className="row"),

    html.Div([
        html.Div([
            audits_layout.layout,
        ], className="six columns"),

        html.Div([
            registrations_layout.layout
        ], className="six columns"),

    ], className="row"),


    html.Div([
        html.Div([
            ages_layout.layout,
        ], className="six columns"),

        html.Div([
            gender_layout.layout
        ], className="six columns"),

    ], className="row"),

    html.Div([
        html.Div([
            source_channels_layout.layout
        ], className="six columns"),

        html.Div([
            languages_layout.layout
        ], className="six columns"),

    ], className="row"),

    html.Div([
        html.Div([
            onboarding_steps_trend_layout.layout
        ], className="six columns"),

        html.Div([
            projects_layout.layout
        ], className="six columns"),

    ], className="row"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
