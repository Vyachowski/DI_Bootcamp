# EXERCISE 1
# 1) Create a set called my_fav_numbers with all your favorites numbers.
# 2) Add two new numbers to the set.
# 3) Remove the last number.
# 4) Create a set called friend_fav_numbers with your friend’s favorites numbers.
# 5) Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = { 0, 1, 22 }
my_fav_numbers.add(222)
my_fav_numbers.add(2222)
my_fav_numbers.pop()
friends_fav_numbers = set((561, 14, 2222))
our_fav_numbers = my_fav_numbers.union(friends_fav_numbers)
print(our_fav_numbers)

# EXERCISE 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
print('No, because a tuple is not able to be changed')

# EXERCISE 3
# 1) Remove “Banana” from the list.
# 2) Remove “Blueberries” from the list.
# 3) Add “Kiwi” to the end of the list.
# 4) Add “Apples” to the beginning of the list.
# 5) Count how many apples are in the basket.
# 6) Empty the basket.
# 7) Print(basket)
basket = ['Banana', 'Apples', 'Oranges', 'Blueberries'];
basket.remove('Banana')
basket.pop()
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)

# EXERCISE 4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
float_list = [num * 0.5 for num in range(3, 11)]
print(float_list)

# EXERCISE 5
# 1) Use a for loop to print all numbers from 1 to 20, inclusive.
# 2) Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for number in range(1, 21):
  print(number)
for number in range(1, 21):
  print(number) if  number % 2 == 0 else False

# EXERCISE 6
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = 'slava'
users_name = ''
while (users_name != name):
  users_name = input('May I have your name, sir: ').lower()

# EXERCISE 7
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. 'apple mango cherry'.
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
fruit_list = input('May I know your favorites fruits, sir (separate it with a space, please): ').lower().split(' ')
favourite_fruit = input('Name the fruit, sir (only one)): ').lower()
if (favourite_fruit in fruit_list):
    print('You chose one of your favorite fruits! Enjoy!')
else: 
   print('You chose a new fruit. I hope you enjoy')

# EXERCISE 8
# 1) Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# 2) As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 3) Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
toppings_list = []
exit_request = False
while (exit_request == False):
  new_topping = input('Please enter a topping, that you want add to your pizza (one at a time, to stop adding pleaser print \'quit\'): ')
  if (new_topping.lower() != 'quit'):
    toppings_list.append(new_topping)
    print(f'You\'ve added {new_topping} to the pizza!')
  else:
    print(f'Total price is: {10 + 0.25 * len(toppings_list)}' )
    exit_request = True

# EXERCISE 9: CINEMAX
# 1) A movie theater charges different ticket prices depending on a person’s age.
#    – if a person is under the age of 3, the ticket is free.
#    – if they are between 3 and 12, the ticket is $10.
#    – if they are over the age of 12, the ticket is $15.

# 2) Ask a family the age of each person who wants a ticket.

# 3) Store the total cost of all the family’s tickets and print it out.

# 4) A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#    Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#    At the end, print the final list.
family = ['father', 'mother', 'daughter']
total_cost = 0
for member in family:
  age = int(input('What is your age: '))
  if (age >= 3 and age <= 12):
    total_cost += 10
  if (age > 12):
    total_cost += 15
print(f'${total_cost}')
    
# EXERCISE 10 : SANDWICH ORDERS
# 1) Use the above list called sandwich_orders.
# 2) Make an empty list called finished_sandwiches.
# 3) As each sandwich is made, move it to the list of finished sandwiches.
# 4) After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
sandwich_orders = ['Tuna sandwich', 'Avocado sandwich', 'Egg sandwich', 'Sabih sandwich', 'Pastrami sandwich']
finished_sandwiches= list()
for sandwich in sandwich_orders:
  finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
  print(f'Your {sandwich} is ready!')


# EXERCISE 11 : SANDWICH ORDERS ADVANCED
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwiches_order = ['Pastrami sandwich', 'Tuna sandwich', 'Avocado sandwich', 'Pastrami sandwich', 'Egg sandwich', 'Sabih sandwich', 'Pastrami sandwich']
print('I am very sorry, but we are out of pastrami. We will prepare your order without it')
finished_sandwiches_without_pastrami = sandwiches_order[:]
while ('Pastrami sandwich' in finished_sandwiches_without_pastrami):
  finished_sandwiches_without_pastrami.remove('Pastrami sandwich')
print(finished_sandwiches_without_pastrami)