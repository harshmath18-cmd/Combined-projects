import os
import csv
import statistics

import gymnasium as gym
from stable_baselines3 import PPO


# ==========================================
# Configuration
# ==========================================

MODEL_PATH = "models/ppo_lander_1M"
NUM_EPISODES = 30

OUTPUT_FOLDER = "evaluation"
OUTPUT_CSV = os.path.join(OUTPUT_FOLDER, "episode_rewards.csv")


# ==========================================
# Create output folder
# ==========================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ==========================================
# Load model
# ==========================================

print("Loading trained model...")

model = PPO.load(MODEL_PATH)

print("Model loaded successfully!\n")


# ==========================================
# Create environment
# ==========================================

env = gym.make("LunarLander-v3")


# ==========================================
# Evaluate
# ==========================================

episode_rewards = []

with open(OUTPUT_CSV, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Episode", "Reward"])

    for episode in range(1, NUM_EPISODES + 1):

        obs, info = env.reset()

        done = False

        total_reward = 0

        while not done:

            action, _ = model.predict(
                obs,
                deterministic=True
            )

            obs, reward, terminated, truncated, info = env.step(action)

            total_reward += reward

            done = terminated or truncated

        episode_rewards.append(total_reward)

        writer.writerow([episode, round(total_reward, 2)])

        print(f"Episode {episode:02d} | Reward = {total_reward:.2f}")


env.close()


# ==========================================
# Statistics
# ==========================================

average_reward = statistics.mean(episode_rewards)

maximum_reward = max(episode_rewards)

minimum_reward = min(episode_rewards)

std_reward = statistics.stdev(episode_rewards)

successes = sum(r >= 200 for r in episode_rewards)

success_rate = successes / NUM_EPISODES * 100


print("\n==============================")
print("Evaluation Finished")
print("==============================")

print(f"Average Reward : {average_reward:.2f}")
print(f"Highest Reward : {maximum_reward:.2f}")
print(f"Lowest Reward  : {minimum_reward:.2f}")
print(f"Std Deviation  : {std_reward:.2f}")
print(f"Success Rate   : {success_rate:.1f}%")

print("\nRewards saved to:")
print(OUTPUT_CSV)