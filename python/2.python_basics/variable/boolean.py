# at basics to advanced level in boolean data type in python
# A boolean data type is a data type that can have one of two possible values: True or False. In Python, the boolean data type is represented by the built-in `bool` class. The `bool` class has two constant values: `True` and `False`, which are used to represent the truth values of expressions and conditions. For example:
is_sunny = True
is_raining = False
print("Is it sunny today?", is_sunny)
print("Is it raining today?", is_raining)
# You can also use boolean values in conditional statements, such as `if` statements, to control the flow of your program based on certain conditions. For example:
if is_sunny:
    print("It's a nice day to go outside!") 
else:
    print("It's better to stay indoors.")
# In addition to the `True` and `False` constants, you can also create boolean expressions using comparison operators (such as `==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (such as `and`, `or`, `not`). For example:
temperature = 25
is_warm = temperature > 20  # This will evaluate to True
is_cold = temperature < 15  # This will evaluate to False   
print("Is it warm?", is_warm)
print("Is it cold?", is_cold)
is_sunny_and_warm = is_sunny and is_warm  # This will evaluate to True
is_raining_or_cold = is_raining or is_cold  # This will evaluate to False
print("Is it sunny and warm?", is_sunny_and_warm)
print("Is it raining or cold?", is_raining_or_cold)
# You can also use the `not` operator to negate a boolean expression. For example:  
is_not_sunny = not is_sunny  # This will evaluate to False
print("Is it not sunny?", is_not_sunny)
"""
    In summary, the boolean data type in Python is a fundamental data type that allows you to represent and manipulate truth values. Understanding how to use boolean values and expressions is essential for controlling the flow of your program and making decisions based on certain conditions.
    
    """