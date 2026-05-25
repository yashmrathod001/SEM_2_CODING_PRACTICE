# introduction to list
# A list is a collection of items that are ordered and changeable. Lists are written with square brackets [].
# 1. Creating a list
my_list = [1, 2, 3, "Hello", True]
print("List:", my_list)
# 2. Accessing list items
print("First item:", my_list[0])  # Accessing the first item
print("Last item:", my_list[-1])  # Accessing the last item
# 3. Modifying list items
my_list[1] = "World"  # Changing the second item
print("Modified List:", my_list)
# 4. Adding items to a list
my_list.append(4.5)  # Adding an item to the end of the list
print("List after append:", my_list)
my_list.insert(2, "Python")  # Inserting an item at index 2
print("List after insert:", my_list)
# 5. Removing items from a list
my_list.remove("Hello")  # Removing an item by value
print("List after remove:", my_list)
popped_item = my_list.pop(1)  # Removing an item by index
print("Popped Item:", popped_item)
print("List after pop:", my_list)
# 6. List slicing
sliced_list = my_list[1:4]  # Slicing the list from index 1 to 3
print("Sliced List:", sliced_list)
# 7. Length of a list
length = len(my_list)

print("Length of List:", length)
# 8. List concatenation
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
concatenated_list = list1 + list2  # Concatenating two lists
print("Concatenated List:", concatenated_list)
# 9. List repetition
repeated_list = list1 * 3  # Repeating the list three times
print("Repeated List:", repeated_list)
# 10. Checking if an item exists in a list
item_exists = 2 in list1  # Checking if 2 is in list1
print("Item exists in list1:", item_exists)
item_not_exists = "d" in list2  # Checking if "d" is in list2
print("Item exists in list2:", item_not_exists) 
# 11. Iterating through a list
print("Iterating through list1:")   
for item in list1:
    print(item) 
