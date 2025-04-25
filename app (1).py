import streamlit as st
from PIL import Image

st.title("Deforestation Detection App")
st.write("Upload a satellite image to check for signs of deforestation.")

uploaded_file = st.file_uploader("Choose a satellite image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("Analyzing image...")
    
    # Dummy analysis
    st.success("Result: This area shows signs of deforestation.")
