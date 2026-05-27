# 10 hard practice problems for if elif else statements in python with full explanation and code
# 1. Write a program to check if a number is positive, negative or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    
# 2. Write a program to check if a year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
    print(f"{year} is a leap year.")   
else:    print(f"{year} is not a leap year.")
# 3. Write a program to check if a number is even or odd.       
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# 4. Write a program to check if a person is eligible to vote or not.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# 5. Write a program to check if a number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:    print(f"{num} is not a prime number.")
# 6. Write a program to check if a string is a palindrome or not.   
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:    print(f"{string} is not a palindrome.")
# 7. Write a program to check if a number is a perfect square or not.
num = int(input("Enter a number: "))
if num >= 0:
    if int(num**0.5)**2 == num:
        print(f"{num} is a perfect square.")
    else:
        print(f"{num} is not a perfect square.")
else:    print(f"{num} is not a perfect square.")
# 8. Write a program to check if a number is a perfect cube or not.
num = int(input("Enter a number: "))    
if num >= 0:
    if int(num**(1/3))**3 == num:
        print(f"{num} is a perfect cube.")
    else:
        print(f"{num} is not a perfect cube.")
else:    print(f"{num} is not a perfect cube.")
# 9. Write a program to check if a number is a multiple of 3 or not.
num = int(input("Enter a number: "))    
if num % 3 == 0:
    print(f"{num} is a multiple of 3.") 
else:    print(f"{num} is not a multiple of 3.")
# 10. Write a program to check if a number is a multiple of 5 or not.
num = int(input("Enter a number: "))        
if num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:    print(f"{num} is not a multiple of 5.")



# one of the hardest problem to self practice for if elif else statements in python with full explanation and code
# Write a program to check if a number is a perfect number or not.
num = int(input("Enter a number: "))
if num > 1:
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
else:    print(f"{num} is not a perfect number.")




