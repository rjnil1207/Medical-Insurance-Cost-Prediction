# 🏥 Medical Insurance Cost Prediction App

This project is a **Streamlit web application** that predicts medical insurance costs based on user inputs like age, BMI, smoking, and more. 
It uses **machine learning models trained on real-world data**, logged with **MLflow** for tracking and reproducibility.

----------------------------------------------------

## 🚀 Features

- 📊 Predict insurance cost based on inputs:
  - Age
  - BMI
  - Smoker
  - Children
  - Sex
  - Region

- 🤖 Supports multiple ML models:
  - Linear Regression
  - DecisionTreeRegressor
  - RandomForestRegressor
  - GradientBoostingRegressor
  - XGBoostRegressor

- 📈 Logs metrics and models with MLflow
- 🧪 Compares model performance (MSE, MAE, R²)

- 🌐 Interactive UI built with Streamlit

----------------------------------------------------

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (for UI)
- **scikit-learn** (for ML models)
- **MLflow** (for experiment tracking)
- **pandas** & **NumPy** (for data handling)

---

## 📂 Project Structure

Medical-Insurance-Predictor/
│
├── app.py                               # Main Streamlit application
├── data                                 # CSV file and Screenshots
├── Medical Insurance Prediction.ipynb   # Train & log models to MLflow
├── README.md  
├── requirements.txt                     # Requirements  
└── mlruns/                              # MLflow tracking artifacts