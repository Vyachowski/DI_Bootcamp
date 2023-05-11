# EXERCISE 1
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
import datetime
birth_date = input('Pleasy enter your birthday in a DD/MM/YYYY format: ')
birth_day, birth_month, birth_year = birth_date.split('/')
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)
candles_amount = age[-1]

print(f'\t\t    _{ birth_date }_    ')
print('\t\t   |:H:a:p:p:y:|   ')
print('\t\t __|___________|__ ')
print('\t\t|^^^^^^^^^^^^^^^^^|')
print('\t\t|:B:i:r:t:h:d:a:y:|')
print('\t\t|                 |')
print('\t\t~~~~~~~~~~~~~~~~~~~')
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~