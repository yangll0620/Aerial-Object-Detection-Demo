import streamlit as st
from PIL import Image
import sys
import os

# --- Add parent project to import path ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


st.set_page_config(page_title="Roof Vision App", layout="wide")

st.title("🏠 Roof Vision Demo")
st.write("Upload an aerial or satellite image to detect roofs using your trained model.")

# Sidebar options
st.sidebar.header("Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)