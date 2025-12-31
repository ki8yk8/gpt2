from dash import html, dcc, Output, Input, State, callback, ctx, no_update
import plotly.express as px

from ....llm.tokenizer import GPTTokenizer
from ....llm.embeddings import Embeddings

embeddings_plot_interactive = html.Section(children=[
	html.P(children="You can try placing any number of tokens by entering it in the input field. If the word is divided into two tokens, then 0th index token will be shown in embedding space", className="text-center"),
	dcc.Graph(id="embeddings_graph"),
	html.Div(
		children=[
			dcc.Input(id="word-input", n_submit=0),
		], className="flex flex-row justify-between items-end gap-2"
	)
], className="interactive")

data = []

@callback(
	Output("embeddings_graph", "figure"),
	Input("word-input", "n_submit"),
	State("word-input", "value"),
	prevent_initial_call=True,
)
def plot_tokens_in_3d_space(word_submit, word_value):
	token_id = GPTTokenizer.get_token_ids(word_value)[0]
	embedding = Embeddings.get_embeding(token_id)

	data.append({"x": 0, "y": 0, "z": 0, "words": word_value})
	data.append({
		"x": embedding[0], "y": embedding[1], "z": embedding[2],
		"words": word_value,
	})

	fig = px.line_3d(
		data,
		x="x", y="y", z="z",
		line_group="words",
		color="words",
		title="Token Embeddings",
	)

	# adding the tips
	fig.update_traces(mode="lines+markers", marker=dict(size=4))

	axis_config = dict(
		visible=False,
		showbackground=False,
		showgrid=False,
		showticklabels=False,
	)

	fig.update_layout(
		scene=dict(
			xaxis=axis_config,
			yaxis=axis_config,
			zaxis=axis_config,
			aspectmode="cube",
		),
	)

	return fig