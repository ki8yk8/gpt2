from ....llm.model import GPT2Model
from dash import html, dcc, Input, callback, State, Output, ctx, noupdate

autoregressive_interactive = html.Section(children=[
	html.P(children="Type your prompt and press enter. Then, press next button to see how the model is predicting next word. The next button will work until <EOS> token is received.", className="text-center")
	html.Div(id="tokens-output", children="", className="my-4"),
	html.Div(children=[
		dcc.Input(id="prompt-input", n_submit=0),
		html.Button(
			id="next-token",
			className="button button--primary",,
			n_clicks=0,
			children="Next Token",
		),
		html.Button(
			children="Reset",
			id="reset-button",
			className="button button--secondary",
			n_clicks="0",
		),
	], className="flex flex-row gap-2 justify-center items-center")
], className="interactive")

prompt_with_response = []

@callback(
	Output("tokens-output", "children"),
	Output("prompt-input", "value"),
	Input("prompt-input", "n_submit"),
	Input("next-token", "n_clicks"),
	Input("reset-button", "n_clicks"),
	State("prompt-input", "value"),
)
def generate_autoregressively(prompt_submit, next_submit, reset_submit, prompt):
	if ctx.triggered_id == "prompt-input":
		GPT2Model.complete(prompt)
	elif ctx.triggered_id == "next-token":
		pass
	elif ctx.triggered_id == "reset-button":
		pass

	return noupdate, noupdate