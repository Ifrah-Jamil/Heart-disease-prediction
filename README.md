#❤️ Heart Disease Prediction using Machine Learning
##Project Overview

This project focuses on predicting the presence of heart disease in patients using machine learning classification techniques.
The aim is to build an end-to-end ML pipeline starting from data preprocessing to model deployment using a Streamlit web application.

The project demonstrates practical skills in:
Data cleaning & preprocessing
Feature encoding & scaling
Model training and evaluation
Model deployment with an interactive UI

##Dataset

Dataset Type: Tabular medical dataset
Target Variable: Heart Disease Status
Problem Type: Binary Classification

Classes:

0 / False → No Heart Disease

1 / True → Heart Disease

The dataset contains patient information such as age, gender, blood pressure, cholesterol levels, lifestyle habits, and other health indicators.

## Technologies & Libraries Used

Python
Pandas & NumPy – Data handling
Matplotlib & Seaborn – Visualization and Manipulation
Scikit-learn – Machine learning models & preprocessing
Streamlit – Web application
Pickle – Model serialization

##Project Workflow
1️⃣ Data Exploration & Profiling
Used head(), info(), describe(), and null checks

2️⃣ Data Cleaning
Handled missing values
Removed irrelevant columns
Ensured correct data types

3️⃣ Feature Engineering
Target encoding using LabelEncoder
Feature selection to ensure consistency between training and deployment

4️⃣ Feature Scaling
Applied StandardScaler to normalize features

5️⃣ Model Training
Two classification models were trained and evaluated:
Logistic Regression
Random Forest Classifier

6️⃣ Model Evaluation

Models were evaluated using:
Accuracy
Classification
Confusion Matrix

7️⃣ Model Saving
Trained model saved using pickle

Scaler saved separately to ensure consistent preprocessing during prediction

##📈 Model Performance

Both Logistic Regression and Random Forest models achieved reliable accuracy on the test dataset.
Evaluation metrics such as classification report and confusion matrix were used to analyze performance beyond accuracy.

🌐 Web Application 
1. Streamlit
An interactive Streamlit web app was developed to:
Take user health inputs
Apply the same preprocessing steps
Predict heart disease in real time

#Live demo
https://heart-diseases-predictionss.streamlit.app/

2. Gradio
Lightweight and user-friendly ML interface
Provides quick predictions with minimal setup

## 📄 Project Report
You can download the complete project report from here:

[Heart Disease Prediction – Project Report](Heart_Disease_Prediction_ML_Project_Report.pdf)



