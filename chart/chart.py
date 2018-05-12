import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='KDE Bugtracking System – Bug List'),

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5, 6], 'y': [32], 'type': 'bar', 'name': 'kwin | wayland-'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [31], 'type': 'bar', 'name': 'plasmash | generic-'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [22], 'type': 'bar', 'name': 'plasmash | general'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [20], 'type': 'bar', 'name': 'kwin | effects-'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [17], 'type': 'bar', 'name': 'framewor | general'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [15], 'type': 'bar', 'name': 'systemse | general'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [12], 'type': 'bar', 'name': 'kwin | input'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [12], 'type': 'bar', 'name': 'kwin | core'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [10], 'type': 'bar', 'name': 'plasmash | Task Man'},
                {'x': [1, 2, 3, 4, 5, 6], 'y': [10], 'type': 'bar', 'name': 'yakuake | general'},
            ],
            'layout': {
                'title': 'Chart of quantities of repeating bugs in descending order'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
