from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import numpy as np

from src.pages.visualizing_llm import page as visualizing_llm_page

print(visualizing_llm_page)

# initializing dash
app = Dash()

# setting the title for app
app.title = "Visualizing LLM Step by Step"

# creating app layout
app.layout = html.Div(
	className="dash-container",
	children= [
		visualizing_llm_page,
	]
)

if __name__ == "__main__":
	app.run(debug=True)