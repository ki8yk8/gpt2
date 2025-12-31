from transformers import AutoTokenizer

model_name = "openai-community/gpt2"
class GPTTokenizer:
	tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

	@classmethod
	def get_tokens(cls, sentence):
		return cls.tokenizer.tokenize(sentence)

	@classmethod
	def token2id(cls, tokens):
		return cls.tokenizer.convert_tokens_to_ids(tokens)
	
	@classmethod
	def id2token(cls, ids):
		return cls.tokenizer.convert_ids_to_tokens(ids)
	
	@classmethod
	def batch_tokenization(cls, sentences):
		return cls.tokenizer(sentences)
