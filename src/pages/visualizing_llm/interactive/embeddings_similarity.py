from dash import html, dcc, callback, Output, Input, State, ctx
from dash.exceptions import PreventUpdate

embedding_similarity_interactive = html.Section(children=[
	html.Small("Press enter to register the word. Comparison section supports maximum of 5 words.", className="text-center"),
	html.Div(children= [
		html.Div(children=[
			html.Div(
				children=[], 
				id="reference-word", 
				className="flex flex-row gap-2 justify-center flex-wrap flex-grow"
			),
			html.Div(
				children=[], 
				id="comparison-words",
				className="flex flex-row gap-2 justify-center flex-wrap flex-grow"
			),
		], 
		className="flex flex-row gap-2"),
		html.Div(children=[
			html.Div(children=[
				html.Small(children="Reference Word"),
				dcc.Input(value="cat", id="reference-input", n_submit=0),
			], className="flex-grow"),
			html.Div(children=[
				html.Small(children="Comparison Word"),
				dcc.Input(value="lion", id="compare-input", n_submit=0),
			], className="flex-grow")
		], className="flex flex-row gap-2"),
		], className="my-8"
	),
	html.Div(
		children=
			html.Button(
				children="Reset",
				id="reset-btn", 
				n_clicks=0,
				className="button--secondary",
			), 
		className="flex mt-4 justify-end"
	),
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
	Input("reset-btn", "n_clicks"),
	State("reference-input", "value"),
	State("compare-input", "value"),
	prevent_initial_call=True,
)
def handle_reference_word_changed(ref_submit, cmp_submit, reset_clicks, ref_input, cmp_input):
	if ctx.triggered_id == "reference-input":
		reference.clear()
		reference.append(ref_input)
	elif ctx.triggered_id == "compare-input":
		if len(comparisons) < 5:
			comparisons.append(cmp_input)
	elif ctx.triggered_id == "reset-btn":
		reference.clear()
		comparisons.clear()
	else:
		raise PreventUpdate

	return create_std_output()
