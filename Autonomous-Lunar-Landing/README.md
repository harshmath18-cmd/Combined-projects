# 🚀 Autonomous Lunar Landing using Proximal Policy Optimization (PPO)

An AI-powered Reinforcement Learning project that teaches a spacecraft to autonomously land on the lunar surface using the **Proximal Policy Optimization (PPO)** algorithm.

The project is built using **Gymnasium**, **Stable-Baselines3**, **PyTorch**, and **Flask**, and includes a modern web interface to demonstrate the trained AI agent.

---

## 🎥 Demo

The homepage includes:

- 🚀 AI landing demonstration video
- 📊 Evaluation reward graph
- 📈 Model performance statistics
- 🤖 PPO algorithm explanation
- 🌕 Lunar Lander project overview

---

## ✨ Features

- Autonomous lunar landing using Reinforcement Learning
- PPO (Proximal Policy Optimization) algorithm
- Gymnasium LunarLander-v3 environment
- Flask web application
- Responsive modern UI
- Landing demonstration video
- Evaluation reward graph
- Trained model included in repository

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | PPO |
| Environment | LunarLander-v3 |
| Training Timesteps | 1,000,000 |
| Evaluation Episodes | 30 |
| Average Reward | **205.65** |
| Highest Reward | **278.66** |
| Lowest Reward | **-16.93** |
| Standard Deviation | **87.41** |
| Success Rate | **83.3%** |

> According to the Gymnasium benchmark, an average reward above **200** indicates that the LunarLander environment has been successfully solved.

---

## 🧠 Tech Stack

- Python
- Flask
- Gymnasium
- Stable-Baselines3
- PyTorch
- Box2D
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

```text
Autonomous-Lunar-Landing/

│── app.py
│── Procfile
│── requirements.txt
│── README.md
│── .gitignore

│── models/
│     └── ppo_lander_1M.zip

│── templates/
│     └── index.html

│── static/
│     ├── css/
│     ├── js/
│     ├── images/
│     └── videos/

│── training/
│     ├── train.py
│     ├── test.py
│     ├── evaluate.py
│     └── plot_rewards.py

│── evaluation/
│     └── episode_rewards.csv
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Chedgeprathm/Autonomous-Lunar-Landing.git
```

Go to the project directory

```bash
cd Autonomous-Lunar-Landing
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 🎮 Train the Model

```bash
python training/train.py
```

---

## 🛰️ Test the Model

```bash
python training/test.py
```

---

## 📈 Evaluate the Model

```bash
python training/evaluate.py
```

---

## 📊 Generate Reward Graph

```bash
python training/plot_rewards.py
```

---

## 🔮 Future Improvements

- TensorBoard integration
- Live evaluation dashboard
- Multiple reinforcement learning algorithms
- Hyperparameter comparison
- Dark/Light theme
- Training analytics dashboard

---

## 👨‍💻 Author

**Prathmesh Chedge**

GitHub:
https://github.com/Chedgeprathm

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!