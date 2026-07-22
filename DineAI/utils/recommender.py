import pickle
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from utils.restaurant_images import get_restaurant_image


# Load dataset
restaurants = pd.read_pickle(
    "dataset/final/master_restaurants.pkl"
)

# Load TF-IDF vectorizer
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load feature matrix
with open("models/restaurant_features.pkl", "rb") as f:
    feature_matrix = pickle.load(f)


def recommend(query, top_n=10):

    query = query.lower()

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(
        query_vector,
        feature_matrix
    ).flatten()

    indices = similarity.argsort()[-top_n:][::-1]

    results = restaurants.iloc[indices].copy()

    results["Image"] = results.apply(
    lambda row: get_restaurant_image(
        row["Restaurant_Name"],
        row["Cuisine"]
    ),
    axis=1
)

    return results 