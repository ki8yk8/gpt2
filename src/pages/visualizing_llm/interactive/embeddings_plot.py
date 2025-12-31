from dash import html, dcc, Output, Input, State, callback, ctx, no_update
import plotly.express as px

from ....llm.tokenizer import GPTTokenizer
from ....llm.embeddings import Embeddings

embeddings_plot_interactive = html.Section(children=[
	dcc.Graph(id="embeddings_graph"),
	html.Div(
		children=[
			dcc.Input(id="red-input", n_submit=0),
			dcc.Input(id="blue-input", n_submit=0),
		], className="flex flex-row justify-between items-end gap-2"
	)
], className="interactive")

red_vector = []
blue_vector = []

@callback(
	Output("embeddings_graph", "figure"),
	Input("red-input", "n_submit"),
	Input("blue-input", "n_submit"),
	State("red-input", "value"),
	State("blue-input", "value"),
)
def plot_tokens_in_3d_space(red_submit, blue_submit, red_value, blue_value):
	if ctx.triggered_id == "red-input":
		red_vector.clear()
		token_id = GPTTokenizer.get_token_ids(red_value)[0]
		red_vector.append(Embeddings.get_embeding(token_id))
	elif ctx.triggered_id == "blue-input":
		blue_vector.clear()
		token_id = GPTTokenizer.get_token_ids(blue_value)[0]
		blue_vector.append(Embeddings.get_embeding(token_id))

	if len(red_vector) > 0 and len(blue_vector) > 0:
		origin = [0, 0, 0]
		[rx, ry, rz] = red_vector[0]
		[bx, by, bz] = blue_vector[0]
		breakpoint()

		data = [
			{"x": 0, "y": 0, "z": 0, "vector": "red"},
			{"x": rx, "y": ry, "z": rz, "vector": "red"},
			{"x": 0, "y": 0, "z": 0, "vector": "blue"},
			{"x": bx, "y": by, "z": bz, "vector": "blue"},
		]

		fig = px.line_3d(
			data,
			x="x", y="y", z="z",
			line_group="vector",
			color="vector",
			title="Token Embeddings",
		)

		# adding the tips
		fig.update_traces(mode="lines+markers", marker=dict(size=4))

		return fig
	else:
		return no_update