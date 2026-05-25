# slicing the strings 
# syntax : string[start:step]
# explanation : String slicing allows you to extract a portion of a string by specifying the start index, stop index, and step. The start index is the position where the slicing begins (inclusive), the stop index is the position where the slicing ends (exclusive), and the step determines the interval between characters in the slice. If you omit the start index, it defaults to 0, and if you omit the stop index, it defaults to the length of the string. You can also use negative indices to slice from the end of the string.
my_string = "Hello, World!"
# slicing from index 0 to 4 (not including index 5)
print(my_string[0:5]) # Hello
# slicing from index 7 to the end of the string
print(my_string[7:13]) # World!
# slicing from the beginning of the string to index 4 (not including index 5)
print(my_string[:5]) # Hello
# slicing with a step of 2 (every second character)
print(my_string[::2]) # Hlo ol!
# slicing with a negative step (reversing the string)
print(my_string[::-1]) # !dlroW ,olleH

# more examples of slicing for syntax [start:stop:step]
# slicing from index 2 to index 8 with a step of 2
print(my_string[2:9:2]) # l,W   
# slicing from index 1 to index 10 with a step of 3
print(my_string[1:11:3]) # e,o
# slicing from index 0 to index 12 with a step of 4
print(my_string[0:13:4]) # H,o
# slicing from index 5 to index 0 with a negative step of 1
print(my_string[5:0:-1]) # ,olleH
# slicing from index 12 to index 0 with a negative step of 2    
print(my_string[12:0:-2]) # !o lH
