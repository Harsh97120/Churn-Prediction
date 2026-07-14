# 📉 Customer Churn Predictor

An interactive web application built with **Streamlit** that uses a Machine Learning model to predict the likelihood of customer churn. 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://churn-prediction-harshn9712.streamlit.app/)

🔗 **Live URL:** [https://churn-prediction-harshn9712.streamlit.app/](https://churn-prediction-harshn9712.streamlit.app/)

---

## 🌟 Key Features

* **Real-time Predictions:** Input customer metrics and immediately receive the classification (Churn: Yes/No) and prediction probability.
* **Responsive Sidebar/Layout:** Side-by-side grouped input fields categorized by customer demographics, subscribed services, and contract details.
* **Pre-trained ML Pipeline:** Automatically preprocesses categorical and numerical features using a saved sklearn `ColumnTransformer`.

---

## 📂 Project Structure

```text
Churn-Prediction/
├── models/
│   ├── best_model.joblib          # Trained Machine Learning Model
│   ├── column_transformer.joblib  # Feature preprocessor (OneHotEncoder, StandardScaler, etc.)
│   └── label_encoder.joblib       # Label Encoder for target classification
├── app.py                         # Streamlit Web Application Source Code
└── requirements.txt               # Project Dependencies (pinned to compatible versions)
```

---

## 📋 Input Fields Explained

The predictor takes the following customer attributes into account:

| Category | Input Field | Description / Value Options |
| :--- | :--- | :--- |
| **Demographic** | Gender | Male, Female |
| | Senior Citizen | 0 (No), 1 (Yes) |
| | Has Partner | Yes, No |
| | Has Dependents | Yes, No |
| **Services** | Phone Service | Yes, No |
| | Multiple Lines | Yes, No, No phone service |
| | Internet Service | DSL, Fiber optic, No |
| | Online Security | Yes, No, No internet service |
| | Tech Support | Yes, No, No internet service |
| | Online Backup | Yes, No, No internet service |
| | Device Protection | Yes, No, No internet service |
| | Streaming TV | Yes, No, No internet service |
| | Streaming Movies | Yes, No, No internet service |
| **Billing & Contract** | Tenure | 0-1 year, 1-2 year, 2-3 year, 3-4 year, 4-5 year, 5-6 year |
| | Contract | Month-to-month, One year, Two year |
| | Paperless Billing | Yes, No |
| | Payment Method | Electronic check, Mailed check, Bank transfer, Credit card |
| | Monthly Charges | Numeric input ($) |
| | Total Charges | Numeric input ($) |

---

## Run Locally

Follow these steps to run the application on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.12+** installed.

### 2. Clone and Navigate to the Repository
```bash
git clone <repository-url>
cd Churn-Prediction
```

### 3. Install Dependencies
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
Start the Streamlit local server:
```bash
streamlit run app.py
```
This will automatically open the application in your default web browser at `http://localhost:8501`.
