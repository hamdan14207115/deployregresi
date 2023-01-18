import numpy as np
import pandas as pd
import streamlit as st
from pickle import load

# Load model
model = load(open("linear_regression.pkl","rb"))

# Judul
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style,unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Prediksi Effort Bug</h1>",unsafe_allow_html=True)
st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;"/>""",unsafe_allow_html=True)

# Input data
st.header("Input Data")

story_point = st.number_input("Story Point",min_value=0,value=0)
in_progress_minutes = st.number_input("In Progress Minutes",min_value=0,value=0)
resolution_time_minutes = st.number_input("Resolution Time Minutes",min_value=0,value=0)

st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;"/>""",unsafe_allow_html=True)

# Prediksi
st.header("Prediction")

inputs = pd.DataFrame(
    data=[[story_point,in_progress_minutes,in_progress_minutes]],
    columns=["Story_Point", "In_Progress_Minutes", "Resolution_Time_Minutes"]
)
pred = model.predict(inputs)[0]

if st.button("Click here to predict"):
    st.success(f"The predicted total effort minutes is {round(pred,2)}")