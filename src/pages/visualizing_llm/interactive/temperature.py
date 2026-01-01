from dash import html, dcc, Output, Input, callback, no_update
import numpy as np
import plotly.express as px
import pandas as pd

TOKENS = ["apple", "banana", "cherry", "date", "orange", "fig", "grape"]
LOGITS = np.array([2.0, 1.5, 3.5, 0.5, 1.0, 0.2, 1.8])

temperature_interactive = html.Section(children=[
	html.P("Adjust the Temperature to see how it flattens or sharpens the proability distribution.", className="text-center"),
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
		dcc.Graph(id="prob-dist-graph", style={"width": "100%"}),
		dcc.Graph(id="sampling-graph", style={"width": "100%"}),
	], className="w-full")
], className="interactive")

def softmax_with_temperature(logits, temperature):
	scaled_logits = logits/temperature
	exp_values = np.exp(scaled_logits)
	probs = exp_values/np.sum(exp_values)

	return probs

@callback(
	Output("prob-dist-graph", "figure"),
	Output("sampling-graph", "figure"),
	Input("temp-slider", "value"),
)
def create_or_update_graphs(temperature):
	probs = softmax_with_temperature(LOGITS, temperature)
	data = pd.DataFrame({
		"Token": TOKENS,
		"Probability": probs,
	})

	# drawing the figure 1
	fig_prob = px.bar(
		data,
		x="Token",
		y="Probability",
		title=f"Probability Distribution at T={temperature}",
	)

	# sampling and having the distribution curve of the token
	samples = np.random.choice(TOKENS, size=100, p=probs)
	unique, counts = np.unique(samples, return_counts=True)

	data = {token: 0 for token in TOKENS}
	for token, count in zip(unique, counts):
		data[token] = count

	df_sample = pd.DataFrame({
		"Token": TOKENS,
		"Count": [data[t] for t in TOKENS],
	})

	fig_sample = px.bar(
		df_sample,
		x="Token",
		y="Count",
		title="Actual Samples (n=100)",
		text_auto=True,
	)

	return fig_prob, fig_sample
	