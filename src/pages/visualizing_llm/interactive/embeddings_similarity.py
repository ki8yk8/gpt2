from dash import html, dcc, callback, Output, Input, State

embedding_similarity_interactive = html.section(children=[
	html.Div(children=[
		html.Div(children=[], id="reference-word"),
		html.Div(children=[
			html.Small(children="Reference Word"),
			dcc.Input(value="cat", id="reference-input"),
		])
	]),
	html.Div(children=[
		html.Div(children=[], id="against-words"),
		html.Div(children=[
			html.Small(children="Supports multiple values"),
			dcc.Input(value="cat", id="compare-input"),
		])
	]),
],className="interactive")