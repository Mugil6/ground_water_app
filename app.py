from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('groundwater_model.pkl')  # Ensure this file is in the same folder

@app.route('/')
def home():
    return jsonify({"message": "Groundwater AQI Prediction API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({'predicted_avg_depth': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
