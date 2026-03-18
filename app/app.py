from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "..", "model", "student_model.pkl")

model = pickle.load(open(model_path, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        study_hours = float(request.form.get("hours", 0))
        attendance = float(request.form.get("attendance", 0))
        previous = float(request.form.get("previous", 0))
        assignments = float(request.form.get("assignments", 0))

        prediction = model.predict([[study_hours, attendance, previous, assignments]])
        result = round(float(prediction[0]), 2)

        category = "Fail"
        if result >= 80:
            category = "Distinction"
        elif result >= 60:
            category = "Merit"
        elif result >= 40:
            category = "Pass"

        return render_template("index.html", result=result, category=category)

    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
