from dash import html
from ...markdown import markdown_to_dash
from .interactive.tokens import tokenization_interactive
from .interactive.embeddings_similarity import embedding_similarity_interactive
from .interactive.embeddings_plot import embeddings_plot_interactive
from .interactive.autoregressive import autoregressive_interactive

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

tokenization_section = markdown_to_dash("""
## Tokenization
An LLM can be thought of as a mathematical tool that uses some clever mathematics to find the semantic of an incomplete sentence and generate the next probable word. So, as any mathematical tool LLM understands numbers but the input are words.

To solve this issue, we use tokenization. Tokenization is the process to convert a given sentence into tokens. A token are atomic component of sentences for that LLM. It can be a word (Eg: run) or it can be prefix or suffix of word (Eg: un).

You can use the interactive menu below, type your sentence and see how tokens are formed.
""")

embedding_section = markdown_to_dash("""
## Embeddings
LLM doesn't understands word but they need numbers to operate. So, the question arises how can one convert the discrete tokens into their numerical representation.

Here, embeddings come into the play. For each token, the LLM (here, GPT 2) has a n-dimensional vector reprsentation for each token. The vector peserves the semantic representation of each token such that, two vectors like "cat" and "lion" that are similar are closer in the embedding space than the token "potato".
""")

embedding_depth_section = markdown_to_dash("""
Each n-dimensional vector corresponding a token represents that vector in the embedding space. Each dimension is assume to hold one property might be emotion, color, type, living or non-living, etc. Such that this results in the similar tokens to be pointing towards same direction in the embedding space.

For an illustration, the 768-dimensional vector of GPT-2 has been reduced to 3-d using Principal Component Analysis. This might introduce some noise because information are compresssed so, errors like two similar tokens might be placed apart from each other while dissimilar can be placed together.

Also, a word is sometime divided into multiple token example; lion is divided as l+ion. For the sake of demonstration, we have only considered the zeroth index token so, please try to add words with single token in the illustration graph. The tokens can be found from the first interactive, tokenization.
""")

introduction_to_autoregression = markdown_to_dash("""
## LLM
Now, let's look at what LLM is. LLM stands for Large Langauge Model and it is an autoregressive generative model for generating text.

Let's focus on the word autoregressive. An LLM can be considered as a function that predicts the new token based on a set of tokens. i.e. when you give a prompt to the LLM, it's task is to complete the prompt token by token. It does so until a special token End of Sequence is received. 
""")


page = html.Main(
	children=[
		title, 
		introduction,
		tokenization_section,
		tokenization_interactive,
		embedding_section,
		embedding_similarity_interactive,
		embedding_depth_section,
		embeddings_plot_interactive,
		introduction_to_autoregression,
		autoregressive_interactive,
	]
)