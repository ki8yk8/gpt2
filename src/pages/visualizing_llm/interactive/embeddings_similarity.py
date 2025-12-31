from dash import html, dcc, callback, Output, Input, State

embedding_similarity_interactive = html.Section(children=[
	html.P("Press enter to register the word. Comparison section supports maximum of 5 words."),
	html.Div(children=[
		html.Div(children=[], id="reference-word"),
		html.Div(children=[
			html.Small(children="Reference Word"),
			dcc.Input(value="cat", id="reference-input", n_submit=0),
		])
	]),
	html.Div(children=[
		html.Div(children=[], id="comparison-words"),
		html.Div(children=[
			html.Small(children="Comparison Word"),
			dcc.Input(value="lion", id="compare-input", n_submit=0),
		])
	]),
], className="interactive")

reference = None
comparisons = []
def create_std_output():
	return (
		html.Span(reference, className="chips") if reference else "", 
		[html.Span(c, className="chips") for c in comparisons],
	)

@callback(
	Output("reference-word", "children"),
	Output("comparison-words", "children"),
	Input("reference-input", "n_submit"),
	State("reference-input", "value"),
	prevent_initial_call=True,
)
def handle_reference_word_changed(n_submit, word):
	reference = word
	return create_std_output()

@callback(
	Output("reference-word", "children"),
	Output("comparison-words", "children"),
	Input("compare-input", "n_submit"),
	State("compare-input", "value"),
)
def handle_comaprison_word_added(n_submit, value):
	if len(comparisons) >= 5:
		return create_std_output()
	
	comparisons.append(value)
	return create_std_output()
