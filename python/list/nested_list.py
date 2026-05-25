# nested list   
# A nested list is a list that contains other lists as its elements. Nested lists can be used to represent complex data structures, such as matrices or tables.
# 1. Creating a nested list 
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Nested List:", nested_list)  
# 2. Accessing elements in a nested list
print("First sublist:", nested_list[0])  # Accessing the first sublist      
print("Second item of the first sublist:", nested_list[0][1])  # Accessing the second item of the first sublist
print("Third item of the second sublist:", nested_list[1][2])  #            
print("First item of the third sublist:", nested_list[2][0])  # Accessing the first item of the third sublist
# 3. Modifying elements in a nested list                    
nested_list[0][1] = "Modified"  # Modifying the second item of the first sublist                
print("Nested List after modification:", nested_list)           
# 4. Adding elements to a nested list           
nested_list[1].append("d")  # Adding an item to the second sublist
print("Nested List after adding an item:", nested_list)
nested_list.append(["New", "Sublist"])  # Adding a new sublist to the nested list
print("Nested List after adding a new sublist:", nested_list)   
# 5. Removing elements from a nested list
nested_list[0].remove("Modified")  # Removing an item from the first sublist    
print("Nested List after removing an item:", nested_list)
nested_list.pop(1)  # Removing the second sublist       
print("Nested List after removing a sublist:", nested_list) 
# 6. Iterating through a nested list
print("Iterating through nested list:") 
for sublist in nested_list:
    for item in sublist:
        print(item) 


        