"""
note:

variable is a name that refers to a value. It is a way to store and manipulate data in a program.
In Python, you can create a variable by assigning a value to it using the assignment operator (=). 

rules for naming variables in Python:
1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. Variable names can contain letters, digits (0-9), and underscores.
3. Variable names cannot start with a digit.
4. Variable names are case-sensitive (e.g., myVariable and myvariable are different variables


For example:
x = 10
y = "Hello, World!"
In this example, we have created two variables: x and y. The variable x is assigned the value 10, which is an integer, and the variable y is assigned the value "Hello, World!", which is a string.
You can also perform operations on variables. For example:
z = x + 5
print(z)
In this example, we have created a new variable z that is the result of adding 5 to the value of x. The output of this code will be 15.
Variables can also be reassigned to new values. For example:
x = 20
print(x)        
In this example, we have reassigned the variable x to a new value of 20. The output of this code will be 20.
Variables can also be of different types, such as integers, floats, strings, lists, dictionaries, and more. The type of a variable is determined by the value it holds. You can check the type of a variable using the built-in type() function. For example:
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>

"""

a = 10 #integer 
b = 20.1 #float
c = "Hello, World!" #string
is_student = True #boolean

"""
using the print() function to display the values of the variables
print(a)  # Output: 10
print(b)  # Output: 20.1        
print(c)  # Output: Hello, World!
print(is_student)  # Output: True
"""
print(a)  # Output: 10
print(b)  # Output: 20.1
print(c)  # Output: Hello, World!
print(is_student)  # Output: True

# change the value of a variable
a = 15
print(a)  # Output: 15
# check the type of a variable
print(type(a))  # Output: <class 'int'> 
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>



