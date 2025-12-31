from dash import html, dcc, callback, Output, Input, State, ctx
from dash.exceptions import PreventUpdate

from ....llm.tokenizer import GPTTokenizer
from ....llm.embeddings import Embeddings

embedding_similarity_interactive = html.Section(children=[
	html.Small("Press enter to register the word. Comparison section supports maximum of 5 words.", className="text-center"),
	html.Div(children= [
		html.Div(children=[
			html.Div(
				children=[], 
				id="reference-word", 
				className="flex flex-row gap-2 justify-center flex-wrap flex-grow items-center"
			),
			html.Div(
				children=[], 
				id="comparison-words",
				className="flex flex-row gap-2 justify-center flex-wrap flex-grow items-center"
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
	chips_classes = "rounded text-white py-1 px-2 m-0"
	return (
		html.P(reference[0]["token"], className=f"{chips_classes} bg-primary") if len(reference) == 1 else "", 
		[html.Div(children=[
			html.P(c["token"], className="m-0"),
			html.Small(c["similarity"]),
		], className=f"{chips_classes} bg-black flex flex-col justify-center items-center") for c in comparisons],
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
		input_token_id = GPTTokenizer.get_token_ids(ref_input)
		if len(input_token_id) > 1:
			return create_std_output()
		
		reference.clear()

		for i, c in enumerate(comparisons):
			similarity = Embeddings.compute_cosine_similarity(input_token_id[0], c["token_id"])
			comparisons[i]["similarity"] = f"{similarity:.3f}"

		reference.append({
			"token": ref_input,
			"token_id": input_token_id[0],
		})
	elif ctx.triggered_id == "compare-input":
		input_token_id = GPTTokenizer.get_token_ids(cmp_input)
		if len(input_token_id) > 1:
			return create_std_output()
		
		if len(comparisons) < 5:
			similarity = Embeddings.compute_cosine_similarity(input_token_id[0], reference[0]["token_id"]) if len(reference) > 0 else 0

			comparisons.append({
				"token": cmp_input,
				"token_id": input_token_id[0],
				"similarity": f"{similarity:.3f}",
			})
	elif ctx.triggered_id == "reset-btn":
		reference.clear()
		comparisons.clear()
	else:
		raise PreventUpdate

	return create_std_output()
