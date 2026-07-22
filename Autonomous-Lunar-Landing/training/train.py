import os

import gymnasium as gym

from stable_baselines3 import PPO




# ==========================================
# Create Lunar Lander Environment
# ==========================================
env = gym.make("LunarLander-v3")

# ==========================================
# Create models folder if it doesn't exist
# ==========================================
os.makedirs("models", exist_ok=True)

MODEL_PATH = "models/ppo_lander_1M"

# ==========================================
# Load existing model if available
# ==========================================
if os.path.exists(MODEL_PATH + ".zip"):
    print("Loading existing model...")
    model = PPO.load(MODEL_PATH, env=env)
else:
    print("Creating new PPO model...")
    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
    )

# ==========================================
# Train the model
# ==========================================
print("Training started...")

model.learn(
    total_timesteps=1_000_000,
    progress_bar=True
)

print("Training completed.")

# ==========================================
# Save model
# ==========================================
model.save(MODEL_PATH)

print("Model saved successfully!")