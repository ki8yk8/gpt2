from dash import html, dcc, callback, Output, Input, State, ctx
from dash.exceptions import PreventUpdate

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

reference = []
comparisons = []
def create_std_output():
	return (
		html.Span(reference[0], className="token") if len(reference) == 1 else "", 
		[html.Span(c, className="token") for c in comparisons],
	)

@callback(
	Output("reference-word", "children"),
	Output("comparison-words", "children"),
	Input("reference-input", "n_submit"),
	Input("compare-input", "n_submit"),
	State("reference-input", "value"),
	State("compare-input", "value"),
	prevent_initial_call=True,
)
def handle_reference_word_changed(ref_submit, cmp_submit, ref_input, cmp_input):
	if ctx.triggered_id == "reference-input":
		reference.clear()
		reference.append(ref_input)
		
		return create_std_output()
	elif ctx.triggered_id == "compare-input":
		if len(comparisons) >= 5:
			return create_std_output()
		
		comparisons.append(cmp_input)
		return create_std_output()
	else:
		raise PreventUpdate
