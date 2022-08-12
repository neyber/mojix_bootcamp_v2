import streamlit as st

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")

option = st.selectbox(
     'Select a python trick that you want to know',
     ('Walrus operator', 'Splitting a string', 'Reversing a string', 'Merging two dictionaries', 'The zip() function', 'Assigning multiple list values to a variable', 'Remove duplicate list items', 'Lambda function', 'Swapping variable value', 'Use a password in your code')
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

elif option == 'Splitting a string':
     st.write('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')
     st.header('Example')
     
     code = '''
          string = “hello world”
string.split()
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          [‘hello’, ‘world’]
     '''

     st.code(output, language='python')

elif option == 'Reversing a string':
     st.write('If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')
     st.header('Example')
     
     code = '''
          str=”hello world!”
a=str[::-1]
print(a)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          !dlrow olleh
     '''

     st.code(output, language='python')

elif option == 'Merging two dictionaries':
     st.write('This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:')
     st.header('Example')
     
     code = '''
          d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          {‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}
     '''

     st.code(output, language='python')

elif option == 'The zip() function':
     st.write('The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.')
     st.header('Example')
     
     code = '''
          colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          red apple
yellow banana
green mango
     '''

     st.code(output, language='python')

elif option == 'Assigning multiple list values to a variable':
     st.write('If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:')
     st.header('Example')
     
     code = '''
          mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          a = 1
b = [2, 3, 4, 5]
     '''

     st.code(output, language='python')

elif option == 'Remove duplicate list items':
     st.write('Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.')
     st.header('Example')
     
     code = '''
          mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          {1, 2, 3, 4, 5, 6, 7, 8, 9}
     '''

     st.code(output, language='python')

elif option == 'Lambda function':
     st.write('If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.')
     st.header('Example')
     
     code = '''
          mul = lambda a,b: a*b
mul(5,6)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          30
     '''

     st.code(output, language='python')

elif option == 'Swapping variable value':
     st.write('One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:')
     st.header('Example')
     
     code = '''
          a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          a = 200
b = 100
     '''

     st.code(output, language='python')

elif option == 'Use a password in your code':
     st.write('This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!')
     st.header('Example')
     
     code = '''
          from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)
     '''

     st.code(code, language='python')
     
     st.header('Output')

     output = '''
          password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password
     '''

     st.code(output, language='python')