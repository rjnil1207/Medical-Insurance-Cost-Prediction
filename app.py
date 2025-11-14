# Importing Libraries
import pandas as pd
import streamlit as st
import joblib

# Load scaler & model
scaler = joblib.load("scaler.pkl")
model = joblib.load("final_model.pkl")

# App Title (centered)
st.markdown(
    """
    <h1 style="text-align:center; color:#2E86C1;">
        Medical Insurance Predictor
    </h1>
    <p style="text-align:center; font-size:18px; color:gray;">
        Predict your estimated insurance cost using Machine Learning 💡
    </p>
    """,
    unsafe_allow_html=True
)

# Input Section
st.subheader("🧾 Fill in Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("🎂 Age", min_value=18, max_value=64, step=1, value=30)
    sex = st.radio("🧑 Gender", ["Male", "Female"], horizontal=True)

with col2:
    bmi = st.number_input("⚖️ BMI", min_value=15.0, max_value=45.0, step=0.2, value=25.0)
    smoker = st.radio("🚬 Smoker", ["Yes", "No"], horizontal=True)

with col3:
    children = st.number_input("👶 Children",min_value=0, max_value=5, step=1, value=0)
    region = st.selectbox("🗺️ Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

# Feature Engineering
num_smoker = 1 if smoker == "Yes" else 0
bmi_smoker = bmi if num_smoker == 1 else 0

# Input DataFrame for model
df = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'num_smoker': [num_smoker],
    'bmi_smoker': [bmi_smoker]})

# Scaling
input_scaled = scaler.transform(df)

# Prediction
a,b,c = st.columns([1,2,1])
with b:
    if st.button("🔍 Predict Insurance Cost", use_container_width=True):
        try:
            prediction = model.predict(input_scaled)[0]
            st.success(f"💰**Estimated Insurance Cost: ₹{prediction:,.2f}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:14px;">
        Made with ❤️ by <b>Niladri Giri</b><br>
        <span style="font-size:12px;">Powered by Streamlit & MLflow</span>
    </div>
    """,
    unsafe_allow_html=True
)
