import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/processed/swiggy_clean.csv")

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# Keep only useful columns
features = df[
    [
        "Restaurant_Name",
        "Cuisine",
        "Rating",
        "Number_of_Ratings",
        "Average_Price",
        "Area",
        "City",
        "Pure_Veg"
    ]
].copy()

# Convert text to lowercase
features["Cuisine"] = features["Cuisine"].str.lower()
features["Area"] = features["Area"].str.lower()
features["City"] = features["City"].str.lower()

# Create one searchable text column
features["Search_Text"] = (
    features["Cuisine"] + " " +
    features["Area"] + " " +
    features["City"] + " " +
    features["Restaurant_Name"].str.lower()
)

print("\nFeature Dataset Shape:", features.shape)

# Save
features.to_csv(
    "dataset/final/master_restaurants.csv",
    index=False
)

print("\nMaster Dataset Created Successfully!")