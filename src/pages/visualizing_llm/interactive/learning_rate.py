from dash import dcc, html, Input, Output, State, callback, ctx, no_update

learning_rate_ineractive = html.Div(children=[
	html.P(children="Click 'Train Step' to move the ball down the hill (minimize the error)", className="font-center"),

	html.Div(children=[
		html.Div([
			html.Small(children="Learning Rate", className="font-bold"),
			dcc.Slider(
				id="lr-slider",
				min=0.05,
				max=1.2,
				step=0.05,
				value=0.1,
				marks={
					0.1: "0.1 (slow)",
					0.9: "0.9 (fast)",
					1.1: "1.1 (overshoot)",
				}
			)
		], className="w-full"),

		dcc.Graph(id="loss-graph"),
		dcc.Store(id="history-store", data=[8.0]),

		html.Div(children=[
			html.Button(children="Train 1 step", id="step-btn", n_clicks=0, className="button--primary"),
			html.Button(children="Reset", id="reset-btn", n_clicks=0, className="button--secondary"),
		], className="flex flex-row justify-around items-center")
	], className="w-full")
])

@callback(
	Output("loss-graph", "figure"),
	Output("history-store", "data"),
	Input("step-btn", "n_clicks"),
	Input("reset-btn", "n_clicks"),
	State("lr-slider", "value"),
	State("history-store", "data"),
)
def update_training_graph(step_clicks, reset_clicks, learning_rate, history):
	if ctx.triggered_id == "reset-btn":
		history = [8.0]
	elif ctx.triggered_id == "step-btn":
		current_x = history[-1]
		pass
	
	x_range = np.linspace(-10, 10, 100)
	y_range = None

	return no_update