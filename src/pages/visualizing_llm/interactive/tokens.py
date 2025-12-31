from dash import html, dcc, Output, Input, callback, State
from ....llm import GPTTokenizer

tokenization_interactive = html.Section(
	children=[
		dcc.Input(value="Tokenizing is fun.", type="text", placeholder="Type words here and see it tokenize", id="token-input", n_submit=0),
		html.Small(children="Press enter to see the tokens", className="hint"),
		html.Div(id="token-output", className="code"),
		html.Div(children=[
			html.P(children=[
				html.Span(children="Tokens: ", className="u-bold"),
				html.Span(children="0", id="token-count")
			]),
			html.P(children=[
				html.Span(children="Words: ", className="u-bold"),
				html.Span(children="0", id="word-count")
			])
		], className="u-w-100 u-flex u-justify-between")
	],
	className="interactive"
)

@callback(
	Output("token-output", "children"),
	Output("token-count", "children"),
	Output("word-count", "children"),
	Input("token-input", "n_submit"),    # trigger
	State("token-input", "value"),    # state
	prevent_initial_call=False,
)
def tokenize_on_enter(n_submit, text):
	if not text:
		return "", "0", "0"

	# simple word wise tokenization
	tokens = GPTTokenizer.get_tokens(text)

	html_tokens_list = []
	for token in tokens:
		if token.startswith("Ġ"):
			html_tokens_list.append(
				html.Span(children=token[1:], className="token token--space")
			)
		else:
			html_tokens_list.append(
				html.Span(children=token, className="token")
			)

	return (
		html.Div(children=html_tokens_list, className="tokens_display"), 
		str(len(html_tokens_list)), 
		str(len(text.split()))
	)