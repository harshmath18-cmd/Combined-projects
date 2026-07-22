import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

print("=" * 60)
print("TRAINING DINEAI MODEL")
print("=" * 60)

# Load dataset
df = pd.read_csv("dataset/final/master_restaurants.csv")

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words="english")

# Transform text into vectors
feature_matrix = vectorizer.fit_transform(df["Search_Text"])

# Save vectorizer
with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Save feature matrix
with open("models/restaurant_features.pkl", "wb") as f:
    pickle.dump(feature_matrix, f)

# Save cleaned dataset
df.to_pickle("dataset/final/master_restaurants.pkl")

print("\nTraining Completed Successfully!")

print(f"\nRestaurants : {len(df)}")
print(f"Features : {feature_matrix.shape[1]}")