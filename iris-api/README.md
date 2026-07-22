# 🌸 Iris Flower Classification System

A Machine Learning-based web application that predicts the species of an Iris flower using a trained **Random Forest Classifier model**. The application is built with **Flask** and provides a simple, user-friendly interface for real-time classification.

---

## 🌐 Live Demo
Live API:  
👉 https://iris-api-adzj.onrender.com

---

## 📌 Project Overview
This project predicts the species of an Iris flower based on input features such as:

- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

The trained Machine Learning model processes these inputs and classifies the flower into one of the following:

- Setosa  
- Versicolor  
- Virginica  

---

## ✨ Features
🌸 Real-time flower classification  
🤖 Machine Learning based prediction  
🌐 Flask REST API  
⚡ Fast response time  
📡 Simple JSON input/output  
🧠 Lightweight and efficient model  

---

## 🛠️ Technologies Used
- Python  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  
- HTML (optional frontend)  
- CSS  

---

## 🧠 Machine Learning Model
- **Algorithm:** Random Forest Classifier  
- **Problem Type:** Multi-class Classification  
- **Dataset:** Iris Dataset (Scikit-learn)  
- **Model Output:** Flower species prediction  
- **Model Serialization:** Pickle (.pkl)  

---

## 📁 Project Structure
```
iris-api/
│
├── app.py
├── train.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🚀 Running the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Chedgeprathm/iris-api.git
```

### 2. Navigate to Project Folder
```bash
cd iris-api
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Flask App
```bash
python app.py
```

### 5. Open in Browser
```
http://127.0.0.1:5000
```

---

## 📡 API Usage

### Endpoint
```
POST /predict
```

### Input Format
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

### Output Format
```json
{
  "prediction": "setosa"
}
```

---

## 🌍 Deployment
The application is deployed on **Render Cloud Platform** and is accessible via the live link above.

---

## 📊 Future Improvements
- Improve model accuracy using feature engineering  
- Add multiple ML model comparison  
- Add database to store predictions  
- Build frontend UI dashboard  
- Deploy with custom domain  

---

## 👨‍💻 Author
**Prathmesh Chedge**

---

## ⭐ Support
If you found this project useful, consider giving it a ⭐ Star on GitHub.

---

## 📬 Contact
For feedback or suggestions, connect via GitHub.