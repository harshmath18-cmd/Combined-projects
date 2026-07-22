from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get form data
    features = [
        float(request.form["gender"]),
        float(request.form["ssc_p"]),
        float(request.form["ssc_b"]),
        float(request.form["hsc_p"]),
        float(request.form["hsc_b"]),
        float(request.form["hsc_s"]),
        float(request.form["degree_p"]),
        float(request.form["degree_t"]),
        float(request.form["workex"]),
        float(request.form["etest_p"]),
        float(request.form["specialisation"]),
        float(request.form["mba_p"])
    ]

    # Convert to NumPy array
    features = np.array(features).reshape(1, -1)

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)[0]

    # Confidence (only if model supports it)
    confidence = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(features)
        confidence = round(max(probability[0]) * 100, 2)

    # Prediction Result
    if prediction == 1:

        result = "Placed"
        color = "success"

        tips = [
            "Excellent academic performance.",
            "Keep improving communication skills.",
            "Practice aptitude and interview questions."
        ]

    else:

        result = "Not Placed"
        color = "danger"

        tips = [
            "Improve technical knowledge.",
            "Work on aptitude preparation.",
            "Practice mock interviews."
        ]

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        color=color,
        tips=tips
    )


if __name__ == "__main__":
    app.run(debug=True)