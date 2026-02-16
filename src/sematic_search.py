from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query, documents):
    query_embedding = model.encode(query, convert_to_tensor=True)
    doc_embeddings = model.encode(documents, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, doc_embeddings)[0]
    best_match = scores.argmax()

    return documents[int(best_match)]
