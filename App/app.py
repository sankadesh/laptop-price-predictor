import streamlit as st
import pickle
import numpy as np
import pandas as pd

# load pipeline
model = pickle.load(open("pipeline.pkl", "rb"))

st.title("Laptop Price Predictor")

# minimal input
company = st.selectbox(
    "Company",
    ["Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba", "Apple","Other"]
)
typename = st.selectbox(
    "Type Name",
    ["Ultrabook", "Notebook", "Netbook", "Gaming", "2 in 1 Convertible", "Workstation"]
)
ram = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)
weight = st.number_input("Weight (kg)", min_value=0.8, max_value=5.0, value=1.5, step=0.1)
opsys = st.selectbox(
    "Operating System",
    ["Windows", "Mac", "Linux", "Other"]
)
cpu_type = st.selectbox(
    "CPU Type",
    ["Intel Core i3", "Intel Core i5", "Intel Core i7","AMD","Other"]
)    

gpu_brand = st.selectbox(
    "Gpu Brand",
    ['Intel', 'Nvidia', 'AMD']
)

touch_val = st.checkbox("Touchscreen")
ips_val = st.checkbox("IPS Display")


if st.button("Predict"):
    # create dataframe with EXACT column names used during training
    input_df = pd.DataFrame([{
        "Company": company,
        "TypeName": typename,
        "Ram": ram,
        "Weight": weight,
        "TouchScreen": int(touch_val),
        "IPS": int(ips_val),
        "Cpu_type": cpu_type,
        "Gpu_brand": gpu_brand,
        "Opsys_type": opsys
    }])

    price = model.predict(input_df)[0]
    price_lkr = price * 365
    st.success(f"Predicted Price: Rs.{price_lkr:.2f}")

