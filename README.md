# 🌍 Human Development Index (HDI) Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the Human Development Index (HDI) of a country using Machine Learning and Flask.

The application takes three important indicators as input:

- Life Expectancy at Birth
- Mean Years of Schooling
- Gross National Income (GNI) Per Capita

It predicts the HDI score and classifies the country into one of four Human Development categories.

---

## Problem Statement

Human Development Index (HDI) is an important measure used by the United Nations Development Programme (UNDP) to evaluate a country's overall development.

Calculating HDI manually is time-consuming. This project uses Machine Learning to estimate HDI based on key development indicators.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- HTML5
- CSS3
- Joblib

---

## Machine Learning Algorithm

Linear Regression

---

## Input Features

- Life Expectancy at Birth (2021)
- Mean Years of Schooling (2021)
- Gross National Income Per Capita (2021)

---

## Output

- Predicted HDI Score
- Human Development Category

---

## Development Categories

| HDI Score | Category |
|-----------|--------------------------|
| Below 0.55 | Low Human Development |
| 0.55–0.699 | Medium Human Development |
| 0.70–0.799 | High Human Development |
| 0.80 and Above | Very High Human Development |

---

## Project Structure

```
HDI-Predictor-Using-Machine-Learning
│
├── Dataset
├── Notebook
├── Flask
│   ├── app.py
│   ├── templates
│   └── static
├── Model
├── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Add more features
- Improve model accuracy
- Deploy on Render
- Interactive dashboard
- Better visualizations

---

## Author

Shaik Mahammad Mathin