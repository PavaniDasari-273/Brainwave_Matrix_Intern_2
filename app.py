import streamlit as st
import pandas as pd 
import joblib 

model=joblib.load("fraud_detection_pipeline.pkl")
st.title("Credit Card Fraud Detection")
st.markdown("pleae enter the transaction details and use the predictuon button")
st.divider()
transaction_type=st.selectbox("Transaction Type",["CASH_OUT","PAYMENT","CASH_IN","TRANSFER","DEBIT"])
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance(sender)",min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input("New Balance(sender)",min_value=0.0,value=90000.9)
oldbalanceDest=st.number_input("Old Balance(receiver)",min_value=0.0,value=10000.0)
newbalanceDest=st.number_input("New Balance(receiver)",min_value=0.0,value=10000.0)

if st.button("Predict"):
    input_dict={
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }
    input_data = pd.DataFrame([input_dict])
    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction: {int(prediction)}")

    if prediction==1:
        st.error("Fraud Transaction")
    else:
        st.success("Not a Fraud Transaction")