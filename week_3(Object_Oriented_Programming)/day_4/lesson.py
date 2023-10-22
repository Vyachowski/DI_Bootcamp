# --- EXERCISE --- #

# 1) Create a colorize(text, color) function that contain this tuple colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
# 2) If the color is not present in the tuple, raise a ValueError exception
# 3) If the text is not a string raise a TypeError Exception
# 4) make sure to catch the exception

# CODE

def colorize(text, color):
  colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
  try:
    if type(text) != int and type(text) != str: 
      raise TypeError('This is not a string or a number')
    if type(color) != str: 
      raise TypeError('A color vlaue should be a string')
    if color not in colors: 
      raise ValueError('There is no such color')
  except Exception as error:
    print(error)
  else:
    print('Colorized!')
    
# OUTPUT

colorize([], 'orange') # -> This is not a string or a number
colorize('', 'orange') # -> There is no such color
colorize(1, 'orange')  # -> There is no such color
colorize(1, [])        # -> A color vlaue should be a string
colorize(1, 'cyan')    # -> Colorized!