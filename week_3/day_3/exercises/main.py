# --- 🌟 Exercise 1 : Built-In Functions --- #
# Instructions:
# Python has many built-in functions.
#  – If you feel that you don’t know how to properly implement them take a look at the python documentation online.
# 1) Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# 2) Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# CODE

def display_abs_result(num):
  '''
  This function displays the absolute value of the given number. 
  If the number is positive or zero, it prints the number itself. 
  If the number is negative, it prints the negation of the number.
  '''
  print (num if num >= 0 else -num)

def display_int_result(value):
  '''
  This function prints the integer representation of the given value. 
  It discards any decimal places and outputs the integer part of the value.
  '''
  print (int(value))

def display_input_result(value):
  '''
  This function prompts the user for input by displaying the given value as a prompt.
  It then waits for the user to enter a value and press Enter. 
  Once the user input is received, it is printed to the console.
  '''
  print (input(value))

# OUTPUT

print(display_abs_result.__doc__)     # -> Docs...

print(display_int_result.__doc__)     # -> Docs...

print(display_input_result.__doc__)   # -> Docs...

# --- 🌟 Exercise 2: Currencies --- #
# Instructions:
# 1) class Currency:
#     def __init__(self, currency, amount):
#       self.currency = currency
#       self.amount = amount
#     # Your code starts HERE
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
#:c1 = Currency('dollar', 5)
#:c2 = Currency('dollar', 10)
#:c3 = Currency('shekel', 1)
#:c4 = Currency('shekel', 10)

#:str(c1)
# '5 dollars'

#:int(c1)
# 5

#:repr(c1)
# '5 dollars'

#:c1 + 5
# 10

#:c1 + c2
# 15

#:c1 
# 5 dollars

#:c1 += 5
#:c1
# 10 dollars

#:c1 += c2
#:c1
# 20 dollars

#:c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount


# OUTPUT

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)   # -> '5 dollars'

int(c1)   # -> 5

repr(c1)  # -> '5 dollars'

c1 + 5    # -> 10

c1 + c2   # -> 15

c1        # -> 5 dollars

c1 += 5
c1        # -> 10 dollars

c1 += c2
c1        # -> 20 dollars

c1 + c3   # -> TypeError: Cannot add between Currency type <dollar> and <shekel>