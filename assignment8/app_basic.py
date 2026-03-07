import streamlit as st

st.title("Welcome to streamlit")
name=st.text_input('Enter your name')
if st.button("Greet Me") and name!='':
    st.write(f"Hello, {name}!")