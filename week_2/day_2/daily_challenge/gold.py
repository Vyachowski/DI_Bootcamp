# --- HAPPY BIRTHDAY --- #

## Instructions
## 1) Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
## 2) Display a little cake as seen below:
##        ___iiiii___
##       |:H:a:p:p:y:|
##     __|___________|__
##    |^^^^^^^^^^^^^^^^^|
##    |:B:i:r:t:h:d:a:y:|
##    |                 |
##    ~~~~~~~~~~~~~~~~~~~
##    – The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
##    – Bonus : If they were born on a leap year, display two cakes !

# IMPORT

from datetime import date

# DATA

born_leap_year = False

# LOGIC

def get_birthday():
  return input('Please enter your birthday in a DD/MM/YYYY format: ').split('/')

def calculate_birthday_candles(birthday):
  birthday_to_numbers_list = list(map(int, birthday))
  # Transforming to the object with year, month, day
  born = {key: value for key, value in zip(['day', 'month', 'year'], birthday_to_numbers_list)}
  today = date.today()
  age = today.year - born['year'] - ((today.month, today.day) < (born['month'], born['day']))
  return int(str(age)[-1])

def is_year_leap(birthday):
  return True if int(birthday[2]) % 4 == 0 else False

def display_cake(candles_amount = 0):
  cake_icing = '_'
  cake_top_slots = 11
  cake_candles = 'i' * candles_amount
  icing_half = cake_icing * ((cake_top_slots - candles_amount) // 2)
  make_top = icing_half + cake_candles + (icing_half if candles_amount % 2 != 0 else icing_half + '_')
  def print_cake(top):
    print(f'\t\t    {top}     '     )
    print( '\t\t   |:H:a:p:p:y:|   ')
    print( '\t\t __|___________|__ ')
    print( '\t\t|^^^^^^^^^^^^^^^^^|')
    print( '\t\t|:B:i:r:t:h:d:a:y:|')
    print( '\t\t|                 |')
    print( '\t\t~~~~~~~~~~~~~~~~~~~')

  if born_leap_year: print_cake(make_top)
  print_cake(make_top)

# OUTPUT

birthday = get_birthday()
born_leap_year = is_year_leap(birthday)
display_cake(calculate_birthday_candles(birthday))