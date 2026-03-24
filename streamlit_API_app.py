import streamlit as st
import pandas as pd
import joblib
from utils import create_features
from groq_setup import get_llm_response

api_key = st.secrets["GROQ_API_KEY"]


pipeline = joblib.load("model\\pipeline.pkl")

st.title("🏦 Bank Churn Prediction AI")


credit_score = st.slider("Credit Score", 300, 900, 600)
age = st.slider("Age", 18, 80, 40)
tenure = st.slider("Tenure (years)", 0, 10, 5)
balance = st.number_input("Balance", 0, 200000, 50000)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
credit_card = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Active Member", [0, 1])
st.write("0 : Not an active member, 1 : An Active member")
salary = st.number_input("Estimated Salary", 0, 200000, 50000)
country = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict"):
    data = {
        "credit_score": credit_score,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products,
        "credit_card": credit_card,
        "active_member": active,
        "estimated_salary": salary,
        "country": country,
        "gender": gender
    }

    
    processed_data = create_features(data.copy())

    df = pd.DataFrame([processed_data])

    
    prediction = pipeline.predict(df)[0]
    prob = pipeline.predict_proba(df)[0][1]
    
    if prob < 0.5:
        st.success("Customer is likely to stay.")
    else:
        st.warning("Customer is likely to churn.")
    
    insight = get_llm_response({
        "input": data,
        "prediction": int(prediction),
        "probability": float(prob)
    })

    st.subheader(f"Prediction: {'Churn' if prediction else 'No Churn'}")
    st.write(f"Churn Probability: {prob:.2f}")

    st.subheader("AI Insights")
    st.write(insight)