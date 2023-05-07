# EXERCISE 1
# 1) Create a set called my_fav_numbers with all your favorites numbers.
# 2) Add two new numbers to the set.
# 3) Remove the last number.
# 4) Create a set called friend_fav_numbers with your friend’s favorites numbers.
# 5) Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = set((0, 1, 22))
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
basket.pop(2)
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)

# EXERCISE 4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
float_list = list((1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5))
print(float_list)
print(type(float_list[0]))

# EXERCISE 4
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

