# 1. Hello App
# - nice title
# - input that ask the user's name
# - display a nice greeting using the user's name1. Hello App
# - nice title
# - input that ask the user's name
# - display a nice greeting using the user's name

import streamlit as st

st.title("Hello")

name = st.text_input("Provide a name:")

if name:
    st.success(f"Hello, {name}! Welcome!")