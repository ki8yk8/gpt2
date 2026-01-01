from dash import html
from ...markdown import markdown_to_dash
from .interactive.tokens import tokenization_interactive
from .interactive.embeddings_similarity import embedding_similarity_interactive
from .interactive.embeddings_plot import embeddings_plot_interactive
# from .interactive.autoregressive import autoregressive_interactive
from .interactive.temperature import temperature_interactive
from .interactive.positional_encoding import positional_encoding_interactive
from .interactive.learning_rate import learning_rate_ineractive

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

auto_regressive_interactive_disabled = markdown_to_dash("""
The autoregressive interactive has been disabled because even GPT2 model didn't ran on my local machine and I wasn't able to debug the workflow without waiting for like 20 minutes for just a single token.
""")

what_is_attention = markdown_to_dash("""
## Attention in Transformer
This part won't be deep diving into the technical details, but we will focus on intution behind the attention. For a given set on input tokens, the task of LLM is to generate next token. Generally, the new token is something that is contextually and factually correct.

This contextual awareness comes from attention. While generating new token, model passes the information of each token with each other to enrich themselves. Example; "Money can be deposited at bank" and "I am fishing from the river bank", in both sentence the word "bank" is same but their meaning is different based on the context. But, if you recall, we know that the LLM only has one vector for each token so, to handle such situation all the tokens passes each other's information and update themselves so that they can differentiate if they are in the bank or river bank.

For this attention comes into play. In attention, you get the value of dependency like how much is my first token dependent on second and so on. And in this way you predict how much the new token should depend on all the other tokens. This dependency is computed, and based on it new vectors are formed and a new token in generated.

Example; in the sentence "The capital of Nepal is" the attention realizes that for generating new token "capital" and "nepal" are much more important. So, it computes new_token as weighted sum of "captial" and "sum" and the weights are determined by attention.
""")

what_is_lmhead = markdown_to_dash("""
## LM Head
The final output after attention decoder stack is a n-dimensional vector in our case 768. The 768 dimensional vector now should be converted back to a token. For this in LLM there is something known as LM head.

The LM head receives a 768-d vector projects the vector into the vocabulary space i.e around 50,000 dimension vector then, applies softmax such that the we obtain a probability distribution over all the words in vocabulary.

Then, the distribution is sampled to get a result which is the next token.
""")

concept_of_temperature = markdown_to_dash("""
## Temperature
A mathematical function is determinstic i.e. for a given set of same input the output is always constant. And this is almost similar in LLM too. For a given set of input tokens, the set of output tokens are almost deterministic, and to control this there is a knob of temperature.

The temperature helps to redistribute the probability across the vocabulary space to make distribution uniform. This uniformity is responsible for generating something that seems random each time the model processes the same input.

The value of temperature is between 0 and Infinity. Value of 0 means the probabiilty of highest token will be near to 1 making the LLM completely deterministic while a higher temperature will distribute the probability more uniformly. This can be realized from the interactive below.
""")

appendix = markdown_to_dash("# Appendix")

appendix_positional_encoding = markdown_to_dash("""
## Positional Encoding
A transformer achitecture is parallel i.e. for a given sentence it processes all words at same time. And this is problem in LLM because it loses the infromation of order. For a model without this, "Dog bites Man" is almost similar to "Man bites Dog" and to fix this there is concept of positional encoding.

The positional encoding helps to inject a unique signal into the word embeddings to defint sequence. It uses sine and cosine functions of different frequency. This pattern is responsible for giving a unique identity to every position so model knows what is first and what is last.

The value is calculated using math formula and added to the token. A low frequency wave changes slowly while high frequency changes fast. This unique combination makes sure every position has different values. This can be realized from the interactive below.
""")

appendix_learning = markdown_to_dash("""
# How Learning Works?
A model training is iterative process i.e. it improves step by step. And this is fundaemntal in LLM training too. At start, the model is dumb with high error, and to fix there is concept of gradient descent.

The learning rate helps to decide how much to change the weights to reduce the error. This rate is responsible for how fast model learns.

The value is hyperparameter. Value of too low means the model will take forever to learn while a high learning rate will make training unstable and error will explode. This can be realized from the interactive below.
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
		# autoregressive_interactive,
		what_is_attention,
		concept_of_temperature,
		temperature_interactive,
		appendix,
		appendix_positional_encoding,
		positional_encoding_interactive,
		appendix_learning,
		learning_rate_ineractive
	]
)