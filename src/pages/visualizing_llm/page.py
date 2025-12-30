from dash import html
from ...markdown import markdown_to_dash

# title of the interactive blog
title = html.H1(children="Visualizing LLMs Step by Step")

# introduction to the topic
introduction = markdown_to_dash("""
This blog is an interactive blog that deeps dive into the working of transformer decoder or generative models or LLMs. For the blog we will go step by step, introducing you with the concepts of tokenization, embeddings and embedding space, and finally into attention.

The blog is designed such that you can interact with all the examples and section for ease of understanding. If you feel something is off or there was a better way of execution, feel free to raise an [issue on our GitHub repo](https://github.com/ki8yk8/gpt2). This is forcefully made longer to test the feature. Please remove this.
""")

# first markdown
tokenization_section = markdown_to_dash("""
## Tokenization
This is a section that talks about the tokenization.
""")

page = html.Main(
	children=[
		title, 
		introduction,
		tokenization_section,
	]
)