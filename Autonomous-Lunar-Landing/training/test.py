import gymnasium as gym
from stable_baselines3 import PPO

# ==========================================
# Create environment with rendering
# ==========================================
env = gym.make(
    "LunarLander-v3",
    render_mode="human"
)

# ==========================================
# Load trained model
# ==========================================
model = PPO.load("models/ppo_lander_1M")

EPISODES = 10

for episode in range(EPISODES):

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

    print(
        f"Episode {episode + 1} Reward: {total_reward:.2f}"
    )

env.close()

print("Testing completed.")