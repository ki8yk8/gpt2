from transformers import set_seed, AutoModelForCausalLM, AutoTokenizer
from torch.nn.functional import softmax

# creating the seed
set_seed(0)

model_name = "openai-community/gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

inputs = tokenizer("The capital of France is", return_tensors="pt")
outputs = model(**inputs)

last_token = outputs.logits
predictions = softmax(last_token, dim=-1)

predicted_tokens = tokenizer.decode(predictions.argmax(dim=-1)[0])