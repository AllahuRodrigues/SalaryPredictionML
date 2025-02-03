#app.py

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from about_page import show_about_page  # <-- import the new function

# Add 'About Me' to our side menu
page = st.sidebar.selectbox(
    "Navigation",
    ("Predict", "Explore", "About Me")
)

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    show_about_page()
