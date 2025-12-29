from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import numpy as np

# initializing dash
app = Dash()

# creating app layout
app.layout = [
	html.H1(children="Visualizing LLMs", style={"textAlign": "center"}),
	dcc.Dropdown(options=np.linspace(0, 1, 6), value=1, id="dropdown-selection"),
	dcc.Graph(id="graph-content")
]

@callback(
	Output("graph-content", "figure"),
	Input("dropdown-selection", "value"),
)
def update_graph(value):
	data = np.array([20.0, 8.0, 11.0, 2.0, 18.0])/(value+0.0001)
	exponents = np.exp(data)

	probabs = exponents/exponents.sum()

	return px.bar({
		"items": np.arange(len(data)),
		"probabilities": probabs,
	}, x="items", y="probabilities")

if __name__ == "__main__":
	app.run(debug=True)