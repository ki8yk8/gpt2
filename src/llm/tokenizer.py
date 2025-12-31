from transformers import AutoTokenizer

model_name = "openai-community/gpt2"
class GPTTokenizer:
	tokenizer = AutoTokenizer.from_pretrained(model_name)

	@classmethod
	def get_tokens(self, sentence):
		return self.tokenizer.tokenize(sentence)

	@classmethod
	def token2id(self, tokens):
		return self.tokenizer.convert_tokens_to_ids(tokens)
	
	@classmethod
	def id2token(self, tokens):
		return self.tokenizer.decode(tokens)
	
	@classmethod
	def batch_tokenization(self, sentences):
		return self.tokenizer(sentences)
