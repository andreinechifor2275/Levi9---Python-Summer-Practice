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

# 3. Calculator App
# - two number inputs
# - a dropdown that has the following options (+, -, *, /)
# - a button that executes the operation on the given numbers
# - display the resulted value
# - handle possible errors

import streamlit as st

st.title("Calculator App using Streamlit")

st.write("---")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

st.write("Operation")

operation = st.radio("Select an operation to perform:", ("Add", "Subtract", "Multiply", "Divide"))

rez = 0

def calculate():
    if operation == "Add":
        rez = num1 + num2
    elif operation == "Subtract":
        rez = num1 - num2
    elif operation == "Multiply":
        rez = num1 * num2
    elif operation == "Divide" and num2 != 0:
        rez = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter another number.")
        rez = "Not defined"

    st.success(f"Answer = {rez}")


if st.button("Calculate result"):
    calculate()


import streamlit as st
import pandas as pd


st.page_link("pages/pg1.py", label="Go to exercise 1")
st.page_link("pages/pg2.py", label="Go to exercise 2")
st.page_link("pages/pg3.py", label="Go to exercise 3")