# type casting in python
# Type casting is the process of converting a value from one data type to another. In Python, you can use built-in functions to perform type casting. The most common type casting functions are `int()`, `float()`, `str()`, and `bool()`. For example:
# Converting a string to an integer 
string_number = "42"
integer_number = int(string_number)  # This will convert the string "42" to the integer 42
print(integer_number)  # Output: 42 
# Converting a string to a float
string_float = "3.14"
float_number = float(string_float)  # This will convert the string "3.14" to the float 3.14
print(float_number)  # Output: 3.14
# Converting an integer to a string
integer_value = 100
string_value = str(integer_value)  # This will convert the integer 100 to the string "100"
print(string_value)  # Output: "100"
# Converting a float to a boolean
# only the float value 0.0 will be converted to False, while any other float value will be converted to True
float_value = 0.0
boolean_value = bool(float_value)  # This will convert the float 0.0 to the boolean False
print(boolean_value)  # Output: False
"""
    In summary, type casting is a fundamental concept in Python that allows you to convert values between different data types. Understanding how to use type casting functions effectively is essential for writing flexible and robust code that can handle various data types and perform necessary conversions when needed.
    
    """