# streamlit_app.py

import streamlit as st
import joblib
import numpy as np
import os

# Load the trained model
MODEL_PATH = "groundwater_model.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please upload groundwater_model.pkl.")
    st.stop()

model = joblib.load(MODEL_PATH)

# UI Setup
st.set_page_config(page_title="🌍 Groundwater Predictor", layout="centered")
st.title("🌊 Groundwater Depletion Prediction")
st.markdown("""
This application uses a trained machine learning model to predict **Groundwater Stress Levels** across Indian districts.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Water_drop_icon.svg/1200px-Water_drop_icon.svg.png", width=100)

# Input Form
with st.form("prediction_form"):
    state = st.text_input("Enter State Name", placeholder="e.g., Tamil Nadu")
    district = st.text_input("Enter District Name", placeholder="e.g., Chennai")
    year = st.number_input("Enter Year", min_value=2000, max_value=2030, step=1, value=2025)

    submitted = st.form_submit_button("🔍 Predict Groundwater Level")

if submitted:
    try:
        # Simple encoding (same logic as model training assumed)
        state_encoded = hash(state.lower()) % 1000
        dist_encoded = hash(district.lower()) % 1000
        input_data = np.array([[state_encoded, dist_encoded, year]])

        prediction = model.predict(input_data)[0]
        st.success(f"**Predicted Groundwater Stress Level:** {prediction}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
