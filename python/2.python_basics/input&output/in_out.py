
# input function (explanation : The input() function is used to take user input from the console. It reads a line of text entered by the user and returns it as a string. You can also provide a prompt message to guide the user on what to enter.)
name = input("Enter your name: ")
print("Hello, " + name + "!")
# output function (explanation : The print() function is used to display output to the console. It can take multiple arguments and will convert them to strings and concatenate them with a space in between by default. You can also use formatted strings or f-strings for more complex output formatting.)
print("This is a simple output.")
# formatted output (explanation : You can use the format() method or f-strings to create formatted output. The format() method allows you to insert values into a string using placeholders, while f-strings provide a more concise syntax for embedding expressions inside string literals.)
age = 25    
print("I am {} years old.".format(age))
# f-string formatted output (explanation : F-strings, introduced in Python 3.6, allow you to embed expressions inside string literals using curly braces {}. They provide a more readable and concise way to format strings compared to the format() method.)
height = 5.9
print(f"I am {height} feet tall.")
