# About the Project
This project will explore three different implementations of the famous LLM , GPT-2;
1. Using huggingface transformers,
2. Using PyTorch, and,
3. From scratch with just matrices.

## Why GPT-2?
1. Simple architecture for understanding,
2. 124M parameter model that can run easily without the need of dedicated GPU,
3. First of its kind so, a good start to know where thing started.

## Scripts
### 3d Token Embeddings
To visualize the embeddings space of tokens, I used GPT-2 embedding matrix to create a lookup dictionary such that whenever user enters a token they can compare the similarlity in the vector space.

Here, to visualize the things better we have also converted the 768 dimensional vector space into 3-d space using PCA. This is to create a 3d plot using plotly and show that to the user.