import streamlit as st

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")

option = st.selectbox(
     'Select a python trick that you want to know',
     ('Walrus operator', 'Splitting a string', 'Reversing a string', 'Merging two dictionaries', 'The zip() function', 'Assigning multiple list values to a variable', 'Lambda function', 'Swapping variable value', 'Use a password in your code')
     )

if option == 'Walrus operator':
     st.write('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')
     st.header('Example')
     
     code = '''
          Mylist = [1,2,3]
          if(l := len(mylist) > 2)
          print(l)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     st.code('3', language='python')