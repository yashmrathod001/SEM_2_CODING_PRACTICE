# basic to advanced concepts of tuples in python    
# tuples are immutable data structures in python that can store a collection of items. They are similar to lists but cannot be modified after creation. Tuples are defined using parentheses () and can contain elements of different data types. They are often used to group related data together and can be used as keys in dictionaries or elements of sets due to their immutability. 
# 1. Creating a tuple
my_tuple = (1, 2, 3, "Hello", True) 
print("Tuple:", my_tuple)
# 2. Accessing tuple items
print("First item:", my_tuple[0])  # Accessing the first item
print("Last item:", my_tuple[-1])  # Accessing the last item
# 3. Tuple slicing
sliced_tuple = my_tuple[1:4]  # Slicing from index 1 to 3
print("Sliced Tuple:", sliced_tuple)
# 4. Length of a tuple
length = len(my_tuple)
print("Length of Tuple:", length)
# 5. Concatenating tuples   
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")    
concatenated_tuple = tuple1 + tuple2  # Concatenating two tuples
print("Concatenated Tuple:", concatenated_tuple)
# 6. Repeating a tuple
repeated_tuple = tuple1 * 3  # Repeating the tuple three times
print("Repeated Tuple:", repeated_tuple)
# 7. Checking if an item exists in a tuple  
item_exists = 2 in tuple1  # Checking if 2 is in tuple1
print("Item exists in tuple1:", item_exists)
item_not_exists = "d" in tuple2  # Checking if "d" is in tuple2
print("Item exists in tuple2:", item_not_exists)
# 8. Iterating through a tuple
print("Iterating through tuple1:")  
for item in tuple1:
    print(item) 
# 9. Unpacking a tuple
a, b, c = tuple1  # Unpacking the tuple into variables
print("Unpacked values:", a, b, c)
# 10. Using tuples as keys in a dictionary
my_dict = {(1, 2): "Value for (1, 2)", (3, 4): "Value for (3, 4)"}  # Using tuples as keys in a dictionary
print("Dictionary with tuple keys:", my_dict)   
# 11. Using tuples in sets
my_set = {(1, 2), (3, 4), (5, 6)}  # Using tuples in a set
print("Set with tuples:", my_set)   
# 12. Nested tuples
nested_tuple = ((1, 2), ("a", "b"), (True, False))  # Creating a nested tuple
print("Nested Tuple:", nested_tuple)    
# 13. Tuple methods
# Tuples have only two built-in methods: count() and index()    
# count() method counts the number of occurrences of a specified value in the tuple
count_of_item = tuple1.count(2)  # Counting occurrences of the item 
print("Count of 2 in tuple1:", count_of_item)
# index() method returns the index of the first occurrence of a specified value in the tuple
index_of_item = tuple1.index(2)  # Finding the index of the item
print("Index of 2 in tuple1:", index_of_item)   