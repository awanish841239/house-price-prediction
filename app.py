import streamlit as st
import numpy as np
import pickle
 
# Load the model
model = pickle.load(open("house_pricemodel.pkl", "rb"))

st.title("House Price Prediction")
MSSubClass = st.number_input("MSSubClass", min_value=20, max_value=190, value=60)

MSZoning = st.selectbox("MSZoning", ["RL", "RM", "C (all)", "FV", "RH"])

LotArea = st.number_input("Lot Area (sq ft)", min_value=1000, max_value=50000, value=8000)

OverallCond = st.slider("Overall Condition (1-10)", 1, 10, 5)

YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2024, value=2000)

YearRemodAdd = st.number_input("Year Remodelled", min_value=1800, max_value=2024, value=2000)

BsmtFinSF2 = st.number_input("Basement Finished Area 2 (sq ft)", min_value=0.0, max_value=2000.0, value=0.0)

TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0.0, max_value=5000.0, value=800.0)

import pandas as pd

btn = st.button("Price Predict Karo! 🏠")

if btn:
    # MSZoning ko number mein convert karo
    zoning_map = {"RL": 0, "RM": 1, "C (all)": 2, "FV": 3, "RH": 4}
    
    input_data = pd.DataFrame([[
        MSSubClass,
        zoning_map[MSZoning],
        LotArea,
        OverallCond,
        YearBuilt,
        YearRemodAdd,
        BsmtFinSF2,
        TotalBsmtSF
    ]], columns=["MSSubClass", "MSZoning", "LotArea", "OverallCond", 
                 "YearBuilt", "YearRemodAdd", "BsmtFinSF2", "TotalBsmtSF"])
    
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: ${prediction:,.0f} 🏠")