from flask import Flask, render_template, request
import os
import joblib
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATHS = [
    os.path.join(BASE_DIR, '..', 'Model', 'HDI.pkl'),
    os.path.join(BASE_DIR, '..', 'Flask', 'model', 'HDI.pkl'),
]

model = None
for path in MODEL_PATHS:
    if os.path.exists(path):
        model = joblib.load(path)
        break

if model is None:
    raise FileNotFoundError('Model file not found')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['life_expectancy']),
        float(request.form['education']),
        float(request.form['income'])
    ]
    df = pd.DataFrame([features], columns=['life_expectancy', 'education', 'income'])
    prediction = model.predict(df)[0]
    return render_template('result.html', prediction=round(prediction, 4))

if __name__ == '__main__':
    app.run(debug=True)
