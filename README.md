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





