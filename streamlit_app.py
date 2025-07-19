import streamlit as st
import pandas as pd
import joblib
import requests

# Load model
model = joblib.load("groundwater_model.pkl")

# Load CSV to get State-District mapping
df = pd.read_csv("groundwater_data.csv")
df.dropna(subset=['State', 'District'], inplace=True)
state_district_map = df.groupby('State')['District'].unique().to_dict()

# Page setup
st.set_page_config(page_title="Groundwater Level Predictor", layout="centered")
st.title("💧 Groundwater Depletion Prediction")
st.markdown("Use this app to predict average groundwater depth based on State, District, Year, and Monsoon type.")

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/groundwater.png", width=100)
st.sidebar.markdown("### About")
st.sidebar.markdown("This app uses an ML model to predict groundwater levels using trained historical data.")

# Dropdowns
state = st.selectbox("Select State", list(state_district_map.keys()))
district = st.selectbox("Select District", sorted(state_district_map[state]))

# Year and monsoon input
year = st.number_input("Enter Year", min_value=2000, max_value=2050, step=1)
monsoon = st.radio("Select Season", ['Pre Monsoon', 'Post Monsoon'])

# Predict
if st.button("🔍 Predict Groundwater Level"):
    if state and district and year and monsoon:
        try:
            input_data = {
                'State': state,
                'District': district,
                'Year': year,
                'Season': monsoon
            }

            # Convert input to DataFrame
            input_df = pd.DataFrame([input_data])

            prediction = model.predict(input_df)[0]

            st.success(f"✅ Predicted Avg Groundwater Depth: **{round(prediction, 2)} meters (mbgl)**")
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
    else:
        st.warning("Please fill all the fields to get a prediction.")
