"""
Creates a lookup dictionary with representation of every token in 3d space.
"""
from transformers import AutoModel
import json
from sklearn.decomposition import PCA

model_name = "openai-community/gpt2"
model = AutoModel.from_pretrained(model_name)

# returns tensor of shape (50257, 768) => (N_vocab, embedding dimension)
embedding_matrix = model.get_input_embeddings().weight
embedding_matrix = embedding_matrix.detach().cpu().numpy().tolist()

# saving the embedding matrix by forming a dict lookup
embeddings_json = dict(zip(range(len(embedding_matrix)), embedding_matrix))
with open("./embeddings-768-dim.json", "w") as fp:
	json.dump(embeddings_json, fp)

# now do PCA to convert 768 dimension to 3 dimension
pca = PCA(n_components=3)
pca.fit(embedding_matrix)

embedding_matrix_3d = pca.transform(embedding_matrix)
embeddings_3d_json =  dict(zip(range(len(embedding_matrix_3d)), embedding_matrix_3d))
with open("./embeddings-3d.json", "w") as fp:
	json.dump(embeddings_3d_json, fp)