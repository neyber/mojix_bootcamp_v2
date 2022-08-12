import streamlit as st

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")

option = st.selectbox(
     'Select a python trick that you want to know',
     ('Walrus operator', 'Splitting a string', 'Reversing a string', 'Merging two dictionaries', 'The zip() function', 'Assigning multiple list values to a variable', 'Lambda function', 'Swapping variable value', 'Use a password in your code')
     )

st.write('You selected:', option)