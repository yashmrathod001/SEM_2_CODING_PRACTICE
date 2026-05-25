# operations on string
# 1. concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)
# 2. repetition
str3 = "Python"
result = str3 * 3
print("Repetition:", result)
# 3. slicing
str4 = "Programming"
result = str4[0:6]  # Extracts "Progra"mming
print("Slicing:", result)
# 4. length
str5 = "Hello, World!"
length = len(str5)
print("Length:", length)
# 5. case conversion    
str6 = "Python Programming"
upper_case = str6.upper()   
lower_case = str6.lower()
print("Upper Case:", upper_case)
print("Lower Case:", lower_case)
# 6. find and replace   
str7 = "I love Python programming"
find_index = str7.find("Python")  # Returns the index of the first occurrence
replaced_str = str7.replace("Python", "Java")  # Replaces "Python" with "Java"
print("Find Index:", find_index)
print("Replaced String:", replaced_str)
# 7. split and join
str8 = "Hello, World, Python"
split_str = str8.split(", ")  # Splits the string into a list   
joined_str = " - ".join(split_str)  # Joins the list into a string with " - " as a separator
print("Split String:", split_str)
print("Joined String:", joined_str)
# 8. string formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."  
print("Formatted String:", formatted_str)

