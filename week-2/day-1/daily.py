import random
# Exercise 1
str = input("Please enter a sentence: ")
if (len(str) < 10):
  print('String is not long enough')
elif (len(str) > 10):
  print('String is too long')
else: print('Well done!')

# Exercise 2
print(f'First letter is: {str[0]}')
print(f'Last letter is: {str[-1]}')

# Exercise 3
result = ''
for sym in str:
  result = result + sym
  print(result)

# Exercise 4
str_list = list(str)
random.shuffle(str_list)
str_shuffled = ''.join(str_list)
result = ''
for sym in str_shuffled:
  result = result + sym
  print(result)