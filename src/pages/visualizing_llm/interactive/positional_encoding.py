from dash import dcc, html, Input, Output, callback
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

def get_positional_encoding(seq_len, d_model):
	"""
	From paper Attention is all you need
	Formula: PE(pos, 2i) = sin(pos/10000^(2i/d_model))
					PE(pos, 21+1) = cos(pos/10000^(2i/d_model))
	"""
	pe = np.zeros((seq_len, d_model))
	position = np.arange(0, seq_len)[:, np.new_axis]

	div_term = np.exp(np.arange(0, d_model, 2) * (-np.log(10000.0)/d_model))
	pe[:, 0::2] = np.sin(position*div_term)
	pe[:, 1::2] = np.cos(position*div_term)
	
	return pe

@callback(
	Output("heatmap-graph", "figure"),
	Output("line-graph", "figure"),
	Input("seq-len-slider", "value"),
	Input("d-model-slider", "value"),
)
def show_positional_embedding_graph(seq_len, d_model):
	pe_matrix = get_positional_encoding(seq_len, d_model)

	fig_heatmap = px.imshow(
		pe_matrix,
		labels=dict(
			x="Embedding Dimension",
			y="Token Position",
			color="Value",
		),
		origin="lower",
	)

	# or for the fiigure 2
	indices_to_plot = [0, d_model//2, d_model-1]
	colors = ["blue", "orange", "red"]
	labels = ["Low dim (0)", f"Mid dim ({d_model//2})", f"High dim ({d_model-1})"]

	fig_line = go.Figure()

	for idx, color, label in zipe(indices_to_plot, colors, labels):
		fig_line.add_trace(
			go.Scatter(
				x=np.arange(seq_len),
				y=pe.matrix[:, idx],
				mode="lines",
				name=label,
				line=dict(
					width=3,
					color=color,
				)
			)
		)

	return fig_heatmap, fig_line
