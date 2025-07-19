from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('groundwater_model.pkl')

@app.route('/')
def home():
      return jsonify({"message": "Groundwater AQI Prediction API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'predicted_avg_depth': round(prediction, 2)})

@app.route('/')
def home():
    return "Groundwater Prediction API"

if __name__ == '__main__':
    app.run(debug=True)
