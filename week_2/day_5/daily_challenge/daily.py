# --- DAILY CHALLENGE: SORTING --- #

## Instructions:
## 1) Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
#     after sorting them alphabetically.
## 2) Use List Comprehension (???)

# DATA

str = 'without,hello,bag,world'

# LOGIC

# Variant 1
def sorting(str, user_input = False):
  if user_input == True:
    str = input('Please type a comma-separated sequence of words: ')
  sorted_list = ','.join(sorted(str.split(',')))
  return sorted_list
