from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

server = app.server  # importante para Gunicorn / Render

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="Demo Dash en Render"
)

app.layout = html.Div([
    html.H1("Mi aplicación Dash publicada en Render"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
