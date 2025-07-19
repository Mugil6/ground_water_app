import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("groundwater_model.pkl")

# Streamlit UI
st.title("Groundwater Level Prediction")
st.markdown("Enter the features below to predict the average groundwater depth:")

# Example features – adjust to match your model's training data
district = st.text_input("District")
year = st.number_input("Year", min_value=2000, max_value=2050, step=1)
season = st.selectbox("Season", ["Pre Monsoon", "Post Monsoon"])

# Prepare input features
if st.button("Predict Groundwater Depth"):
    try:
        # Prepare dataframe - modify keys to match your model's feature columns
        input_data = pd.DataFrame([{
            "District": district,
            "Year": year,
            "Season": season
        }])
        
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Average Groundwater Depth: {round(prediction, 2)} meters")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
