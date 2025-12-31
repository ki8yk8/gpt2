import numpy as np
import json

with open("embeddings-3d.json", "r") as fp:
	EMBEDDINGS = json.load(fp)

class Embeddings:
	@classmethod
	def compute_cosine_similarity(cls, i1, i2):
		t1, t2 = EMBEDDINGS[i1], EMBEDDINGS[i2]
		t1, t2 = np.array(t1), np.array(t2)
		
		return t1.dot(t2)
	
	def get_embeding(cls, i):
		return EMBEDDINGS(i)
