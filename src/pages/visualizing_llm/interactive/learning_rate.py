from dash import dcc, html, Input, Output, State, callback, ctx, no_update
import plotly.graph_objects as go
import numpy as np

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
			html.Button(children="Reset", id="lr-reset-btn", n_clicks=0, className="button--secondary"),
		], className="flex flex-row justify-around items-center")
	], className="w-full")
])

def loss_function(x):
	return x**2

def gradient(x):
	# derivative of loss function
	return 2*x

@callback(
	Output("loss-graph", "figure"),
	Output("history-store", "data"),
	Input("step-btn", "n_clicks"),
	Input("lr-reset-btn", "n_clicks"),
	State("lr-slider", "value"),
	State("history-store", "data"),
)
def update_training_graph(step_clicks, reset_clicks, learning_rate, history):
	if ctx.triggered_id == "lr-reset-btn":
		history = [8.0]
	elif ctx.triggered_id == "step-btn":
		current_x = history[-1]
		grad = gradient(current_x)
		new_x = current_x - (learning_rate * grad)
		history.append(new_x)
	
	x_range = np.linspace(-10, 10, 100)
	y_range = loss_function(x_range)

	fig = go.Figure()
	fig.add_trace(
		go.Scatter(
			x=x_range, y=y_range,
			mode="lines",
			name="Error Surface",
			line=dict(
				color="lightgray",
				width=2,
			)
		)
	)

	history_x = np.array(history)
	history_y = loss_function(history_x)

	fig.add_trace(
		go.Scatter(
			x=history_x,
			y=history_y,
			mode="lines+markers",
			name="Traning Path",
		)
	)

	fig.add_trace(
		go.Scatter(
			x=[history_x[-1]],
			y=[history_y[-1]],
			mode="markers",
			name="Current Weight",
		)
	)

	fig.update_layout(
		title=f"Step {len(history)-1} with Current Error: {history_y[-1]:.4f}",
		xaxis_title="Weight Parameter (x)",
		yaxis_title="Loss/Error (y)",
		xaxis=dict(range=[-10, 10]),
		yaxis=dict(range=[-10, 10])
	)

	return fig, history