from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import numpy as np

# initializing dash
app = Dash()

# creating app layout
app.layout = [
	html.H1(children="Visualizing LLMs this is a long text for the try"),
	html.H2(children="This the H2 tag"),
	html.P(children="This is a paragraph that is immediately followed by the H1. THis is an example of me trying to create the best style for my system."),
	dcc.Graph(id="graph-content"),
	dcc.Slider(
		min=0.1, 
		max=2, 
		step=0.1, 
		marks={
			0.1: "0",
			0.5: "0.5",
			1: "1",
			2: "2"
		}, 
		tooltip = {
			"placement": "bottom",
			"always_visible": True,
		},
		value=1, 
		id="temperature-slider"
	),
]

@callback(
	Output("graph-content", "figure"),
	Input("temperature-slider", "value"),
)
def update_graph(value):
	data = np.array([20.0, 8.0, 11.0, 2.0, 18.0])/(value+0.0001)
	exponents = np.exp(data)

	probabs = exponents/exponents.sum()

	fig = px.bar(
		{
			"items": np.arange(len(data)),
			"probabilities": probabs,
		}, 
		x="items", 
		y="probabilities"
	)

	fig.update_yaxes(
		range=[0, 1.2],
		title="Probability",
	)

	fig.update_xaxes(title="Items")

	fig.update_layout(
		title=f"Softmax with temperature {value:.1f}",
		title_x=0.5,
		bargap=0.25,
	)

	return fig

if __name__ == "__main__":
	app.run(debug=True)