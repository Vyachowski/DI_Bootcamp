# EXERCISE 1

## Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

# IMPORT

from datetime import date

# LOGIC

def get_birthday():
  birthday_input = input('Please enter your birthday in a DD/MM/YYYY format: ')
  birthday_to_numbers = list(map(int, birthday_input.split('/')))
  return {key: value for key, value in zip(['day', 'month', 'year'], birthday_to_numbers)} # => transforming to the object with year, month, day

def calculate_candles(born):
    print(born)
    today = date.today()
    age = today.year - born['year'] - ((today.month, today.day) < (born['month'], born['day']))
    return int(str(age)[-1])

def display_cake(candles_amount = 0):
  cake_icing = '_'
  cake_top_slots = 11
  cake_candles = 'i' * candles_amount
  icing_half = cake_icing * ((cake_top_slots - candles_amount) // 2)

  make_top = icing_half + cake_candles + (icing_half if candles_amount % 2 != 0 else icing_half + '_')
  
  print(f'\t\t    {make_top}     ')
  print( '\t\t   |:H:a:p:p:y:|   ')
  print( '\t\t __|___________|__ ')
  print( '\t\t|^^^^^^^^^^^^^^^^^|')
  print( '\t\t|:B:i:r:t:h:d:a:y:|')
  print( '\t\t|                 |')
  print( '\t\t~~~~~~~~~~~~~~~~~~~')

# OUTPUT
display_cake(3)
display_cake(5)
display_cake(9)
display_cake(10)
display_cake(11)