# Exercise 1
# Print the following output in one line of code:
print('Hello world\n'*5 + 'I love python\n'*5)

# Exercise 2
# 1) Ask the user to input a month (1 to 12).
# 2) Display the season of the month received :
#    Spring runs from March (3) to May (5)
#    Summer runs from June (6) to August (8)
#    Autumn runs from September (9) to November (11)
#    Winter runs from December (12) to February (2)
monthNumber = int(input("Please enter a number of a month (from 1 to 12): "))
if ( 2 < monthNumber < 6 ):
  print('It is spring now!')
elif ( 5 < monthNumber < 9 ):
  print('It is summer now!')
elif ( 8 < monthNumber < 12 ):
  print('It is fall now!')
else:
  print('It is winter now!')
