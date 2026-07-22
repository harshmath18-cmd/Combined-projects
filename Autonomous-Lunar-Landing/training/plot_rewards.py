import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Paths
# ==========================================

CSV_PATH = "evaluation/episode_rewards.csv"

OUTPUT_DIR = "static/images"
OUTPUT_IMAGE = os.path.join(OUTPUT_DIR, "training_reward.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(CSV_PATH)

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(
    df["Episode"],
    df["Reward"],
    marker="o",
    linewidth=2,
    label="Episode Reward"
)

plt.axhline(
    y=200,
    color="green",
    linestyle="--",
    label="Solved Threshold (200)"
)

plt.title("Lunar Lander PPO Evaluation")

plt.xlabel("Episode")

plt.ylabel("Reward")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(OUTPUT_IMAGE, dpi=300)

plt.close()

print(f"\nGraph saved successfully:")
print(OUTPUT_IMAGE)