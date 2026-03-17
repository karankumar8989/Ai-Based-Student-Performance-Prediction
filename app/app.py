from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("../model/student_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    try:
        study_hours = float(request.form.get("hours", 0))
        attendance = float(request.form.get("attendance", 0))
        previous = float(request.form.get("previous", 0))
        assignments = float(request.form.get("assignments", 0))

        # Perform prediction
        prediction = model.predict([[study_hours, attendance, previous, assignments]])
        result = round(float(prediction[0]), 2)
        
        # Categorize the result
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
    app.run(debug=True)