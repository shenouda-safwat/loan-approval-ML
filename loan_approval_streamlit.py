import streamlit as st
import pandas as pd
import joblib

xgb_model = joblib.load('best_model.pkl')

st.markdown("""
    <style>
    /* خلفية عامة */
    .main {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* عنوان التطبيق */
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        color: #ffd700;  /* ذهبي */
        text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
    }

    /* نص الوصف */
    .description {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        color: #eee;
    }

    /* أزرار */
    div.stButton > button {
        background-color: #ffd700;
        color: #4b0082;
        font-weight: bold;
        padding: 10px 25px;
        border-radius: 15px;
        border: none;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #ffec8b;
        color: #3a006e;
    }

    /* Inputs */
    .stNumberInput > label, .stSelectbox > label {
        font-weight: 600;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 Loan Approval Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Enter the applicant\'s data to find out whether the loan will be approved or not</div>', unsafe_allow_html=True)

no_of_dependents = st.number_input("📌 Number of Dependents", min_value=0, max_value=10, value=0)
education = st.selectbox("🎓 Education", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("💼 Self Employed", ['Yes', 'No'])
income_annum = st.number_input("💵 Annual Income", min_value=0, value=100000)
loan_amount = st.number_input("💳 Loan Amount", min_value=0, value=50000)
loan_term = st.number_input("📆 Loan Term (in years)", min_value=1, value=5)
cibil_score = st.number_input("📊 CIBIL Score", min_value=300, max_value=900, value=700)
residential_assets_value = st.number_input("🏠 Residential Assets Value", min_value=0, value=100000)
commercial_assets_value = st.number_input("🏢 Commercial Assets Value", min_value=0, value=50000)
luxury_assets_value = st.number_input("🚗 Luxury Assets Value", min_value=0, value=25000)
bank_asset_value = st.number_input("🏦 Bank Asset Value", min_value=0, value=75000)

education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

input_data = pd.DataFrame({
    'no_of_dependents': [no_of_dependents],
    'education': [education],
    'self_employed': [self_employed],
    'income_annum': [income_annum],
    'loan_amount': [loan_amount],
    'loan_term': [loan_term],
    'cibil_score': [cibil_score],
    'residential_assets_value': [residential_assets_value],
    'commercial_assets_value': [commercial_assets_value],
    'luxury_assets_value': [luxury_assets_value],
    'bank_asset_value': [bank_asset_value],
})

if st.button("📈 Predict Loan Status"):
    prediction = xgb_model.predict(input_data)[0]
    prediction_proba = xgb_model.predict_proba(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.markdown("### Probability Details:")
    st.write(f"Approval Probability: **{prediction_proba[1]*100:.2f}%**")
    st.write(f"Rejection Probability: **{prediction_proba[0]*100:.2f}%**")
