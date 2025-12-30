from dash import html
from ...markdown import markdown_to_dash

# title of the interactive blog
title = html.H1(children="Visualizing LLMs Step by Step")

# introduction to the topic
introduction = markdown_to_dash("""
This blog is an interactive blog that deeps dive into the working of transformer decoder or generative models or LLMs. For the blog we will go step by step, 
- introducing you with the concepts of tokenization, 
- embeddings and embedding space, and,
- finally into attention.

The blog is designed such that you can interact with all the examples and section for ease of understanding. If you feel something is off or there was a better way of execution, feel free to raise an [issue on our GitHub repo](https://github.com/ki8yk8/gpt2).
""")

# first markdown
tokenization_section = markdown_to_dash("""
## Tokenization
An LLM can be thought of as a mathematical tool that uses some clever mathematics to find the semantic of an incomplete sentence and generate the next probable word. So, as any mathematical tool LLM understands numbers but the input are words.

To solve this issue, we use tokenization. Tokenization is the process to convert a given sentence into tokens. A token are atomic component of sentences for that LLM. It can be a word (Eg: run) or it can be prefix or suffix of word (Eg: un).

You can use the interactive menu below, type your sentence and see how tokens are formed.
""")

page = html.Main(
	children=[
		title, 
		introduction,
		tokenization_section,
	]
)