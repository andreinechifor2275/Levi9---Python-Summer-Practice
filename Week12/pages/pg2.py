# 2. Make a user data input page
# - input user name
# - input a short user bio (multiple lines)
# - input user birth date

import streamlit as st
from datetime import date

st.title("User Data Input Page")
name = st.text_input("Enter your name:")
bio = st.text_area("Write a short bio:")

birth_date = st.date_input(
    "Birth date:",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Submit"):
    st.subheader("Your Submitted Data")
    st.write(f"**Name:** {name}")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Birth Date:** {birth_date.strftime('%B %d, %Y')}")