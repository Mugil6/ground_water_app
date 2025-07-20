\# 🌊 Groundwater Prediction App (https://ground-water-app.onrender.com)



This project is an end-to-end \*\*MLOps application\*\* that predicts groundwater depletion severity  using historical groundwater level data. The project covers:



\- Data preprocessing

\- Model training and saving (`.pkl`)

\- Serving predictions via a Flask REST API

\- Docker containerization for production deployment



---





---



\## ⚙️ Features



\- \*\*Model\*\*: Machine Learning model trained on district/state/year groundwater data

\- \*\*API\*\*: REST API built using Flask

\- \*\*Dockerized\*\*: Easily deployable using Docker

\- \*\*Predictive\*\*: Returns groundwater stress category



---



\## How to Use



1\. Clone the repo and `cd` into the folder  

2\. Run `python train\_model.py` to train and save the model  

3\. Run `python app.py` to start the API locally at `http://localhost:5000`  

4\. Send POST requests to `/predict` with JSON input:  


⚠️ Data Limitations

> ❗ **Please note the following constraints of the current model:**

- 📉 **Rainfall data is only available till 2017**, while groundwater data starts from 2020.  
  Hence, rainfall has **not been directly used** in the current prediction model.
- 🌦 Future versions may use **forecasted rainfall** to enhance accuracy.
- 🧪 Model is trained on **only 4 years** of groundwater data, which may limit generalization.
- 📍 Predictions are **district-level**, while rainfall data is **region-level**, making direct mapping complex.





