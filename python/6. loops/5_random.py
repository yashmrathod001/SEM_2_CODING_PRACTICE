# the explanation of Random module in Python
#  the random module in Python provides functions for generating random numbers and performing random operations
#  you can use the random module to generate random integers, random floating-point numbers, and random choices from a sequence
#  to use the random module, you need to import it first
import random
#  example of generating a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)
#  in the above example, the randint() function from the random module will generate a random integer between 1 and 10 (inclusive) and print it
#  example of generating a random floating-point number between 0 and 1 
random_float = random.random()
print(random_float)
#  in the above example, the random() function from the random module will generate a random floating-point number between 0 and 1 and print it
#  example of generating a random choice from a list
fruits = ["apple", "banana", "cherry"]
random_fruit = random.choice(fruits)
print(random_fruit)
#  in the above example, the choice() function from the random module will select a random element from the list of fruits and print it
#  example of generating a random sample from a list
numbers = [1, 2, 3, 4, 5]
random_sample = random.sample(numbers, 3)
print(random_sample)
#  in the above example, the sample() function from the random module will select a random sample of 3 elements from the list of numbers and print it
#  example of shuffling a list randomly 
random.shuffle(fruits)
print(fruits)   
#  in the above example, the shuffle() function from the random module will shuffle the list of fruits randomly and print the shuffled list
#  you can also use the random module to generate random numbers with a specific distribution, such as normal distribution, uniform distribution, etc.
#  example of generating a random number with a normal distribution
random_normal = random.normalvariate(0, 1)
print(random_normal)
#  in the above example, the normalvariate() function from the random module will generate a random number with a normal distribution with a mean of 0 and a standard deviation of 1 and print it       

# some more examples of using the random module in Python
#  example of generating a random integer between 1 and 100 (inclusive)
random_integer = random.randint(1, 100) 
print(random_integer)
#  in the above example, the randint() function from the random module will generate a random integer between 1 and 100 (inclusive) and print it
#  example of generating a random floating-point number between 0 and 10
random_float = random.uniform(0, 10)
print(random_float)
#  in the above example, the uniform() function from the random module will generate a random floating-point number between 0 and 10 and print it
#  example of generating a random choice from a string  
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter = random.choice(letters)
print(random_letter)
#  in the above example, the choice() function from the random module will select a random character from the string of letters and print it
#  example of generating a random sample from a string
random_sample = random.sample(letters, 5)
print(random_sample)
#  in the above example, the sample() function from the random module will select a random sample of 5 characters from the string of letters and print it
#  example of shuffling a string randomly   
letters_list = list(letters)
random.shuffle(letters_list)                
shuffled_letters = ''.join(letters_list)
print(shuffled_letters)     
#  in the above example, the shuffle() function from the random module will shuffle the list of letters randomly and then the join() method will convert the shuffled list back to a string and print it    
