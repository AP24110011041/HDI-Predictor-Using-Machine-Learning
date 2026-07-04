# Functional Requirements

## Overview

Functional requirements describe the features and operations that the HDI Prediction System must perform.

## Functional Requirements

### FR-01: User Input

The system shall allow users to enter the required socio-economic indicators through a web interface.

### FR-02: Input Validation

The system shall validate all user inputs before processing.

### FR-03: Data Processing

The system shall preprocess the input values before sending them to the trained machine learning model.

### FR-04: HDI Prediction

The system shall predict the Human Development Index using the trained Linear Regression model.

### FR-05: Display Results

The system shall display the predicted HDI score and its corresponding category.

### FR-06: Model Loading

The system shall load the trained model (`HDI.pkl`) during application startup.

### FR-07: Error Handling

The system shall display appropriate error messages for invalid or missing inputs.