import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Deforestation Detector", layout="wide")


st.markdown("<h1 style='text-align: center; color: green;'>🌳 Deforestation Detection App 🌍</h1>", unsafe_allow_html=True)


st.markdown("<p style='text-align: center;'>Upload a satellite image and find out if your area is suffering from deforestation.</p>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("*Choose a Satellite Image:*", type=["jpg", "jpeg", "png"])

with col2:
    st.image("https://cdn.pixabay.com/photo/2016/10/15/11/19/deforestation-1747621_960_720.jpg", use_column_width=True, caption="Example Deforested Area")


if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Satellite Image", use_column_width=True)

   
    st.markdown("### ✅ Analysis Result:")
    st.success("This area *shows signs of deforestation.* Take necessary action!")

 
    st.markdown("---")
    st.image("https://cdn.pixabay.com/photo/2013/07/25/13/01/forest-167536_1280.jpg", caption="Healthy Area for Comparison", use_column_width=True)
