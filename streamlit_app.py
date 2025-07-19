import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("groundwater_model.pkl")

st.set_page_config(page_title="Groundwater Depletion Predictor", page_icon="💧")
st.title("💧 Groundwater Depletion Prediction App")
st.write("Enter environmental and location data to predict average groundwater depth (mbgl).")

# Example input fields — change these based on your model
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
district = st.text_input("District Name")
year = st.number_input("Year", min_value=2000, max_value=2050, step=1)

if st.button("Predict Groundwater Depth"):
    try:
        input_data = pd.DataFrame([{
            "rainfall": rainfall,
            "temperature": temperature,
            "district": district,
            "year": year
        }])

        prediction = model.predict(input_data)[0]
        st.success(f"🌊 Predicted Groundwater Level: {round(prediction, 2)} meters (mbgl)")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
