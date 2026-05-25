# List operations - slicing, concat, repeat, append, insert ,- extend, remove, pop , clear, index, count, sort, reverse, copy , Numerical operations on list elements 
# 1. Slicing a list
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  # Slicing from index 1 to 3
print("Sliced List:", sliced_list)
# 2. Concatenating lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
concatenated_list = list1 + list2  # Concatenating two lists
print("Concatenated List:", concatenated_list)
# 3. Repeating a list
repeated_list = list1 * 3  # Repeating the list three times
print("Repeated List:", repeated_list)
# 4. Appending an item to a list
my_list.append(6)  # Adding an item to the end of the list
print("List after append:", my_list)
# 5. Inserting an item at a specific index
my_list.insert(2, "Hello")  # Inserting an item at index 2
print("List after insert:", my_list)
# 6. Extending a list with another list
my_list.extend([7, 8, 9])  # Extending the list with another list
print("List after extend:", my_list)    
# 7. Removing an item by value
my_list.remove("Hello")  # Removing an item by value    
print("List after remove:", my_list)
# 8. Removing an item by index  
popped_item = my_list.pop(2)  # Removing an item by index
print("Popped Item:", popped_item)  
print("List after pop:", my_list)
# 9. Clearing a list    
my_list.clear()  # Removing all items from the list
print("List after clear:", my_list)
# 10. Finding the index of an item
index_of_item = list1.index(2)  # Finding the index of the item 
print("Index of 2 in list1:", index_of_item)
# 11. Counting occurrences of an item       
count_of_item = list1.count(2)  # Counting occurrences of the item
print("Count of 2 in list1:", count_of_item)    
# 12. Sorting a list
unsorted_list = [3, 1, 4, 2]    
unsorted_list.sort()  # Sorting the list in ascending order
print("Sorted List:", unsorted_list)        
# 13. Reversing a list
unsorted_list.reverse()  # Reversing the list   
print("Reversed List:", unsorted_list)
# 14. Copying a list    
copied_list = list1.copy()  # Creating a copy of the list
print("Copied List:", copied_list)  
# 15. Numerical operations on list elements
numbers = [1, 2, 3, 4, 5]       
squared_numbers = [x**2 for x in numbers]  # Squaring each element in the list
print("Squared Numbers:", squared_numbers)  
cubed_numbers = [x**3 for x in numbers]  # Cubing each element in the list      
print("Cubed Numbers:", cubed_numbers)      
sum_of_numbers = sum(numbers)  # Calculating the sum of the list elements
print("Sum of Numbers:", sum_of_numbers)    
average_of_numbers = sum(numbers) / len(numbers)  # Calculating the average of the list elements
print("Average of Numbers:", average_of_numbers)    
max_number = max(numbers)  # Finding the maximum number in the list
print("Maximum Number:", max_number)        
min_number = min(numbers)  # Finding the minimum number in the list
print("Minimum Number:", min_number)        
