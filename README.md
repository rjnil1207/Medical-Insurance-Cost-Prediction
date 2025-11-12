# 🏥 Medical Insurance Cost Prediction App  

This project is an **AI-powered Streamlit web application** that predicts **medical insurance costs** using a variety of personal and health-related factors such as **age**, **BMI**, **smoking habits**, and **number of children**.  
The solution integrates **machine learning models** with **MLflow experiment tracking** to ensure transparency, reproducibility, and scalability.


## 🚀 Features  

- 📊 **Predicts insurance cost** based on user inputs:
  - Age  
  - BMI  
  - Number of Children  
  - Smoker / Non-Smoker  

- 🧠 **Feature Engineering:**
  - `smoker_bmi` = smoker × BMI  
  - `age_smoker` = age × smoker  
  - `age_bmi` = age × BMI  

- 🤖 **Machine Learning Models Used:**
  - Linear Regression  
  - Ridge Regression  
  - RandomForestRegressor  
  - GradientBoostingRegressor  
  - XGBoostRegressor  

- 📈 **Experiment Tracking with MLflow**
  - Logs all model metrics (MAE, RMSE, R²)
  - Saves scaler and trained model for reproducible predictions
  - Uses relative URI: `file:///./mlruns` (works on both local and cloud)

- 🌐 **Interactive Streamlit Interface**
  - User-friendly form for inputs  
  - Real-time prediction output  
  - Clean visualization and insights  

---

## 🧩 Model Performance Summary  

| Model | Train R² | Test R² | MAE (₹) | RMSE (₹) | Observation |
|--------|-----------|----------|----------|-----------|-------------|
| Linear Regression | 0.833 | 0.860 | 2805| 4551 | Stable baseline |
| Ridge Regression | 0.833 | 0.859 | 2813 | 4561 | Similar to Linear |
| Random Forest | 0.976 | 0.842 | 2601 | 4830 | overfitted |
| Gradient Boosting | **0.902** | **0.875** | **2342** | **4296** | Balanced, strong performer |
| XGBoost (Final) | 0.992 | 0.832 | 2685 | 4978 | overfitted |

**✅ Final Selected Model:** `GradientBoostRegressor`  
**🎯 Accuracy:** R² = **0.884**, MAE ≈ 2,405

---

## 🧠 Key Insights  

- **Top Predictors:**  
  - Smoking status is the **most dominant factor** influencing charges.  
  - `smoker_bmi` interaction captures the joint effect of obesity & smoking.  
  - Age contributes linearly to premium increase.  

- **Business Takeaways:**  
  - Smokers pay on average **2.5× higher** insurance costs.  
  - Lifestyle factors (BMI, smoking) can be leveraged to create health-based discount plans.  
  - Predictive modeling helps insurers **personalize pricing** and forecast premiums more effectively.  

- **Model Reliability:**  
  - Explains ~**88%** of the total variation in charges.  
  - Minimal train–test gap → strong generalization.  
  - Average prediction error ≈ ₹2,405 — highly practical for real-world use.  

---

## ☁️ Deployment  

This app is **deployed on Streamlit Cloud** directly from the GitHub repository.  
All paths and resources are relative, ensuring smooth operation across environments.


## 📂 Project Structure

Medical-Insurance-Predictor/
│
├── app.py                               # Main Streamlit application
├── data                                 # CSV file and Screenshots
├── Medical Insurance Prediction.ipynb   # Train & log models to MLflow
├── README.md  
├── requirements.txt                     # Requirements  
├── scaler.pkl                           # Saved Scaler  
├── final_model.pkl                      # Saved Model  
└── mlruns/                              # MLflow tracking artifacts

## 👨‍💻 Author

Niladri Giri
📧 Email: rjnil1207@gmail.com
💼 Aspiring Data Scientist | Machine Learning & AI Enthusiast