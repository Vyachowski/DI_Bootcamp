# -- NOT READY YET -- #
# REASON: TOO MUCH TIME SPENT ON PAGINATION EXERCISE

# --- Exercise 1 : Built-In Functions --- #
# Instructions
# Python has many built-in functions.
#  – If you feel that you don’t know how to properly implement them take a look at the python documentation online.
# 1) Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# 2) Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.


# 🌟 Exercise 2: Currencies
# Instructions
# 1) class Currency:
#     def __init__(self, currency, amount):
#       self.currency = currency
#       self.amount = amount
#     # Your code starts HERE
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount
