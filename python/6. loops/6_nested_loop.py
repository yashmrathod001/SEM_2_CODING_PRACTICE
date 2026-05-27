# introduction to nested loops explanation and examples
#  nested loops are loops that are inside another loop  
#  the inner loop will be executed for each iteration of the outer loop
#  example of nested loops  
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")    
#  in the above example, the outer loop will iterate 3 times and the inner loop will iterate 2 times for each iteration of the outer loop
#  the output will be:
#  i: 0, j: 0
#  i: 0, j: 1
#  i: 1, j: 0
#  i: 1, j: 1   
#  you can also use nested loops with other types of loops, such as while loops
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1
#  in the above example, the outer while loop will execute as long as the condition i < 3 is true and the inner while loop will execute as long as the condition j < 2 is true for each iteration of the outer loop
#  the output will be:  
#  i: 0, j: 0
#  i: 0, j: 1
#  i: 1, j: 0
#  i: 1, j: 1
#  you can also use nested loops with for loops and while loops together
for i in range(3):
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}")
        j += 1  
#  in the above example, the outer for loop will iterate 3 times and the inner while loop will execute as long as the condition j < 2 is true for each iteration of the outer loop
#  the output will be:  
#  i: 0, j: 0
#  i: 0, j: 1
#  i: 1, j: 0
#  i: 1, j: 1
#  you can also use nested loops to iterate over multi-dimensional data structures, such as lists of lists or dictionaries of dictionaries
#  example of using nested loops to iterate over a list of lists    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      
for row in matrix:
    for element in row:
        print(element)  
#  in the above example, the outer loop will iterate over each row of the matrix and the inner loop will iterate over each element in the row and print it
#  the output will be:  
#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9
#  example of using nested loops to iterate over a dictionary of dictionaries
data = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
    "person3": {"name": "Charlie", "age": 35}
}   
for person, info in data.items():
    print(f"{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
#  in the above example, the outer loop will iterate over each key-value pair in the dictionary "data" and print the person name, and the inner loop will iterate over each key-value pair in the inner dictionary "info" and print the key and its corresponding value
#  the output will be:
#  person1: 
#    name: Alice
#    age: 30    
#  person2:
#    name: Bob
#    age: 25
#  person3:
#    name: Charlie      
#  you can also use nested loops to create patterns or perform calculations 
