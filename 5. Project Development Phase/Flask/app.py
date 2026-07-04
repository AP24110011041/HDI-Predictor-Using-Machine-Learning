from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Possible model locations
MODEL_PATHS = [
    os.path.join(BASE_DIR, "..", "Model", "HDI.pkl"),
    os.path.join(BASE_DIR, "model", "HDI.pkl")
]

model = None

for path in MODEL_PATHS:
    if os.path.exists(path):
        model = joblib.load(path)
        print(f"Model loaded from: {path}")
        break

if model is None:
    print("Warning: HDI.pkl model file not found.")

# Feature names used during training
FEATURES = [
    "Life Expectancy at Birth (2021)",
    "Mean Years of Schooling (2021)",
    "Gross National Income Per Capita (2021)"
]


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if model is None:
            return "Error: HDI.pkl model file not found."

        try:
            life = float(request.form["Life Expectancy at Birth (2021)"])
            school = float(request.form["Mean Years of Schooling (2021)"])
            income = float(request.form["Gross National Income Per Capita (2021)"])

            sample = pd.DataFrame(
                [[life, school, income]],
                columns=FEATURES
            )

            prediction = round(model.predict(sample)[0], 4)

            if prediction < 0.55:
                category = "Low Human Development"
            elif prediction < 0.70:
                category = "Medium Human Development"
            elif prediction < 0.80:
                category = "High Human Development"
            else:
                category = "Very High Human Development"

            return render_template(
                "result.html",
                prediction=prediction,
                category=category
            )

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )