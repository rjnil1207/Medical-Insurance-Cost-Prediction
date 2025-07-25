import streamlit as st
import mlflow
import mlflow.sklearn
import pandas as pd

# Set tracking URI 
mlflow.set_tracking_uri("file:///C:/Users/Nil/Documents/GUVI PROJECT/Medical Insurance Predict ML/mlruns")

# Load model
model_uri = "runs:/3c0b05346f3641f5b8bea73d8ddc17b4/model"
model = mlflow.sklearn.load_model(model_uri)

# App Title
st.title("🏥 Insurance Cost Prediction")

# Input Section
st.header("📋 Enter Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    sex = st.selectbox("🧑 Sex", ["Male", "Female"])
    age = st.slider("🎂 Age", 18, 100, 30)

with col2:
    smoker = st.selectbox("🚬 Smoker", ["Yes", "No"])
    bmi = st.slider("⚖️ BMI", 15.0, 45.0, 25.0)

with col3:
    region = st.selectbox("🗺️ Region", ["Southeast", "Southwest", "Northeast", "Northwest"])
    children = st.slider("👶 Children", 0, 5, 0)

# Feature Engineering
smoker_val = 1 if smoker == "Yes" else 0
smoker_bmi = bmi if smoker_val == 1 else 0

# Input DataFrame for model
input_df = pd.DataFrame({
    'age': [age],
    'smoker*bmi': [smoker_bmi]})

# Prediction
if st.button("🔍 Predict Insurance Cost"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"💰**Estimated Insurance Cost: ₹{prediction:,.2f}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# Footer
st.markdown("---")
st.markdown("**Made with ❤️ by Streamlit & MLflow**")
