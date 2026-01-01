from dash import html, dcc, Output, Input, callback, no_update
import numpy as np

TOKENS = ["apple", "banana", "cherry", "date", "orange", "fig", "grape"]
LOGITS = np.array([2.0, 1.5, 3.5, 0.5, 1.0, 0.2, 1.8])

temperature_intearctive = html.Section(children=[
	html.P("Adjust the Temperature to see how it flattens or sharpens the proability distribution." className="text-center"),
	html.Div(children=[
		dcc.Slider(
			id="temp-slider",
			min=0.1,
			max=5.0,
			step=0.1,
			value=1.0,
			marks={
				0.1: "0.1 (cold)",
				1: "1.0 (normal)",
				5: "5.0 (hot)",
			},
			tooltip={
				"placement": "bottom", 
				"always_visible": True
			},
		),
		html.Button("Sample 100 Times", id="sample-btn", n_clicks=0),
		dcc.Graph(id="prob-dist-graph"),
		dcc.Graph(id="sampling-graph"),
	], className="")
], className="interactive")

def softmax_with_temperature(logits, temperature):
	scaled_logits = logits/temperature
	exp_values = np.exp(scaled_logits)
	probs = exp_values/np.sum(exp_values)

	return probs

@app.callback(
	Output("prob-dist-graph", "figure"),
	Output("sampling-graph", "figure"),
	Input("temp-slider", "value"),
	Input("sample-btn", "n_clicks"),
)
def create_or_update_graphs(temperature, sample_clicks):
	return no_update