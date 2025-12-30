from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import numpy as np

from src.markdown import markdown_to_dash

# initializing dash
app = Dash()

# first markdown
tokenization_section = markdown_to_dash("""
## Tokenization
This is a section that talks about the tokenization.
""")

# creating app layout
app.layout = html.Div(
	className="dash-container",
	children= [
		html.H1(children="Visualizing LLMs this is a long text for the try"),
		html.Section(children=tokenization_section),
	]
)

if __name__ == "__main__":
	app.run(debug=True)