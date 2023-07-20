# --- DAILY CHALLENGE: SORTING --- #

## Instructions:
## 1) Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
##    after sorting them alphabetically.
## 2) Use List Comprehension (???)

# DATA

str = 'without,hello,bag,world'

# CODE

# Variant 1
def sorting(str, user_input = False):
  if user_input == True:
    str = input('Please type a comma-separated sequence of words: ')
  sorted_list = ','.join(sorted(str.split(',')))
  return sorted_list

# Challenge 2 : Longest Word
## Instructions
## Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
## Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(sentence):
  words_list = sentence.split()
  words_length_list = []
  for word in words_list:
    words_length_list.append(len(word))
  longest_word_number = max(words_length_list)
  max_word_index = words_length_list.index(longest_word_number)
  return words_list[max_word_index]

# TEST:
print(longest_word("Margaret's toy is a pretty doll.")) # ➞ "Margaret's"

print(longest_word("A thing of beauty is a joy forever.")) # ➞ "forever."

print(longest_word("Forgetfulness is by all means powerless!")) # ➞ "Forgetfulness"