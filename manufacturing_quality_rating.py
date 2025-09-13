import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk
import os

# Load the pre-trained model
# model = pk.load(open('manufacturing_quality_rating_model.pkl', 'rb'))
model_path = os.path.join(os.path.dirname(__file__), "manufacturing_quality_rating_model.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)   # ✅ consistent variable name
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Set page configuration
st.set_page_config(page_title="Manufacturing Quality Rating Predictor", layout="wide")
st.title("Manufacturing Quality Rating Predictor")
st.write("This application predicts the quality rating of manufactured products based on various features.")

# Load dataset
try:
    df = pd.read_csv('manufacturing_xgr.csv')
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

temperature = st.text_input("Enter your Temperature (°C):")
pressure = st.text_input("Enter your Pressure (kPa):")
temperature_x_Pressure = st.text_input("Enter your Temperature x Pressure:")
material_fusion_metric = st.text_input("Enter your Material Fusion Metric:")
material_transformation_fusion_metric = st.text_input("Enter your Material Transformation Metric:")

if st.button("Predict"):
    input_data = pd.DataFrame([[temperature, pressure, temperature_x_Pressure, material_fusion_metric, material_transformation_fusion_metric]], columns=['Temperature (°C)', 'Pressure (kPa)', 'Temperature x Pressure', 'Material Fusion Metric', 'Material Transformation Metric'])
    input_data = input_data.astype(float)
    prediction = model.predict(input_data)

    st.write(f"The predicted Quality Rating is: {prediction[0]:.2f}")

