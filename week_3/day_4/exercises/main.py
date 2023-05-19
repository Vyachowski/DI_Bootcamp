# --- 🌟 Exercise 1 – Random Sentence Generator ---
# Instructions
# Description: In this exercise we will create a random sentence generator. 
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# 1) Download this word list
# 2) Save it in your development directory.
# 3) Create a function called get_words_from_file. This function should read the file’s content and
#    return the words as a collection. What is the correct data type to store the words?
# 4) Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# 5) use the words list to get your random words.
#    the amount of words should be the value of the length parameter.
# 6) Take the random words and create a sentence (using a python method), the sentence should be lower case.
# 7) Create a function called main which will:
#    Print a message explaining what the program does.
# 8) Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. 
#    Validate your data and test your validation!
# 9) If the user inputs incorrect data, print an error message and end the program.
#    If the user inputs correct data, run your code.

# IMPORT

import os
import random

# CODE

file_example = 'sowpods.txt'

def get_source_absolute_path(file_name):
  # Get the absolute path of the current script
  current_file_path = os.path.abspath(__file__)
  # Get the directory of the current script
  current_directory = os.path.dirname(current_file_path)
  # Define the path relative to the current script
  absolute_path = os.path.join(current_directory, file_name)
  try: 
    if os.path.exists(absolute_path):
      return absolute_path
    else:
      raise ValueError(f'{file_name} doesn\'t exist in current directory')
  except ValueError as e:
    print(e)

def get_words_from_file(absolute_path):
  words_list = open(absolute_path).readlines()
  return words_list

def get_random_sentence(length):
  try:
    if type(length) != int: 
      raise ValueError(f'Length shoud be an integer')
  except ValueError as e:
    print(e)
  else:
    absolute_path = get_source_absolute_path(file_example)
    words_list = get_words_from_file(absolute_path)
    random_words = random.choices(words_list, k=length)
    random_words_without_new_lines = [word.rstrip() for word in random_words]
    sentence = ' '.join(random_words_without_new_lines).lower()
    return sentence

def main():
  print('This program can give you a random sentence based on your length input. Let\'s try!')
  try:
    user_length = int(input('Please enter a length of a sentence between 2 and 20: '))
    if (type(user_length) != int):
      raise TypeError('Please, exhale. Inhale. And explain me why didn\'t you enter a number? Not for Griffindor, sorry.')
    if 2 > user_length > 20:
      raise ValueError('The number should be between 2 and 20, I am very sorry but Griffindor is not for you')
  except (TypeError, ValueError) as e:
    print(e)
  else:
    random_sentence = get_random_sentence(user_length)
    return random_sentence

# OUPUT

print(main()) # -> entered '5' => e.g. irremovably leucemia starkness hemimorphisms bosser

# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.