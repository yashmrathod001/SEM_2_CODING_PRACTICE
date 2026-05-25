# basics to advance dictionary  
# dictionaries are mutable data structures in python that store key-value pairs. They are defined using curly braces {} and can contain elements of different data types. Dictionaries are used to store and retrieve data based on unique keys, making them efficient for lookups and data manipulation.
# 1. Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)
# 2. Accessing dictionary values
print("Name:", my_dict["name"])  # Accessing value using key
print("Age:", my_dict.get("age"))  # Accessing value using get() method
# 3. Modifying dictionary values    
my_dict["age"] = 31  # Modifying the value of an existing key
print("Modified Dictionary:", my_dict)
# 4. Adding new key-value pairs to a dictionary
my_dict["country"] = "USA"  # Adding a new key-value pair   
print("Dictionary after adding a new key-value pair:", my_dict)
# 5. Removing key-value pairs from a dictionary
del my_dict["city"]  # Removing a key-value pair using del statement
print("Dictionary after removing a key-value pair:", my_dict)   
my_dict.pop("age")  # Removing a key-value pair using pop() method
print("Dictionary after popping a key-value pair:", my_dict)
# 6. Iterating through a dictionary
print("Iterating through dictionary keys:")
for key in my_dict:
    print(key)
print("Iterating through dictionary values:")
for value in my_dict.values():
    print(value)
print("Iterating through dictionary key-value pairs:")      
for key, value in my_dict.items():
    print(f"{key}: {value}")    
# 7. Checking if a key exists in a dictionary
key_exists = "name" in my_dict  # Checking if "name" is a key in the dictionary
print("Key 'name' exists in the dictionary:", key_exists)   
key_not_exists = "age" in my_dict  # Checking if "age" is a key in the dictionary
print("Key 'age' exists in the dictionary:", key_not_exists)    
# 8. Length of a dictionary
length = len(my_dict)  # Getting the number of key-value pairs in the dictionary
print("Length of the dictionary:", length)
# 9. Copying a dictionary
copied_dict = my_dict.copy()  # Creating a copy of the dictionary
print("Copied Dictionary:", copied_dict)    
# 10. Clearing a dictionary
my_dict.clear()  # Removing all key-value pairs from the dictionary
print("Dictionary after clear:", my_dict)


    