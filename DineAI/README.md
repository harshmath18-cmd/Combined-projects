# 🍽️ DineAI - AI Restaurant Recommendation System

DineAI is an **AI-powered restaurant recommendation system** that helps users discover restaurants across India based on their preferences like **city, cuisine, restaurant name, and search queries**.

The system uses **Machine Learning and NLP techniques** to analyze restaurant data and provide relevant recommendations with a modern, responsive user interface.

---

## 🚀 Live Demo

🌐 **Website:**
https://dineai-oz55.onrender.com

---

## ✨ Features

* 🤖 AI-powered restaurant recommendations
* 🔍 Smart search by restaurant, city, or cuisine
* 🏙️ Restaurant discovery across Indian cities
* 🍕 Cuisine-based recommendations
* 🧠 NLP-based similarity matching
* 🖼️ Automatic restaurant image mapping
* 🏷️ Brand logo support for popular restaurant chains
* ⭐ Restaurant rating display
* 📍 Google Maps directions integration
* 📱 Fully responsive mobile-friendly design
* 🎨 Modern Apple-inspired UI design

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning & NLP

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Joblib

### Data Processing

* Pandas
* NumPy

### Deployment

* GitHub
* Render

---

## 🧠 How It Works

1. User enters a restaurant name, city, or cuisine preference.
2. The input query is processed using **TF-IDF Vectorization**.
3. The system compares restaurant features using **Cosine Similarity**.
4. The most relevant restaurants are recommended with:

   * Restaurant Name
   * Cuisine
   * Rating
   * Location
   * Restaurant Images
   * Google Maps Directions

---

## 📂 Project Structure

```text
DineAI/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── city_encoder.pkl
│   ├── cuisine_encoder.pkl
│   ├── restaurant_features.pkl
│   └── tfidf_vectorizer.pkl
│
├── dataset/
│
├── utils/
│   └── recommender.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│       ├── restaurants/
│       ├── brands/
│       ├── cities/
│       └── cuisines/
│
├── templates/
│
└── README.md
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Chedgeprathm/DineAI.git
```

### Navigate to Project Folder

```bash
cd DineAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## 🔮 Future Improvements

* 👤 User authentication
* ❤️ Favorite restaurants
* 🎯 Personalized recommendations
* 🎤 Voice-based food search
* ⭐ User reviews and ratings
* 🌐 Live restaurant API integration
* 🌙 Dark mode support

---

## 👨‍💻 Author

**Prathmesh Chedge**

GitHub:
https://github.com/Chedgeprathm

---

## ⭐ Support

If you like this project, consider giving this repository a ⭐ on GitHub.
