from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_recommender(df):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['ingredients'])
    return tfidf, tfidf_matrix

def recommend_recipes(df, tfidf, tfidf_matrix, user_input, top_n=10):
    user_vec = tfidf.transform([user_input])
    similarity = cosine_similarity(user_vec, tfidf_matrix)[0]

    # Always use full df length
    top_indices = similarity.argsort()[-top_n:][::-1]

    return df.iloc[top_indices]
