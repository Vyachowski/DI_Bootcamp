# --- GAME LOGIC --- #

import random

class Game:
  '''Simple child game (that called CU-EF-A in Russia) against computer'''

  def __init__(self) -> None:
    self.__move_variants = { 
      'rock': ['rock', 'rok', 'roc', 'r'],
      'paper': ['paper', 'p'],
      'scissors': ['scissors', 'scissor', 'scisors', 'scisors', 's']
      }
    self.__all_moves_list = sum(self.__move_variants.values(), [])

  def get_user_item(self):
    user_variant = ''

    while user_variant not in self.__all_moves_list:
      user_variant = input('Selecet [r]ock, [p]aper or [s]cissors: ') # Need to add a code for printing errors
    user_answer = ''.join([key for key, values in self.__move_variants.items() if user_variant in values])
    return user_answer
  
  def get_computer_item(self):
    computer_answer = random.choice(list(self.__move_variants.keys()))
    return computer_answer

game = Game()
print(game.get_user_item())
print(game.get_computer_item())


# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.