import random
# CHALLENGE 1
# Using the input function, ask the user for a string. The string must be 10 characters long.
# 1) Ask the user for a number and a length.
# 2) Create a program that prints a list of multiples of the number until the list length reaches length.
#    Eg: 
#    number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
#    number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#    number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
start_point = int(input('For this trick I need a number. Your choice is: '))
length = int(input('And a length: '))
numbers = []
acc = 0
while length > len(numbers):
  acc += start_point
  numbers.append(acc)
print(numbers)

# CHALLENGE 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples
# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

# First variant
word = input('Give me a word, please, with any duplicate consecutive letters, for instance\'ppoeeemm\': ')
letters_list = list(word)
print(letters_list)
final_list = []
for letter in letters_list:
  if (letter not in final_list):
    final_list.append(letter)
corrected_word1 = ''.join(final_list)
print(corrected_word1)

# Second variant
word = input('Give me a word, please, with any duplicate consecutive letters, for instance\'ppoeeemm\': ')
letters_list = list(word)
removed_duplicates_list = list(dict.fromkeys(letters_list))
print(removed_duplicates_list)
corrected_word = ''.join(removed_duplicates_list)
print(corrected_word)