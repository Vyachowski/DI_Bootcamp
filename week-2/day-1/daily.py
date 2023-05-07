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
for sym in str:
  print(sym)

# Exercise 4
random.shuffle(list(str))
str_new = ''.join(list(str))
for sym in str_new:
  print(sym)