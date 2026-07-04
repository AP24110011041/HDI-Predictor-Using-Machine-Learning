# System Architecture

## Overview

The Human Development Index (HDI) Prediction System is developed using Python, Flask, and Machine Learning.

The application predicts the Human Development Index (HDI) based on three important indicators:

- Life Expectancy at Birth (2021)
- Mean Years of Schooling (2021)
- Gross National Income Per Capita (2021)

## System Workflow

1. The user enters the required values through the web application.
2. Flask receives the input.
3. The trained Linear Regression model processes the input.
4. The model predicts the HDI score.
5. The application displays the predicted HDI and its development category.

## Components

- User
- Flask Web Application
- Linear Regression Model
- Prediction Result