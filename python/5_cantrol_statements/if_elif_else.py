# it is file for learning if elif else statements in python it the basic to advanced  level with full explanation, code and example
# if statement is used to check a condition and execute a block of code if the condition is true
# elif statement is used to check multiple conditions and execute a block of code if any of the conditions is true
# else statement is used to execute a block of code if all the conditions are false 
# syntax of if statement
# if condition: 
#     block of code
# syntax of if elif else statement  
# if condition1:
#     block of code1    
# elif condition2:
#     block of code2    
# else:
#     block of code3    
# example of if statement
age = 18        
if age >= 18:
    print("You are eligible to vote.")  
# example of if elif else statement
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# example of if statement with multiple conditions
num = 10
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
# example of if statement with nested conditions
num = 15    

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")




            