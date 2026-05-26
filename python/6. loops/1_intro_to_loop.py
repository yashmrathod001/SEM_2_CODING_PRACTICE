#  intro duction to loops
#  loops are used to repeat a block of code multiple times  
#  there are two types of loops in python
#  for loop and while loop
#  for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects
#  while loop is used to execute a block of code as long as a condition is true
#  for loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#  while loop example
i = 0
while i < 5:
    print(i)
    i += 1
#  in the above example, the while loop will execute the block of code as long as the condition i < 5 is true
#  the output will be:  0 1 2 3 4
#  in the for loop example, the loop will iterate over the list of fruits and print each fruit
#  the output will be:  apple banana cherry
#  loops can also be nested, meaning you can have a loop inside another loop
#  nested loop example  
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
#  in the above example, the outer loop will iterate 3 times and the inner loop will iterate 2 times for each iteration of the outer loop
#  the output will be:
#  i: 0, j: 0
#  i: 0, j: 1
#  i: 1, j: 0
#  i: 1, j: 1
#  i: 2, j: 0
#  i: 2, j: 1



                