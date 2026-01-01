from transformers import set_seed, AutoModelForCausalLM, AutoTokenizer
import torch

# creating the seed
set_seed(0)

model_name = "openai-community/gpt2"

class GPT2Model:
	tokenizer = AutoTokenizer.from_pretrained(model_name)
	model = AutoModelForCausalLM.from_pretrained(model_name)

	@classmethod
	def complete(cls, prompt):
		inputs = cls.tokenizer(prompt, return_tensors="pt")

		with torch.no_grad():
			outputs = cls.model(**inputs)
		
		breakpoint()
		return completed