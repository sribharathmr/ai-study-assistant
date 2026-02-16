from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import preprocess_text

def find_best_match(query, documents):
    processed_docs = [preprocess_text(doc) for doc in documents]
    processed_query = preprocess_text(query)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_docs + [processed_query])

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    best_match_index = similarity_scores.argmax()
    return documents[best_match_index]
