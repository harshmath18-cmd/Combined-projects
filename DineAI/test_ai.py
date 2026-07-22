from utils.recommender import recommend

print("=" * 60)
print("DINEAI AI TEST")
print("=" * 60)

results = recommend("pizza in pune", 10)

print(results)