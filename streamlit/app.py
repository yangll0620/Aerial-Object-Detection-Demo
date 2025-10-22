import streamlit as st
from PIL import Image
import sys
import os


st.set_page_config(page_title="Roof Vision App", layout="wide")

st.title("🏠 Roof Vision Demo")
st.write("Upload an aerial or satellite image to detect roofs using AI technology.")

tab1, tab2 = st.tabs(["🏠 Demo", "📄 About Project"])

with tab1:
    st.header("Roof Vision Demo")
    

# --- Read and display roof_vision_description.md ---
readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'roof_vision_description.md'))
print(f"Readme path: {readme_path}")
with tab2:
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        st.markdown(readme_content, unsafe_allow_html=True)
    else:
        st.markdown("RoofVision is a cutting-edge web-based roof detection system, deployed on AWS for speed, scalability, and security.  "
                    "With just an image upload, our AI automatically detects and segments roofs with high accuracy, saving you hours of manual work.", unsafe_allow_html=True)