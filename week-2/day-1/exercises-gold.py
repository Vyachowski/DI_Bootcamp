# Exercise 1
print('Hello world\n'*5)
print('I love python\n'*5)

# Exercise 2
monthNumber = int(input("Please enter a number of a month (from 1 to 12): "))
if (monthNumber == 12 or monthNumber < 3):
  print('It is winter now!')
elif (monthNumber < 6 and monthNumber > 2):
  print('It is spring now!')
elif (monthNumber < 9 and monthNumber > 5):
  print('It is summer now!')
else: print('It is fall now!')