import streamlit as st
import joblib
import pandas as pd

# Load saved artifacts
model = joblib.load('models/best_model.joblib')
column_transformer = joblib.load('models/column_transformer.joblib')
label_encoder = joblib.load('models/label_encoder.joblib')

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")
st.title("Customer Churn Predictor")
st.write("Enter customer details to predict the likelihood of churn.")

# --- Input form ---
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = int(st.selectbox("Senior Citizen", [0, 1]))
    Partner = st.selectbox("Has Partner", ["Yes", "No"])
    Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
    tenure = st.selectbox("Tenure", [
    "0-1 year", "1-2 year", "2-3 year", "3-4 year", "4-5 year", "5-6 year"
])
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

with col2:
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 840.0)

# --- Predict ---
if st.button("Predict Churn", type="primary"):
    input_df = pd.DataFrame([{
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }])

    # Apply the same transformer used during training
    input_transformed = column_transformer.transform(input_df)

    # Predict
    prediction = model.predict(input_transformed)
    prediction_proba = model.predict_proba(input_transformed)[:, 1][0]
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Prediction", predicted_label)
    with col_b:
        st.metric("Churn Probability", f"{prediction_proba:.1%}")
