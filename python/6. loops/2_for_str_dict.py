# for loop at basic to advance level with string and dictionary
#  for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects
#  for loop syntax
#  for variable in sequence:
#      block of code
#  for loop with string example 
name = "John"
for letter in name:
    print(letter)   
#  in the above example, the for loop will iterate over each letter in the string "John" and print it
#  the output will be:  J o h n 

#  for loop with dictionary example
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key]) 
#  in the above example, the for loop will iterate over each key in the dictionary "person" and print the key and its corresponding value
#  the output will be:
#  name John
#  age 30
#  you can also use the items() method to iterate over the key-value pairs in the dictionary
for key, value in person.items():
    print(key, value)
#  in the above example, the for loop will iterate over each key-value pair in the dictionary "person" and print the key and its corresponding value
#  the output will be:
#  name John
#  age 30   

# more examples of for loop with string and dictionary
#  for loop with string example
sentence = "Hello World"
for word in sentence.split():
    print(word)
#  in the above example, the for loop will iterate over each word in the string "Hello World" and print it
#  the output will be:  Hello World
#  for loop with dictionary example
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
for student, score in students.items():
    print(f"{student} scored {score}")  
#  in the above example, the for loop will iterate over each key-value pair in the dictionary "students" and print the student name and their corresponding score
#  the output will be:  
#  Alice scored 85
#  Bob scored 90    
#  you can also use the keys() method to iterate over the keys in the dictionary
for student in students.keys():
    print(student)  
#  in the above example, the for loop will iterate over each key in the dictionary "students" and print it
#  the output will be:
#  Alice
#  Bob
#  you can also use the values() method to iterate over the values in the dictionary
for score in students.values():
    print(score)        
#  in the above example, the for loop will iterate over each value in the dictionary "students" and print it        
#  the output will be:
#  85
#  90
#  you can also use the enumerate() function to get the index and value while iterating over a sequence
for index, student in enumerate(students.keys()):
    print(f"{index}: {student}")    
#  in the above example, the for loop will iterate over each key in the dictionary "students" and print the index and the student name
#  the output will be:      
#  0: Alice
#  1: Bob
