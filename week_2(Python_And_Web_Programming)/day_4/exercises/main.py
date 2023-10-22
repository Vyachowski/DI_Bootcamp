# 🌟 EXERCISE 1 : What are you learning?
## Instructions
## 1) Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
## 2) Call the function, and make sure the message displays correctly.
def display_messsage():
  print('My creed is to upgrade and organize. The best way to give it to the world is to write a code.')

display_messsage()

# 🌟 EXERCISE 2 : What is your favourite book?
## Instructions
## 1) Write a function called favorite_book() that accepts one parameter called title.
## 2) The function should print a message, such as "One of my favorite books is <title>".
def favourite_book(title):
  print(f'One of my favorite books is {title}')

favourite_book('Alice in Wonderland') # => “One of my favorite books is Alice in Wonderland”

# 🌟 EXERCISE 3 : Some Geography
## Instructions
## 1) Write a function called describe_city() that accepts the name of a city and its country as parameters.
## 2) The function should print a simple sentence, such as "<city> is in <country>".
## 3) For example “Reykjavik is in Iceland”
## 4) Give the country parameter a default value.
## 5) Call your function.
def describe_city(city, country = 'Israel'):
  print(f'{city} is in {country}')

describe_city('Eilat')
describe_city('Eilat', 'Egypt')

# EXERCISE 4 : Random
## Instructions
## 1) Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
## 2) Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random

def equality_randomizer(number = 1):
  if type(number) != int or number > 100:
    return "You shall not pass!"
  random_number = random.randint(1,100)
  if number != random_number:
    print(f'First number was {number} and second number was {random_number}')
  else: 
    print('Congratulations, it\'s a match!')

equality_randomizer(2)

# 🌟 EXERCISE 5 : Let’s Create Some Personalized Shirts!
## Instructions
## 1) Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
## 2) The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
## 3) Call the function make_shirt().
## 4) Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
## 5) Make a large shirt with the default message
## 6) Make medium shirt with the default message
## 7) Make a shirt of any size with a different message.
## 8) Bonus: Call the function make_shirt() using keyword arguments.
def make_shirt(size = 'L', message_text = 'I love Python'):
  print(f'The size of the shirt is {size} and the text is {message_text}')

make_shirt()
make_shirt('M')
make_shirt('M','The truth is that I love JavaScript')

# 🌟 EXERCISE 6 : Magicians …
## Instructions
## 1) Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
## 2) Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
## 3) Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
## 4) Call the function make_great().
## 5) Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_list):
  for magician in magician_list:
    print(magician)

def make_great():
  for magician in enumerate(magician_names):
    magician_names[magician[0]] = 'the Great ' + magician[1]

show_magicians(magician_names)
make_great()
show_magicians(magician_names)

# 🌟 EXERCISE 7 : Temperature Advice
## Instructions
## 1) Create a function called get_random_temp().
## 2) This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
## 3) Test your function to make sure it generates expected results.
## 4) Create a function called main().
## 5) Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
## 6) Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
## 7) Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
##    – below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
##    – between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
##    – between 16 and 23
##    – between 24 and 32
##    – between 32 and 40
## 8) Change the get_random_temp() function:
##    – Add a parameter to the function, named ‘season’.
##    – Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
## 11) Now that we’ve changed get_random_temp(), let’s change the main() function:
##     – Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
##     – Use the season as an argument when calling get_random_temp().
## Bonus: Give the temperature as a floating-point number instead of an integer.
## Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
def get_random_temp(season):
  if season == 'winter':
    return random.randint(-10,16)
  elif season == 'autumn':
    return random.randint(17, 23)
  elif season == 'spring':
    return random.randint(24, 32)
  elif season == 'summer':
    return random.randint(33, 41)

def main():
  season = input('What season do you prefer? Pleasy type in: ')
  temp = get_random_temp(season)
  print(f'The temperature right now is {temp} degrees Celsius.')
  if temp < 0:
    print('Brrr, that’s freezing! Wear some extra layers today')
  elif 0 < temp <= 16:
    print('Quite chilly! Don’t forget your coat')
  elif 16 < temp <= 23:
    print('To coat or not to coat? Hard to decise')
  elif 23 < temp <= 32:
    print('Grab a hoodie for the evening, my friend.')
  else:
    print('Welcome to Eilat, please use a sun protection and wear a sunglasses!')

print(get_random_temp('spring'))
main()