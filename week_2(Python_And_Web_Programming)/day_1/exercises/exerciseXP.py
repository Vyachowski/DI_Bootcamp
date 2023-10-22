# EXERCISE 1
# Print the following output in one line of code:
print('Hello world\n'*5)

# EXERCISE 2
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99^3)*8)

# EXERCISE 3
# Predict the output of the following code snippets:
# I've predicted but here is the output
print(5 < 3)
print(3 == 3)
print(3 == "3")
# print('3' > 3)
print("Hello" == "hello")

# EXERCISE 4
# Create a variable called computer_brand which value is the brand name of your computer.
computer_brand = 'Apple'
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
print(f'I have an {computer_brand} computer')

# EXERCISE 5
# Create a variable called name, and set it’s value to your name.
name = 'Slava'
# Create a variable called age, and set it’s value to your age.
age = 34
# Create a variable called shoe_size, and set it’s value to your shoe size.
shoe_size = 42
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
info = (f'Surprise is that {name} is {age} years old and it\'s so close to his {shoe_size} shoe size')
# Have your code print the info message.
# Run your code
print(info)

# EXERCISE 6
# Create two variables, a and b.
# Each variable value should be a number.
a = 7
b = 6
# If a is bigger then b, have your code print Hello World.
if (a > b):
  print("Hello World!")

# EXERCISE 7
# Write code that asks the user for a number and determines whether this number is odd or even.
num = int(input("Please enter a number: "))
if (num % 2 == 0):
  print('It\'s even!')
else: 
  print('It\'s odd!')


# EXERCISE 8
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
my_name = 'Slava'
name = str(input("Please enter your name, my friend: "))

if (name == my_name):
  print('Wow! You parents are the best persons in the whole world!')

# EXERCISE 9
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.
height = int(input("Please enter your height(in inches): "))
if (height > 145):
  print('You are tall enough to ride!')
else: print('I am sorry, but this roller coaster is only for your brother')