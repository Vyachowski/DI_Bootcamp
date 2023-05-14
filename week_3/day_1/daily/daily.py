import random
# EXERCISE 1
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
str = input('Please enter a sentence: ')
if (len(str) < 10):
  print('String is not long enough')
elif (len(str) > 10):
  print('String is too long')
else: print('Well done!')

# EXERCISE 2
# Then, print the first and last characters of the given text.
print(f'First letter is: {str[0]}')
print(f'Last letter is: {str[-1]}')

# # EXERCISE 3
# Using a for loop, construct the string character by character: Print the first character, then the second, 
# then the third, until the full string is printed.
result = ''
for sym in str:
  result = result + sym
  print(result)

# EXERCISE 4
# Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).
str_list = list(str)
random.shuffle(str_list)
str_shuffled = ''.join(str_list)
print(str_shuffled)
# result = ''
# for sym in str_shuffled:
#   result = result + sym
#   print(result)