from dash import dcc, html, Input, Output, callback
import numpy as np
import pandas as pd

positional_encoding_interactive = html.Section(children=[
	html.P("Demonstration of addition of Positional Encoding" className="text-center"),
	
	html.Div([
		html.Div([
			html.Small(children="Number of tokens", style="font-bold"),
			dcc.Slider(
				id="seq-len-slider",
				min=10,
				max=100,
				step=10,
				value=50,
				marks={
					10: "10",
					50: "50",
					100: "100",
				},
				tooltip={
					"placement": "bottom",
					"always_visible": True,s
				}
			)
		], className="w-full"),

		html.Div(children=[
			html.Small(children="Embedding Dimension", style="font-bold"),
			dcc.Slider(
				id="d-model-slider",
				min=16,
				max=128,
				step=16,
				value=64,
				marks={
					16: "16",
					64: "64",
					128: "128",
				},
				tooltip={
					"placement": "bottom",
					"always_visible": True,
				}
			)
		], className="w-full"),

		html.Div(children=[
			dcc.Graph(id="heatmap-graph", className="w-full"),
			dcc.Graph(id="line-graph", className="w-full"),
		])
	])
], className="interactive w-full")

@callback(
	Output("heatmap-graph", "figure"),
	Output("line-graph", "figure"),
	Input("seq-len-slider", "value"),
	Input("d-model-slider", "value"),
)
def show_positional_embedding_graph(seq_len, d_model):
	pass