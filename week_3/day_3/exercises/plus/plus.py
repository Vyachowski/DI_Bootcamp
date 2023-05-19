# --- FOR NOW ONLY NECESSARY EXERCISE --- #
# SPENT TOO MUCH TIME ON PAGINATION EXERCISE #
# FIRST TASK IS IN ANOTHER FILES – AS DESCRIBED IN INTSTRUCTION #


# --- 🌟 Exercise 2: Random Module --- #
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
import random

def guess_random_number(user_number):
  random_number = random.randint(1, 100)
  
  if user_number == random_number:
    return f'Congratulations! Your guess is right:'
  else:
    return 'Sorry, not even close pal :('

# --- 🌟 Exercise 3: String Module --- #
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
import string

letters = string.ascii_uppercase + string.ascii_lowercase
random_string = ''.join([random.choice(letters) for _ in range(5)])

print(random_string) # -> e.g. 'fELch'

# --- 🌟 Exercise 4 : Current Date --- #
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.


# --- Exercise 5 : Amount Of Time Left Until January 1st --- #
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


# --- Exercise 6 : Birthday And Minutes --- #
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


# --- Exercise 7 : Upcoming Holiday --- #
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.


# --- Exercise 8 : How Old Are You On Jupiter? --- #
# Instructions:
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.



# --- Exercise 9 : Faker Module --- #
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.