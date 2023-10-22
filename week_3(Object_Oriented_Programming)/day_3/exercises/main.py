# --- 🌟 Exercise 1 : Built-In Functions --- #
# Instructions:
# Python has many built-in functions.
#  – If you feel that you don’t know how to properly implement them take a look at the python documentation online.
# 1) Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# 2) Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# CODE

def display_abs_result(num):
  '''
  This function displays the absolute value of the given number. 
  If the number is positive or zero, it prints the number itself. 
  If the number is negative, it prints the negation of the number.
  '''
  print (num if num >= 0 else -num)

def display_int_result(value):
  '''
  This function prints the integer representation of the given value. 
  It discards any decimal places and outputs the integer part of the value.
  '''
  print (int(value))

def display_input_result(value):
  '''
  This function prompts the user for input by displaying the given value as a prompt.
  It then waits for the user to enter a value and press Enter. 
  Once the user input is received, it is printed to the console.
  '''
  print (input(value))

# OUTPUT

print(display_abs_result.__doc__)     # -> Docs...

print(display_int_result.__doc__)     # -> Docs...

print(display_input_result.__doc__)   # -> Docs...

# --- 🌟 Exercise 1: Currencies --- #
# Instructions:
# 1) class Currency:
#     def __init__(self, currency, amount):
#       self.currency = currency
#       self.amount = amount
#     # Your code starts HERE
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# CODE

class Currency:
  '''Class to perform an actions with any currencies'''
  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount

  def __str__(self):
    return (f'{str(self.amount)} {self.currency}s')

  def __int__(self):
    return self.amount

  def __repr__(self):
    return (f'{str(self.amount)} {self.currency}s')

  def __add__(self, other):
    if isinstance(other, Currency):
      try:
        if self.currency == other.currency:
          return (self.amount + other.amount)
        else:
          raise ValueError(f'TypeError: Cannot add between Currency Type {self.currency} and {other.currency}')
      except ValueError as e:
        print(e)
    else:
      if isinstance(other, (int, float)):
        return (self.amount + other)
      
  def __iadd__(self, other):
    if isinstance(other, Currency):
      try:
        if self.currency == other.currency:
          self.amount += other.amount
        else:
          raise TypeError(f'TypeError: Cannot add between Currency type {self.currency} and {other.currency}')
      except ValueError as e:
        print(e)
    else:
      if isinstance(other, (int, float)):
        self.amount += other
    return self

# OUTPUT

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))   # -> '5 dollars'

print(int(c1))   # -> 5

print(repr(c1))  # -> '5 dollars'

print(c1 + 5)    # -> 10

print(c1 + c2)   # -> 15

print(c1)        # -> 5 dollars

c1 += 5
print(c1)        # -> 10 dollars

c1 += c2
print(c1)        # -> 20 dollars

print(c1 + c3)   # -> TypeError: Cannot add between Currency type <dollar> and <shekel>

print(c1.__doc__)# -> Documentation

# -- 🌟 Exercise 2: Import -- #
# Instructions:
# 1) In a file named func.py create a function that adds 2 number, and prints the result
# 2) In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:
# import module_name 
# OR 
# from module_name import function_name 
# OR 
# from module_name import function_name as fn 
# OR
# import module_name as mn
from sum import calc_sum as sum
print(sum(5, 3))

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
# Instructions:
# 1) Create a function that displays the current date.
# Hint : Use the datetime module.
from datetime import datetime

def display_date():
  current_date = datetime.now().date()
  print(f'Current date is {current_date}')

print(display_date()) # -> Current date is 2023-05-19

# --- Exercise 5 : Amount Of Time Left Until January 1st --- #
# Instructions:
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01 hours).
def display_time_before_new_year():
  now = datetime.now()
  new_year = datetime(now.year + 1, 1, 1)
  time_left = new_year - now
  days = time_left.days
  hours = time_left.seconds // 3600
  minutes = (time_left.seconds % 3600) // 60
  seconds = (time_left.seconds % 3600) % 60
    
  print(f'The 1st of January is in {days} days, {hours:02d}:{minutes:02d}:{seconds:02d} hours.')

display_time_before_new_year() # -> The 1st of January is in 225 days, 07:23:05 hours.

# --- Exercise 6 : Birthday And Minutes --- #
# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def calculate_minutes_lived(birthday):
    now = datetime.now()
    birthday = datetime.strptime(birthday, '%d-%m-%Y')
    birthday_formatted = birthday.strftime('%d-%m-%Y')
    time_lived = now - birthday
    minutes_lived = int(time_lived.total_seconds() / 60)
    
    print(f'You\'ve lived {minutes_lived} minutes since {birthday_formatted}')

calculate_minutes_lived('22-03-1989') # -> You've lived 17967882 minutes since 22-03-1989

# --- Exercise 7 : Upcoming Holiday --- #
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def nearest_holiday():
    current_date = datetime.now()
    next_holiday = datetime(2023, 6, 12)
    holiday_name = 'Day of Russia'
    
    time_left = next_holiday - current_date
    total_seconds = time_left.total_seconds()
    days = time_left.days
    hours = int(total_seconds // 3600 % 24)
    minutes = int(total_seconds // 60 % 60)
    seconds = int(total_seconds % 60)
    
    print(f'Today is: {current_date.strftime("%Y-%m-%d")}')
    print(f'Next holiday is {holiday_name} in {days} days, {hours:02d}:{minutes:02d}:{seconds:02d} hours')

nearest_holiday() # -> Next holiday is Day of Russia in 22 days, 07:06:05 hours

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

def calculate_age_on_planets(seconds):
    earth_year_seconds = 31557600
    orbital_periods = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    age_on_planets = {}
    for planet, orbital_period in orbital_periods.items():
      age_on_planets[planet] = round(seconds / (earth_year_seconds * orbital_period), 2)
    return age_on_planets

print(calculate_age_on_planets(1_000_000_000))

# --- Exercise 9 : Faker Module --- #
# Instructions:
# 1) Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# 2) Create an empty list called users. Tip: It should be a list of dictionaries.
# 3) Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. 
# 4) Use faker to populate them with fake data.

from faker import Faker
import pprint

called_users = []
fake = Faker()

def add_user():
  user = {
    'name': fake.name(),
    'address': fake.address(),
    'language_code': fake.language_code()
  }
  called_users.append(user)

add_user()
add_user()
add_user()

print(pprint.pprint(called_users)) # -> [prettified dictionary with fake persons]