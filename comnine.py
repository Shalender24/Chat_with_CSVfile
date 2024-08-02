import streamlit as st
from chat_app import run_chat_app
from visualize_app import run_visualize_app

st.sidebar.title("Navigation")
app_selection = st.sidebar.radio("Go to", ("Chat with CSV", "Visualize Data"))

if app_selection == "Chat with CSV":
    run_chat_app()
elif app_selection == "Visualize Data":
    run_visualize_app()
