import torch
from transformers import pipeline

def generate(prompt="The capital city of USA is"):
	# creating the generator using pipeline
	generator = pipeline("text-generation", model="openai-community/gpt2")

	# using generator to generate responses
	output = generator(prompt, max_new_tokens=32)

	return {
		"response": output[0]["generated_text"],
	}
