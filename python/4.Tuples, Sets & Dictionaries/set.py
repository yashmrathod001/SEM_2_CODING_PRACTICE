# basic to advanced concepts of sets in python
# sets are unordered collections of unique elements in python. They are defined using curly braces {} and can contain elements of different data types. Sets are mutable, meaning you can add or remove elements after creation, but they do not allow duplicate values. Sets are commonly used for membership testing, eliminating duplicate entries, and performing mathematical operations like union, intersection, and difference.
# 1. Creating a set
my_set = {1, 2, 3, "Hello", True}
print("Set:", my_set)
# 2. Adding elements to a set
my_set.add(4.5)  # Adding an element to the set 
print("Set after adding an element:", my_set)
my_set.update([5, 6, 7])  # Adding multiple elements to the set
print("Set after adding multiple elements:", my_set)
# 3. Removing elements from a set
my_set.remove("Hello")  # Removing an element from the set
print("Set after removing an element:", my_set)
my_set.discard(10)  # Discarding an element that may not exist (no error if it doesn't exist)
print("Set after discarding an element:", my_set)   
popped_element = my_set.pop()  # Removing and returning an arbitrary element from the set
print("Popped Element:", popped_element)    
print("Set after popping an element:", my_set)
# 4. Set operations 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6} 
union_set = set1.union(set2)  # Union of two sets
print("Union of set1 and set2:", union_set)     
intersection_set = set1.intersection(set2)  # Intersection of two sets
print("Intersection of set1 and set2:", intersection_set)   
difference_set = set1.difference(set2)  # Difference of two sets
print("Difference of set1 and set2:", difference_set)   
symmetric_difference_set = set1.symmetric_difference(set2)  # Symmetric difference of two sets
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)       
# 5. Checking if a set is a subset or superset of another set
is_subset = set1.issubset(union_set)  # Checking if set1 is a subset of the union set       
print("Is set1 a subset of the union set?", is_subset)
is_superset = union_set.issuperset(set1)  # Checking if the union set is a superset of set1
print("Is the union set a superset of set1?", is_superset)
# 6. Iterating through a set
print("Iterating through set1:")    
for item in set1:
    print(item)
# 7. Length of a set
length = len(set1)  
print("Length of set1:", length)
# 8. Checking if an item exists in a set    
item_exists = 2 in set1  # Checking if 2 is in set1
print("Item exists in set1:", item_exists)  
item_not_exists = 10 in set1  # Checking if 10 is in set1
print("Item exists in set1:", item_not_exists)  
# 9. Clearing a set 
my_set.clear()  # Removing all elements from the set
print("Set after clear:", my_set)
# 10. Copying a set
copied_set = set1.copy()  # Creating a copy of set1 
print("Copied Set:", copied_set)
                