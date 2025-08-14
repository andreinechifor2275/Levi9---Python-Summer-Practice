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