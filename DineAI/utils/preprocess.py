import pandas as pd

print("=" * 60)
print("DINEAI DATA CLEANING")
print("=" * 60)

# Load Swiggy dataset
df = pd.read_csv("dataset/raw/swiggy_master.csv")

print(f"\nOriginal Rows : {len(df)}")

# Remove duplicate rows
df = df.drop_duplicates()

print(f"After Removing Duplicates : {len(df)}")

# Fill missing values
df["Cuisine"] = df["Cuisine"].fillna("Unknown")
df["Number of Ratings"] = df["Number of Ratings"].fillna(0)
df["Offer Name"] = df["Offer Name"].fillna("No Offer")
df["Area"] = df["Area"].fillna("Unknown")

# Rename columns
df = df.rename(columns={
    "Restaurant Name": "Restaurant_Name",
    "Average Price": "Average_Price",
    "Number of Ratings": "Number_of_Ratings",
    "Offer Name": "Offer_Name",
    "Pure Veg": "Pure_Veg",
    "Location": "City"
})

# Save cleaned dataset
df.to_csv(
    "dataset/processed/swiggy_clean.csv",
    index=False
)

print("\nCleaning Completed Successfully!")

print("\nFinal Shape :", df.shape)

print("\nSaved As : dataset/processed/swiggy_clean.csv")
