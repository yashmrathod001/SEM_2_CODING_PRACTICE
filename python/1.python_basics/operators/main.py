#introduction to operators
#operators are used to perform operations on variables and values

# typre of operators
#1. arithmetic operators
#2. assignment operators
#3. comparison operators
#4. logical operators
#5. bitwise operators


#1. arithmetic operators(define the basic mathematical operations)
# +(addition), -(substraction), *(multiplication), /(division), %(reminder ), **( power), //(int division)
a = 10
b = 3
print(a + b) #13
print(a - b) #7
print(a * b) #30
print(a / b) #3.3333333333333335
print(a % b) #1
print(a ** b) #1000
print(a // b) #3

#2. assignment operators(used to assign values to variables)
# = (assignment), += (add and assign), -= (subtract and assign), *= (multiply and assign), /= (divide and assign), %= (modulo and assign), **= (power and assign), //= (integer divide and assign)
a = 10
a += 5 # a = a + 5
print(a) #15
a -= 3 # a = a - 3
print(a) #12
a *= 2 # a = a * 2
print(a) #24
a /= 4 # a = a / 4
print(a) #6.0
a %= 5 # a = a % 5
print(a) #1.0
a **= 3 # a = a ** 3
print(a) #1.0   
a //= 2 # a = a // 2
print(a) #0.0

#3. comparison operators(used to compare values)
# == (equal), != (not equal), > (greater than), < (less than), >= (greater than or equal), <= (less than or equal)
a = 10
b = 5
print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a < b) #False
print(a >= b) #True 
print(a <= b) #False

#4. logical operators(used to combine conditional statements)
# and, or, not
# the mean of and is that both conditions must be true for the result to be true
# the mean of or is that at least one condition must be true for the result to be true
# the mean of not is that it negates the value of the condition
a = True
b = False
print(a and b) #False
print(a or b) #True
print(not a) #False
print(not b) #True

#5. bitwise operators(used to perform bitwise operations)
# &, |, ^, ~, <<, >>
a = 5 # 0101
b = 3 # 0011
print(a & b) # 1 (0001)
print(a | b) # 7 (0111)
print(a ^ b) # 6 (0110)
print(~a) # -6 (1010)
print(a << 1) # 10 (1010)
print(a >> 1) # 2 (0010)



