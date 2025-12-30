from transformers import AutoTokenizer

model_name = "openai-community/gpt2"

# initializing tokenizer for GPT-2
tokenizer = AutoTokenizer.from_pretrained(model_name)

# simple tokenizer usage
tokenizer_op = tokenizer("The capital city of France is")
print(tokenizer_op["input_ids"])
print(tokenizer_op["attention_mask"])

# get an array of tokens
tokens = tokenizer.tokenize("The capital city of France is")

# get an array of token ids
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)

# decoding token ids
decoded_string = tokenizer.decode(ids)
print(decoded_string)

# batching sequences; for returning pytroch tensor instead of tensor use return_tensors="pt"
batch_tokeizer_op = tokenizer([
	"This is the first word",
	"This is the second word",
], return_tensors="pt")