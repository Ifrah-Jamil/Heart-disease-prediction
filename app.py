##STREAMLIT APPLICATION 

import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("heart_disease_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Prediction App")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient health details below:")

# -------- INPUT FIELDS --------
age = st.number_input("Age", min_value=1, max_value=120, value=30)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol Level",
    min_value=100,
    max_value=400,
    value=200
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=50.0,
    value=25.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=1.0,
    max_value=12.0,
    value=7.0
)

# -------- PREDICTION --------
if st.button("Predict"):
    # Arrange inputs EXACTLY as training order
    input_data = np.array([[
        age,
        blood_pressure,
        cholesterol,
        bmi,
        sleep_hours
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Display result
    if prediction[0] == 1:
        st.error(" Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")










