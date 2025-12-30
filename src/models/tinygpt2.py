from transformers import AutoTokenizer, AutoModalForCausalLM

class TinyGPT2:
	def __init__(self, model_id):
		self.tokenizer = AutoTokenizer.from_pretrained(model_id)
		self.model = AutoModalForCausalLM.from_pretrained(model_id)

	def tokenize(self, sentence):
		tokens = self.tokenizer.tokenize(sentence)
		token_ids = self.tokenizer.convert_tokens_to_ids(tokens)

		return {
			"tokens": tokens,
			"input_ids": token_ids,
		}

	def predict(self, sentence):
		pass