import streamlit as st
from predict import show_predict_page
from explore import show_explore_page

page = st.sidebar.selectbox("Insider/Institution or Fundamental",("Fundamental","Insider/Institution"))


if page=="Fundamental":
    show_predict_page()
else:
    show_explore_page()

