# basics to advanced f-string  in python
# f-string (explanation : F-strings, also known as formatted string literals, are a way to embed expressions inside string literals using curly braces {}. They were introduced in Python 3.6 and provide a more concise and readable way to format strings compared to the older format() method. F-strings allow you to include variables, expressions, and even function calls directly within the string, making it easier to create dynamic and formatted output.)
name = "Alice"
age = 30
height = 5.5
# basic f-string usage
print(f"My name is {name}, I am {age} years old, and I am {height} feet tall.")
# f-string with expressions     
print(f"In 5 years, I will be {age + 5} years old.")
# f-string with function calls
def greet(name):
    return f"Hello, {name}!"
print(f"{greet(name)} Welcome to the world of f-strings.")
# f-string with formatting options
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.") # formats pi to 2 decimal places
# f-string with conditional expressions
is_student = True
print(f"{name} is {'a student' if is_student else 'not a student'}.")
# f-string with nested expressions
print(f"The length of my name is {len(name)} characters.")
# f-string with multiple lines
multi_line_string = f"""My name is {name},  
I am {age} years old,
and I am {height} feet tall."""
print(multi_line_string)    