# Here is a table of prices for a wedding catering company:
# of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

# 📝 Instructions:

# Please write an program that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.

guests_number = int(input('How many people will be on your wedding? Please type a number: '));
if (guests_number > 200):
  print('It will cost your $20,000')
elif (guests_number > 100 and guests_number <= 200):
  print('It will cost your $15,000')
elif (guests_number > 50 and guests_number <= 100):
  print('It will cost your $10,000')
elif (guests_number <= 50):
  print('It will cost your $4,000')